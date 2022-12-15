def flat(lst_lst):
    """flats a list of lists without using any predefined functions."""
    res_lst = []
    for l in lst_lst:
        res_lst += l
    return res_lst


def main():
    """ Launcher """
    print(flat([[2,3],[4,5,6],[],[7]]))

if __name__ == "__main__":
    main()
