#!/usr/bin/env python3
"""Implement scaled dot-product attention for the provided matrices."""

import numpy as np


def scaled_dot_product_attention(
    query: np.ndarray, key: np.ndarray, value: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    """Return the attention weights and weighted value output."""
    # Calcuate dot scors and scale by key dimenssion.
    scores = query @ key.T / np.sqrt(key.shape[-1])

    # Apply stable softmax seperatley for each of the querys.
    shifted_scores = scores - np.max(scores, axis=-1, keepdims=True)
    exponentiated_scores = np.exp(shifted_scores)
    attention_weights = exponentiated_scores / np.sum(
        exponentiated_scores, axis=-1, keepdims=True
    )

    # Weigt value vecors to create the final outpt.
    output = attention_weights @ value
    return attention_weights, output


def main() -> None:
    query = np.array([[1, 0, 1, 0], [0, 1, 0, 1]], dtype=float)
    key = np.array([[1, 0, 1, 0], [0, 1, 0, 1]], dtype=float)
    value = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=float)

    attention_weights, output = scaled_dot_product_attention(query, key, value)
    np.set_printoptions(precision=4, suppress=True)

    print("Attention Weights:")
    print(attention_weights)
    print("Final Output:")
    print(output)


if __name__ == "__main__":
    main()
