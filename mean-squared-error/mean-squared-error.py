import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    a = np.array(y_pred)
    b = np.array(y_true)

    c = a-b
    d = np.square(c)
    result = np.mean(d)
    return result
    
        
    pass
