"""
Implement Non-Maximum Suppression in object detection

NMS filters out multiple detections of the same object, keeping only the most confident one.

🧠 How NMS Works:
1. Sort all detected bounding boxes by their confidence score.
2. Select the box with the highest score and remove it from the list.
3. Compare it with all other boxes:
    - Calculate IoU (Intersection over Union).
    - If IoU > threshold (e.g., 0.5), suppress the box (i.e., it's considered a duplicate).
4. Repeat the process for the next highest-scoring box until none remain.

Time Complexity: O(n log n) sorting, O(n²) comparing each box with each other -> total O(n2)
Space Complexity: O(n)
"""

import numpy as np


def iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1_p, y1_p, x2_p, y2_p = box2

    xi1 = max(x1, x1_p)
    yi1 = max(y1, y1_p)
    xi2 = min(x2, x2_p)
    yi2 = min(y2, y2_p)

    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2_p - x1_p) * (y2_p - y1_p)

    return inter_area / float(box1_area + box2_area - inter_area)


def non_max_suppression(boxes, scores, iou_threshold=0.5):
    indices = np.argsort(scores)[::-1]
    keep = []

    while indices.size > 0:
        current = indices[0]
        keep.append(current)

        rest = indices[1:]
        indices = np.array(
            [idx for idx in rest if iou(boxes[current], boxes[idx]) < iou_threshold]
        )

    return keep
