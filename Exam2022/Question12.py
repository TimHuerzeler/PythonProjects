# def same_length(lst_lst: List[List[Any]]) -> bool:
def same_length(lst_lst: [[1, 2, 3], ['a', 'b'], [5, 6, 7]]) -> bool:
    length = len(lst_lst)
    if len(lst_lst) == 0:
        return True
    else:
        def iterate(lst, start, end):
            if start < 0 or end >= len(lst) or start > end:
                return
            print(lst[start])
            iterate(lst, start + 1, end)

        all = iterate(lst_lst, 1, length)
        print(all)
        return

my_list = [[1, 2, 3], ['a', 'b'], [5, 6, 7]]

same_length(my_list)
