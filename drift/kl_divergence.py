
import numpy as np
from scipy.stats import entropy

def kl_divergence(p, q):
    """KL Divergence between two distributions."""
    p = np.asarray(p) + 1e-8
    q = np.asarray(q) + 1e-8
    return entropy(p, q)

def detect_drift_kl(W_curr, W_ref, bins=20, threshold=0.5):
    """
    Compare W_curr to W_ref using KL divergence.

    Args:
        W_curr, W_ref: Lists or arrays of recent and reference values
        bins (int): Number of histogram bins
        threshold (float): KL divergence threshold to flag drift

    Returns:
        (bool, float): (drift_detected, kl_score)
    """
    hist_curr, _ = np.histogram(W_curr, bins=bins, density=True)
    hist_ref, _ = np.histogram(W_ref, bins=bins, density=True)
    kl_score = kl_divergence(hist_curr, hist_ref)
    drift = kl_score > threshold
    return drift, kl_score
