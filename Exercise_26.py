#Author: TimHuerzeler
#Date: 06.10.2022

import numpy as np

def loadtext():
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
def findcommondivisor(a,b):
    n = 0
    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            n += 1
    if n>1:
        return True
    else:
        return False

def algorithm(matrixalgo, a,b):
#     get the input
#     try the one above
#     try the one to the right
#     try the one below
#     try the one to the left
#     return the value of the one that worked
#     return the location of the one that worked
    valueofcurrentcell = matrixalgo[a, b]
    theoneabove = matrixalgo[a, b-1]
    theoneright = matrixalgo[a+1, b]
    theonebelow = matrixalgo[a, b+1]
    theoneleft = matrixalgo[a-1, b]
    resultabove = findcommondivisor(valueofcurrentcell, theoneabove)
    resultright = findcommondivisor(valueofcurrentcell, theoneright)
    resultbelow = findcommondivisor(valueofcurrentcell, theonebelow)
    resultleft = findcommondivisor(valueofcurrentcell, theoneleft)
    if resultabove == True:
        return resultabove
    elif resultright == True:
        return resultright
    elif resultbelow == True:
        return resultbelow
    elif resultleft == True:
        return resultleft

def findpath(matrix,int startx,int starty,int endx,int endy):
    n = False
    while n != True:
        algorithm(matrix, startx,starty)
        returndvalue = np.where(matrix == algorithm(matrix))[0]
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