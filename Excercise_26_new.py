#Author: TimHuerzeler
#Date: 06.10.2022
import numpy as np

class AlienfindShip:
    def __init__(self, beginning, ending):
        self.beginning = beginning
        self.ending = ending

    def loadtext(self):
        search_text1 = "X"
        search_text2 = "Y"
        replace_text = "1"
        with open(r'et.txt', 'r') as file:
            data = file.read()
            data = data.replace(search_text1, replace_text)
            data = data.replace(search_text2, replace_text)
        with open(r'et1.txt', 'w') as file:
            file.write(data)
        returnmatrix = np.loadtxt('et1.txt', usecols=range(8))
        return returnmatrix

    def findcommondivisor(self,a,b):
        n = 0
        for i in range(1, min(a, b) + 1):
            if a % i == b % i == 0:
                n += 1
        if n>1:
            return True
        else:
            return False

    def algorithm(self,a,b):
        beginning = a
        end = b
        happened = []
        matrix = AlienfindShip.loadtext('car')
        happened.append("orange")

    def pathfinder(self, matrix, start, end):
        n = False
        while n != True:
            returndvalue = algorithm(matrix, startx, starty)
            if not returndvalue:
                startx = 5
                starty = 5
                continue
            if returndvalue == [endx, endy]:
                n = True
            startx = returndvalue[0]
            starty = returndvalue[1]

    def main(self):
        start = (AlienfindShip.loadtext('car'))[5, 5]
        finish = (AlienfindShip.loadtext('car'))[2, 2]
        print('This is the startingpoint value', start)
        print('This is the startingpoint location X=5 & Y=5')

def main():
    AlienfindShip.algorithm('car',1,1)
    AlienfindShip.main('car')



if __name__ == "__main__":
    main()