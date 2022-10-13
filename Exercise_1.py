# Develop a function that returns True if its parameter is even, False otherwise.

#Author: TimHuerzeler
#Date: 06.10.2022


def even(b):
    if b/2 == 0:
        return True
    else:
        return False

def trueornot():
    while True:
        num = int(input("Input a number: "))
        if even(num):
            print('{} is even.'.format(num))
        else:
            print('{} is odd.'.format(num))

if __name__ == "__main__":
    trueornot()
