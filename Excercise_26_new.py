#Author: TimHuerzeler
#Date: 17.12.2022
import numpy as np

def get_position(matrix, value):
    location = np.where(matrix == value)
    return location[0]

def loadtext(textfile,search_txt1,search_txt2,replace_txt):
    with open(textfile, 'r') as infile, open('et_temp.txt', 'w') as outfile:
        data = infile.read()
        data = data.replace(search_txt1, replace_txt)
        data = data.replace(search_txt2, replace_txt)
        outfile.write(data)
    matrix = np.loadtxt('et1.txt', usecols=range(8))
    return matrix

def findcommondivisor(a,b):
    n = 0
    if a == 1 or b ==1:
        return True
    for i in range(1, min(a, b) + 1):
        if a % i == b % i == 0:
            n += 1
    if n>1:
        return True
    else:
        return False

def algo(matrix,x,y,used = []):
    uabove=1
    uright=1
    ubelow=1

    current = int(matrix[x,y])
    # print(current)
    # print(used)

    if x == 2 and y == 2:
        print('succesfull')
        quit()

    if y == 0: left = 0
    else: left = int(matrix[x,y-1])
    if x == 7: below = 0
    else: below = int(matrix[x+1,y])
    if y == 7: right = 0
    else: right = int(matrix[x,y+1])
    if x == 0: above = 0
    else: above = int(matrix[x-1,y])

    if above == 1 or right == 1 or below == 1 or left == 1:
        if x<=3 and y<=3:
            print('Succesfull')
            used.append([current])
            if above == 1:
                used.append([above])
            if right == 1:
                used.append([right])
            if below == 1:
                used.append([below])
            if left == 1:
                used.append([left])
            print('These Fields where visited to reach the spaceship:', '\n', used)
            quit()

    if current != 1:
        if [above] == used[-1]:
            uabove = 0
        if [left] == used[-1]:
            uleft = 0
        if [below] == used[-1]:
            ubelow = 0

    if ([current] in used):
        if current == 2:
            return
        if used[-1] == [above]:
            uabove=0
        if used[-1] == [right]:
            uright=0
        if used[-1] == [below]:
            ubelow=0
        if used.count([above]) >= 10:
            uabove = 0
        if used.count([right]) >= 10:
            uabove = 0
            uright = 0
        if used.count([below]) >= 10:
            uabove = 0
            uright = 0
            ubelow = 0

    if (findcommondivisor(current,above)) == True and uabove == 1:
        x=x-1
        y=y
        used.append([current])
        algo(matrix,x,y)
        return
    if (findcommondivisor(current,right)) == True and uright == 1:
        x=x
        y=y+1
        used.append([current])
        algo(matrix,x,y)
        return
    if (findcommondivisor(current,below)) == True and ubelow == 1:
        x=x+1
        y=y
        used.append([current])
        algo(matrix,x,y)
        return
    if (findcommondivisor(current,left)) == True:
        x=x
        y=y-1
        used.append([current])
        algo(matrix,x,y)
        return
    else:
        if (findcommondivisor(current, above)) == True:
            x = x - 1
            y = y
            used.append([current])
            algo(matrix, x, y)
            return
        if (findcommondivisor(current, right)) == True:
            x = x
            y = y + 1
            used.append([current])
            algo(matrix, x, y)
            return
        if (findcommondivisor(current, below)) == True:
            x = x + 1
            y = y
            used.append([current])
            algo(matrix, x, y)
            return
        if (findcommondivisor(current, left)) == True:
            x = x
            y = y - 1
            used.append([current])
            algo(matrix, x, y)
            return

def main():
    matrix = loadtext('et.txt','X','Y','1')
    print(matrix)
    algo(matrix,5,5)



if __name__ == "__main__":
    main()