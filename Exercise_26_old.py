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
    with open(r'et_temp.txt', 'w') as file:
        file.write(data)
    returnmatrix = np.loadtxt('et_temp.txt', usecols=range(8))
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

def algorithm(matrixalgo, a, b, used=[], failedused=[], counter=[], results=[], failedresults=[], failed=[]):
#     get the input
#     try the one above
#     try the one to the right
#     try the one below
#     try the one to the left
#     return the value of the one that worked
#     return the location of the one that worked
    valueofcurrentcell = int(matrixalgo[a, b])
    print('counter value', counter)
    counter.append(1)
    if [a, b] not in used or len(counter) == 1:
        theoneabove = 0
        theoneright = 0
        theonebelow = 0
        theoneleft = 0
        if a == -1:
            print('failed cause of a-1')
            quit()
        if b == -1:
            print('failed cause of b-1')
            quit()

        if a != 0:
            theoneabove = int(matrixalgo[a-1, b])
        if b != 7:
            theoneright = int(matrixalgo[a, b+1])
        if a != 7:
            theonebelow = int(matrixalgo[a+1, b])
        if b != 0:
            theoneleft = int(matrixalgo[a, b-1])

        resultabove = findcommondivisor(valueofcurrentcell, theoneabove)
        if [a, b] in used:
            resultabove = False
        resultright = findcommondivisor(valueofcurrentcell, theoneright)
        if [a, b] in used:
            resultright = False
        resultbelow = findcommondivisor(valueofcurrentcell, theonebelow)
        if [a, b] in used:
            resultbelow = False
        resultleft = findcommondivisor(valueofcurrentcell, theoneleft)
        if [a, b] in used:
            resultleft = False
        if resultabove == False and resultright== False and resultbelow == False and resultbelow == False:
            used = used[-2]
        used.append([a, b])
        results.append([resultabove,resultright,resultbelow,resultleft])
        if len(counter) != 1:
            counter.clear()
            if len(counter) >= 3:
                print('quite becuase of counter len being', len(counter))
                quit()
        print(a,b)

        if resultabove == True:
            return [a - 1, b]
        elif resultright == True:
            return [a, b + 1]
        elif resultbelow == True:
            return [a + 1, b]
        elif resultleft == True:
            return [a, b - 1]

    if len(counter) == 2:
        resultabove = (results[-1])[0]
        resultright = (results[-1])[1]
        resultbelow = (results[-1])[2]
        resultleft = (results[-1])[3]
        theoneabove = 0
        theoneright = 0
        theonebelow = 0
        theoneleft = 0
        a = (used[-2])[0]
        b = (used[-2])[1]
        if True in (results[-1]):
            i = ((results[-1]).index(True))+1
        else:
            if True in (results[-2]):
                i = ((results[-2]).index(True))+1
            else:
                print('reached end of code cause idiot')
                quit()


        if i==0:
            if a != 0:
                theoneabove = int(matrixalgo[a - 1, b])
            resultabove = findcommondivisor(valueofcurrentcell, theoneabove)
        if i == 1:
            if b != 7:
                theoneright = int(matrixalgo[a, b + 1])
            resultright = findcommondivisor(valueofcurrentcell, theoneright)
        if i == 2:
            if a != 7:
                theonebelow = int(matrixalgo[a + 1, b])
            resultbelow = findcommondivisor(valueofcurrentcell, theonebelow)
        if i == 3:
            if b != 0:
                theoneleft = int(matrixalgo[a, b - 1])
            resultleft = findcommondivisor(valueofcurrentcell, theoneleft)
        if i == 4:
            if a != 0:
                theoneabove = int(matrixalgo[a - 1, b])
            resultabove = findcommondivisor(valueofcurrentcell, theoneabove)

        failedused.append([a, b])
        failedresults.append([resultabove, resultright, resultbelow, resultleft])
        counter.clear()
        print('used when failed', failedused)

        if resultabove == True:
            return [a - 1, b]
        elif resultright == True:
            return [a, b + 1]
        elif resultbelow == True:
            return [a + 1, b]
        elif resultleft == True:
            return [a, b - 1]
        else:
            print('failed because dumb')
            quit()
    else:
        failed.append(1)
        counter.append(1)
        if len(failed) == 10:
            quit()
        return [5, 5]

def findpath(matrix,startx,starty,endx,endy):
    n = False
    while n != True:
        returndvalue = algorithm(matrix, startx, starty)
        if returndvalue == False:
            print('Finished unsuccessfully cause False')
            quit()
        if returndvalue == None:
            print('Finished unsuccessfully cause None')
            quit()
        if not returndvalue:
            startx=5
            starty=5
            continue
        if returndvalue == [endx, endy]:
            n = True
            print('Finished successfully')
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