import numpy as np
from scipy.stats import entropy

def compute_histogram(data, bins=10):
    """
    Compute a normalized histogram (i.e. a probability distribution) from the raw data.
    
    Parameters:
        data (array-like): The raw sample data.
        bins (int): The number of bins to use.
    
    Returns:
        hist (np.array): A normalized histogram that sums to 1.
    """
    hist, _ = np.histogram(data, bins=bins, density=True)
    # Add a small constant to avoid zero probabilities
    hist = hist + 1e-8
    # Normalize explicitly to ensure sum equals 1
    hist = hist / np.sum(hist)
    return hist

def kl_divergence_from_samples(data_p, data_q, bins=10):
    """
    Compute the KL divergence between two sets of samples by converting them into histograms.
    
    Parameters:
        data_p, data_q: Raw sample data for the two distributions.
        bins (int): Number of bins for histogram creation.
    
    Returns:
        float: The KL divergence between the two distributions.
    """
    p = compute_histogram(data_p, bins)
    q = compute_histogram(data_q, bins)
    return entropy(p, q)

def jensen_shannon_divergence_from_samples(data_p, data_q, bins=10):
    """
    Compute the Jensen-Shannon divergence between two sets of samples.
    
    Parameters:
        data_p, data_q: Raw sample data.
        bins (int): Number of bins.
    
    Returns:
        float: The Jensen-Shannon divergence.
    """
    p = compute_histogram(data_p, bins)
    q = compute_histogram(data_q, bins)
    m = (p + q) / 2.0
    return 0.5 * entropy(p, m) + 0.5 * entropy(q, m)

def hellinger_distance_from_samples(data_p, data_q, bins=10):
    """
    Compute the Hellinger distance between two sets of samples.
    
    Parameters:
        data_p, data_q: Raw sample data.
        bins (int): Number of bins.
    
    Returns:
        float: The Hellinger distance (0 indicates identical distributions; 1 indicates maximum difference).
    """
    p = compute_histogram(data_p, bins)
    q = compute_histogram(data_q, bins)
    return np.sqrt(np.sum((np.sqrt(p) - np.sqrt(q)) ** 2)) / np.sqrt(2)

def categorize_drift(div_value, method='kl'):
    """
    Categorize the type of drift based on the computed divergence value.
    
    Parameters:
        div_value (float): The divergence value.
        method (str): The divergence method used ('kl', 'js', or 'hellinger').
    
    Returns:
        str: A label indicating the drift type ("abrupt", "gradual", or "stable").
        
    Note:
        The threshold values here are hypothetical. You should calibrate them based on your data.
    """
    if method in ['kl', 'js']:
        if div_value > 1.0:
            return "abrupt"
        elif div_value > 0.5:
            return "gradual"
        else:
            return "stable"
    elif method == 'hellinger':
        if div_value > 0.7:
            return "abrupt"
        elif div_value > 0.4:
            return "gradual"
        else:
            return "stable"
    else:
        return "unknown"
