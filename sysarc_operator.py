"""
System Architecture Operators: Π_Oh -> Θ_φ -> Γ transformation.
"""

def Pi_Oh(input_vec):
    """Project input onto octahedral symmetry."""
    return np.round(input_vec / np.linalg.norm(input_vec), 3)

def Theta_phi(input_vec):
    """Apply golden-ratio scaling."""
    phi = (1 + 5 ** 0.5) / 2
    return input_vec * phi

def Gamma_transform(input_vec):
    """Generalized channel permutation."""
    return np.roll(input_vec, 1)
