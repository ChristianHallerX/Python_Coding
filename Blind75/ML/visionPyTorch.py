from torch.utils.data import Dataset
import numpy as np
import math
import cv2
import torch
from typing import List, Tuple

# Device configuration: use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

####################################### Data #######################################


class CircleDataset(Dataset):
    """This class can be used to generate blank canvases and draw a single
    circle with a random radius, position, and color in ranges defined by
    the user.
    """

    def __init__(
        self,
        size: int = 100,
        min_radius: float = 0.0,
        max_radius: float = 10.0,
        image_size_wh: List = [100, 100],
        colors: List = [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    ):
        self.size = size
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.image_size_wh = image_size_wh
        self.color_map = colors
        self.gen = torch.Generator()
        self.gen.manual_seed(42)
        self.images, self.pos_labels, self.color_labels = self._generate_data()

    @staticmethod
    def generate_image_tensor(
        cx: float,
        cy: float,
        r: float,
        img_w: int,
        img_h: int,
        color: List[int],
        fill: bool = True,
    ) -> torch.Tensor:
        blank_image = np.zeros((img_h, img_w, 3), np.uint8)
        coords = (cx - r, cy - r, cx + r, cy + r)
        cv2.circle(
            blank_image,
            (int(cx), int(cy)),
            max(int(r), 0),
            color,
            cv2.FILLED if fill else 3,
        )
        img_arr = torch.from_numpy(blank_image.transpose((2, 0, 1))).type(torch.float)
        return img_arr

    def _generate_data(self) -> Tuple[List, List, List]:
        images, color_labels, pos_labels = [], [], []
        w, h = self.image_size_wh
        for i in range(0, self.size):
            # select random parameters of the circle
            r = (
                torch.rand(1, generator=self.gen).item()
                * (self.max_radius - self.min_radius)
                + self.min_radius
            )
            cx = torch.rand(1, generator=self.gen).item() * w
            cy = torch.rand(1, generator=self.gen).item() * h
            color = torch.randint(
                0, len(self.color_map), (1,), generator=self.gen
            ).item()
            img_tensor = CircleDataset.generate_image_tensor(
                cx, cy, r, w, h, self.color_map[color]
            )
            images.append(img_tensor)
            pos_labels.append(torch.tensor([cx, cy, r], dtype=torch.float))
            color_labels.append(torch.tensor(color))
        return images, pos_labels, color_labels

    def __getitem__(self, idx: int) -> torch.Tensor:
        return self.images[idx], self.pos_labels[idx], self.color_labels[idx]

    def __len__(self) -> int:
        return self.size

    def visualize_(self, cols: int = 10, max_viz: int = 100) -> None:
        # visualize only the first max_viz elements
        CircleDataset.visualize(self.images[0:max_viz], cols=cols)

    @staticmethod
    def create_image_grid(images: List[torch.Tensor], cols=10) -> torch.Tensor:
        assert len(images) > 0
        h, w = images[0].shape[1], images[0].shape[2]
        rows = math.ceil(len(images) / cols)
        image_grid = torch.zeros(3, rows * h, cols * w)

        # fill image_grid with images
        for i, img in enumerate(images):
            r_idx = (i // cols) * h
            c_idx = (i % cols) * w
            image_grid[:, r_idx : r_idx + h, c_idx : c_idx + w] = img
        # draw marker white lines to make visualization nicer
        for r in range(0, rows):
            image_grid[:, r * h, :] = 255
        for c in range(0, cols):
            image_grid[:, :, c * w] = 255
        return image_grid.permute(1, 2, 0).int()

    # @staticmethod
    # def visualize(gt_images: List[torch.Tensor],
    #               pred_images: List[torch.Tensor]=None,
    #               cols=10) -> None:
    #   """ Given a list of image (GT) tensors and prediction tensors,
    #   this helper function can visualize them in a grid pattern.
    #   """
    #   assert len(gt_images)>0
    #   if pred_images:
    #     assert len(gt_images) == len(pred_images)
    #   rows = math.ceil(len(gt_images) / cols)
    #   fig = plt.figure(figsize=[cols, rows])
    #   gt_grid = CircleDataset.create_image_grid(gt_images, cols)
    #   if not pred_images:
    #     plt.imshow(gt_grid)
    #   else:
    #     pred_grid = CircleDataset.create_image_grid(pred_images, cols)
    #     plt.imshow((gt_grid/1.5 + pred_grid).int())


test_dataset = CircleDataset(100, max_radius=10.0)
# test_dataset.visualize_()

####################################### Model #######################################

import torch.nn as nn


class CircleRegressor(nn.Module):
    def __init__(
        self, input_size: int = 100, input_chans: int = 3, num_colors: int = 3
    ):
        super(CircleRegressor, self).__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(input_chans, 16, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
        )
        # For an input image of 100x100 and four layers with stride 2:
        # 100 -> 50 -> 25 -> 13 -> 7, so the feature map is 7x7 with 32 channels.
        feature_size = 32 * 7 * 7  # 1568
        # Regress raw logits for color (for CrossEntropyLoss)
        self.color_predictor = nn.Linear(feature_size, num_colors)
        # Regress 3-tuple: x0, y0, radius
        self.location_predictor = nn.Linear(feature_size, 3)
        self.color_loss = nn.CrossEntropyLoss()
        self.loc_loss = nn.MSELoss()

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        batch = x.shape[0]
        features = self.backbone(x)
        features_flat = features.view(batch, -1)
        location = self.location_predictor(features_flat)
        color_logits = self.color_predictor(features_flat)

        if not self.training:
            # In evaluation mode, convert logits to probabilities and get the predicted class
            _, color = torch.max(torch.softmax(color_logits, dim=1), dim=1)
            return location, color

        return location, color_logits

    def compute_loss(
        self,
        loc: torch.Tensor,
        loc_label: torch.Tensor,
        color: torch.Tensor,
        color_label: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        # Correctly compute the location loss comparing predictions with ground truth.
        loc_loss = self.loc_loss(loc, loc_label)
        color_loss = self.color_loss(color, color_label)
        return loc_loss, color_loss


####################################### training + eval #######################################
from torch.utils.data import DataLoader
import torch.optim as optim


def run_train(
    dataset: torch.utils.data.Dataset,
    model: torch.nn.Module,
    optimizer: torch.optim.Optimizer,
    num_epochs: int = 10,
    batch_size: int = 8,
) -> None:
    train_loader = DataLoader(dataset, batch_size=batch_size, num_workers=8)
    loss_arr = []

    model.train()  ########## Set model to training mode

    for epoch in range(num_epochs):
        epoch_loss = 0.0
        epoch_correct = 0
        epoch_total = 0
        num_batches = 0
        for i, (inputs, loc_label, color_label) in enumerate(train_loader):

            # 0. Transfer inputs and labels to the device (GPU or CPU)
            inputs = inputs.to(device)
            loc_label = loc_label.to(device)
            color_label = color_label.to(device)

            # 1. Optimizer zero grad
            optimizer.zero_grad()

            # 2. Forward Pass. In training mode, forward returns raw logits for color
            location, color_logits = model(inputs)

            # 3. Loss (custom for loc and color)
            loc_loss, color_loss = model.compute_loss(
                location, loc_label, color_logits, color_label
            )
            total_loss = loc_loss + color_loss
            loss_arr.append(total_loss.item())

            # 4. Backprop
            total_loss.backward()

            # 5
            #
            #
            # . Gradient Descent
            optimizer.step()

            # Compute accuracy for the color classification
            pred_color = torch.argmax(color_logits, dim=1)
            epoch_correct += (pred_color == color_label).sum().item()
            epoch_total += color_label.size(0)
            epoch_loss += total_loss.item()
            num_batches += 1

        avg_loss = epoch_loss / num_batches if num_batches > 0 else 0
        train_acc = epoch_correct / epoch_total if epoch_total > 0 else 0
        print(
            f"Epoch: {epoch}, Average Loss: {avg_loss:.4f}, Training Color Accuracy: {train_acc * 100:.2f}%"
        )

    print("Training complete")
    # fig, ax = plt.subplots()
    # ax.plot(range(len(loss_arr)), loss_arr)
    # ax.set_title("Loss over iterations")
    # plt.show()


def run_eval(dataset: torch.utils.data.Dataset, model: torch.nn.Module):
    eval_loader = DataLoader(dataset, batch_size=8, num_workers=8)

    model.eval()  ################ Set model to evaluation mode

    eval_images = []
    pred_images = []
    total_correct = 0
    total_samples = 0

    with torch.no_grad():  ### eval mode does not require gradient tracking, less data, faster
        for i, (inputs, loc_label, color_label) in enumerate(eval_loader):
            ######### Move inputs and labels to the device (GPU or CPU)
            inputs = inputs.to(device)
            loc_label = loc_label.to(device)
            color_label = color_label.to(device)

            b, c, h, w = inputs.shape  # NCHW
            # In eval mode, forward returns predicted color indices
            loc, pred_color = model(inputs)
            total_correct += (pred_color == color_label).sum().item()
            total_samples += color_label.size(0)

            # # Generate visualizations using predictions
            # for img, pred_loc, p_color in zip(inputs, loc, pred_color):
            #     eval_images.append(img)
            #     pred_image = CircleDataset.generate_image_tensor(
            #         pred_loc[0],
            #         pred_loc[1],
            #         pred_loc[2],
            #         w,
            #         h,
            #         dataset.color_map[p_color.item()],
            #         fill=False,
            #     )
            #     pred_images.append(pred_image)

    eval_acc = total_correct / total_samples if total_samples > 0 else 0
    print(f"Evaluation Color Accuracy: {eval_acc * 100:.2f}%")
    # CircleDataset.visualize(eval_images, pred_images)


if __name__ == "__main__":
    print(f"torch version: {torch.__version__}")
    print(f"cuda version: {torch.version.cuda}")
    print(f"using {device}")

    # Assuming CircleDataset and CircleRegressor have been defined as per the previous updates
    img_size = 100
    train_dataset = CircleDataset(
        size=100, image_size_wh=[img_size, img_size], max_radius=75, min_radius=25
    )
    eval_dataset = CircleDataset(size=100, image_size_wh=[img_size, img_size])
    model = CircleRegressor(input_size=img_size).to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-1)

    run_train(train_dataset, model, optimizer, num_epochs=10, batch_size=8)
    run_eval(eval_dataset, model)
