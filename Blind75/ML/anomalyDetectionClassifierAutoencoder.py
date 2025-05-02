import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset


# Define model architecture
class Autoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim=32):
        super(Autoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(True),
            nn.Linear(64, latent_dim),
            nn.ReLU(True),
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(True),
            nn.Linear(64, input_dim),
            nn.Sigmoid(),
        )

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon


# Helper: Training loop
def train_autoencoder(model, dataloader, n_epochs=50, lr=1e-3, device="cpu"):
    model = model.to(device)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    for epoch in range(1, n_epochs + 1):
        # set to training mode
        model.train()
        running_loss = 0.0
        for batch in dataloader:
            # 0. Transfer inputs and labels to the device (GPU or CPU)
            x_batch = batch[0].to(device)

            # 1. Optimizer zero grad
            optimizer.zero_grad()

            # 2. Forward Pass
            x_recon = model(x_batch)

            # 3. Loss
            loss = criterion(x_recon, x_batch)

            # 4. Backprop
            loss.backward()

            # 5. Gradient Descent
            optimizer.step()

            # batch loss
            running_loss += loss.item() * x_batch.size(0)

        # epoch loss
        epoch_loss = running_loss / len(dataloader.dataset)

        # print epoch loss
        if epoch % 10 == 0 or epoch == 1:
            print(f"Epoch {epoch}/{n_epochs}, Loss: {epoch_loss:.6f}")
    return model


def compute_reconstruction_errors(model, dataloader, device="cpu"):
    model = model.to(device)
    # set to evaluation mode
    model.eval()
    errors = []
    with torch.no_grad():
        for batch in dataloader:
            x_batch = batch[0].to(device)
            x_recon = model(x_batch)
            batch_errors = torch.mean((x_batch - x_recon) ** 2, dim=1)
            errors.append(batch_errors.cpu())
    errors = torch.cat(errors).numpy()
    return errors


def main():
    # Example synthetic data (replace with your dataset loading)
    import numpy as np

    rng = np.random.RandomState(42)
    # Generate normal data
    normal_data = rng.normal(loc=0.0, scale=1.0, size=(10000, 20))
    # Generate anomalies
    anomaly_data = rng.normal(loc=5.0, scale=1.0, size=(200, 20))

    # Combine normal and anomaly data and assign labels
    data = np.concatenate([normal_data, anomaly_data], axis=0)
    labels = np.array([0] * len(normal_data) + [1] * len(anomaly_data))

    # Shuffle before splitting to distribute anomalies across both sets
    perm = rng.permutation(len(labels))
    data = data[perm]
    labels = labels[perm]

    # Split into train/test (e.g., 80% train, 20% test)
    split_idx = int(0.8 * len(labels))
    train_data, test_data = data[:split_idx], data[split_idx:]
    train_labels, test_labels = labels[:split_idx], labels[split_idx:]

    # Create DataLoaders
    train_loader = DataLoader(
        TensorDataset(torch.FloatTensor(train_data)), batch_size=128, shuffle=True
    )
    test_loader = DataLoader(
        TensorDataset(torch.FloatTensor(test_data)), batch_size=128, shuffle=False
    )
    train_loader = DataLoader(
        TensorDataset(torch.FloatTensor(train_data)), batch_size=128, shuffle=True
    )
    test_loader = DataLoader(
        TensorDataset(torch.FloatTensor(test_data)), batch_size=128, shuffle=False
    )

    # Train model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"using device {device}")
    model = Autoencoder(input_dim=train_data.shape[1], latent_dim=16)
    print("Starting training...")
    model = train_autoencoder(model, train_loader, n_epochs=50, lr=1e-3, device=device)

    # Compute reconstruction errors on test set
    test_errors = compute_reconstruction_errors(model, test_loader, device=device)

    # Compute reconstruction errors on train set and Choose threshold (e.g., 95th percentile of train errors)
    train_errors = compute_reconstruction_errors(
        model,
        DataLoader(TensorDataset(torch.FloatTensor(train_data)), batch_size=128),
        device=device,
    )
    threshold = np.percentile(train_errors, 95)
    print(f"Anomaly detection threshold: {threshold:.6f}")

    # Predict anomalies in test set
    preds = (test_errors > threshold).astype(int)
    from sklearn.metrics import classification_report

    print("Test Set prediction report")
    print(classification_report(test_labels, preds, target_names=["Normal", "Anomaly"]))


if __name__ == "__main__":
    main()
