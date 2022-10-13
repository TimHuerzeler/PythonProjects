# Develop a function that returns the greatest value of a list of positive numbers.

#Author: TimHuerzeler
#Date: 06.10.2022
from random import  randint
def greatest(a):
    b= max(a)
    return b
def main():
    # lst = [4, 7, 8, 2, 5, 10]
    lst = []
    for x in range(0, 101):
        lst.append(randint(0, 100))

    print(lst)
    print('The greatest element is {}.'.format(greatest(lst)))

if __name__ == "__main__":
    main()
