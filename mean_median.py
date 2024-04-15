import numpy as np

def calculation(numbers):
    """
    _summary_

    Parameters
    ----------
    numbers :list
        _List of numbers

    Returns
    -------
    dict
        {"std":standard_deviation,"mean":mean,
        "median":median}
    """
    if len(numbers)==0:
        return {"std":None,"mean":None,"median":None}
    std=round(np.std(numbers),3)
    mean=round(np.mean(numbers),3)
    medain=round(np.median(numbers),3)
    return {"std":std,"mean":mean,"median":medain}
