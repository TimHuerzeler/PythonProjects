# Develop a function that computes the area of a disc of a given radius.

#Author: TimHuerzeler
#Date: 06.10.2022
import math

pi = math.pi
def calculatearea():
    while True:
        num = int(input("Input a number: "))
        result=num**2*pi
        print('The circle would have a circumference of {}.'.format(result))

if __name__ == "__main__":
    calculatearea()