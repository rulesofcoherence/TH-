"""
Core invariants and lattice geometry functions for THÆ.
"""

import numpy as np

def octahedral_clusters(codon_matrix):
    """
    Cluster codons into 8 octahedral attractors.
    codon_matrix: [64, feature_dims] numpy array.
    Returns: cluster_labels [64]
    """
    from sklearn.cluster import KMeans
    model = KMeans(n_clusters=8, random_state=42)
    labels = model.fit_predict(codon_matrix)
    return labels

def divergence_free_modes(data_matrix, n=10):
    """
    Decompose input data into n divergence-free toroidal modes.
    data_matrix: [n_samples, n_features]
    Returns: [n_samples, n] mode projections
    """
    # Placeholder: Set up SVD for modes
    U, S, Vt = np.linalg.svd(data_matrix, full_matrices=False)
    modes = U[:, :n]
    return modes

def exchange_channels(adjacency_matrix, n=18):
    """
    Identify exchange channels in an adjacency/graph matrix.
    adjacency_matrix: [nodes, nodes]
    Returns: channel_indices or subgraphs
    """
    # Take top-k eigenvectors as "channels"
    eigvals, eigvecs = np.linalg.eigh(adjacency_matrix)
    idx = np.argsort(-np.abs(eigvals))[:n]
    channels = eigvecs[:, idx]
    return channels

def golden_ratio_asymmetry(seq):
    """
    Compute temporal asymmetry τ₊/τ₋ and compare to φ (golden ratio).
    seq: np.array time series
    Returns: observed_ratio, percent_error_to_phi
    """
    tau_plus = np.mean(seq[seq > 0])
    tau_minus = -np.mean(seq[seq < 0])
    observed = tau_plus / tau_minus if tau_minus != 0 else np.nan
    phi = (1 + np.sqrt(5)) / 2
    error = 100 * abs(observed - phi) / phi
    return observed, error
