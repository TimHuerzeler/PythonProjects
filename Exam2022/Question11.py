def same_length(lst_lst: [[1, 2, 3], ['a', 'b'], [5, 6, 7]]) -> bool:
     if len(lst_lst) == 0:
         return True
     else:
         all(len(i) == len(lst_lst[0]) for i in lst_lst)
         print(all)
         return

my_list = [[1, 2, 3], ['a', 'b'], [5, 6, 7]]

same_length(my_list)
