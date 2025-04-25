"""
Top-k confidence scores from a list (and optionally their indices)

Time Complexity O(n + k log k) sorting k only, O(n) slicing -> total O
Space Complexity O(k)
"""

import numpy as np


def top_k_scores(scores, k):
    scores = np.array(scores)

    topk_indices = np.argpartition(scores, -k)[-k:]
    # indices of top k scores, descending
    topk_scores = scores[topk_indices]
    return topk_scores, topk_indices


if __name__ == "__main__":
    scores = [0.2, 0.9, 0.4, 0.95, 0.3]
    k = 3

    topk_scores, topk_indices = top_k_scores(scores, k)
    print(topk_scores)  # [0.95 0.9  0.4 ]
    print(topk_indices)  # [3 1 2]
