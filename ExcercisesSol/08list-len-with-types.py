# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional

def list_len(lst : List[str]) -> List[int]:
    """
    Takes a list of strings and returns a list of integers where
    the values are the length of each string.
    """
    res_lst = []
    for s in lst:
        res_lst += [len(s)] 
    return res_lst
