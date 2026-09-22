import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    # if isinstance(x, list):
    #     return 1 / (1 + np.exp(np.negative(x)))
    # else:
    #     

    return 1 / (1 + np.exp(np.negative(x)))

    # return np.array([1 / (1 + np.exp(np.negative(i))) for i in x])