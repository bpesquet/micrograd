"""
Regression metrics
"""

import numpy as np
from pyfit.tensor import Tensor


def mean_squared_error(expected: Tensor, predicted: Tensor) -> float:
    """
    Mean Squared Error
    """
    return np.square(expected - predicted).mean()