#Author: TimHuerzeler
#Date: 06.10.2022

import numpy as np

def loadtext():
    search_text1 = "X"
    search_text2 = "Y"
    replace_text = "2"
    with open(r'et.txt', 'r') as file:
        data = file.read()
        data = data.replace(search_text1, replace_text)
        data = data.replace(search_text2, replace_text)
    with open(r'et1.txt', 'w') as file:
        file.write(data)
    returnmatrix = np.loadtxt('et1.txt', usecols=range(8))
    return returnmatrix
def findcommondivisor(a,b):
    n = 0
    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            n += 1
    if n>1:
        return True
    else:
        return False

def algorithm(matrixalgo, a,b, used=[]):
#     get the input
#     try the one above
#     try the one to the right
#     try the one below
#     try the one to the left
#     return the value of the one that worked
#     return the location of the one that worked
    valueofcurrentcell = int(matrixalgo[a, b])
    if [a, b] not in used:
        print(used)
        theoneabove = int(matrixalgo[a, b-1])
        theoneright = int(matrixalgo[a+1, b])
        theonebelow = int(matrixalgo[a, b+1])
        theoneleft = int(matrixalgo[a-1, b])
        resultabove = findcommondivisor(valueofcurrentcell, theoneabove)
        resultright = findcommondivisor(valueofcurrentcell, theoneright)
        resultbelow = findcommondivisor(valueofcurrentcell, theonebelow)
        resultleft = findcommondivisor(valueofcurrentcell, theoneleft)
        used.append([a, b])
        
        print(a,b)
        if resultabove == True:
            return [a, b-1]
        elif resultright == True:
            return [a+1, b]
        elif resultbelow == True:
            return [a, b+1]
        elif resultleft == True:
            return [a-1, b]
    else:
        return False

def findpath(matrix,startx,starty,endx,endy):
    n = False
    while n != True:
        returndvalue = algorithm(matrix, startx, starty)
        if not returndvalue:
            startx=5
            starty=5
            continue
        if returndvalue == [endx, endy]:
            n = True
        startx = returndvalue[0]
        starty = returndvalue[1]


def main():
    results = []
    matrix = loadtext()
    print(matrix)
    start = matrix[5, 5]
    finish = matrix[2, 2]
    print('This is the startingpoint value',start)
    print('This is the startingpoint location X= 5 & Y=5')
    # start = matrixalgo[5, 5]
    # finish = matrixalgo[2, 2]
    findpath(matrix, 5,5,2,2)

if __name__ == "__main__":
    main()