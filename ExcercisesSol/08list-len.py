def list_len(lst):
    """
    Takes a list of strings and returns a list of integers where
    the values are the length of each string.
    """
    res_lst = []
    for s in lst:
        res_lst += [len(s)] 
    return res_lst
