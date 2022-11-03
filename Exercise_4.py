# Develop a function that reverses a list of elements (try to develop an iterative and a recursive solution).

#Author: TimHuerzeler
#Date: 06.10.2022
from random import  randint

def sort(a):
    b = a.reverse
    return b

def main():
    lst = []
    for x in range(0, 101):
        lst.append(randint(0, 100))
    print('Sorted list {}.'.format(lst.reverse()))

if __name__ == "__main__":
    main()