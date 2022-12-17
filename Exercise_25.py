# Develop a small program that reads the following text file:
#     et.txt
# 92 78 39 38 95 19 57 72
# 90 61 26 51 78 41 82 27
# 99  9  X 17 87 40 42 12
# 20 62 31 33 54  5 74 75
# 34 35 77 11 25 10 37 81
# 85 91 45 18 43  Y 15 36
# 93 13 65 63 21 49 60 58
# 84 69 66 70 55 30 24 29
# and stores the information into a list of lists of integers.
# Transform the strings "X" and "Y" into the integer value 1.

#Author: TimHuerzeler
#Date: 06.10.2022

import numpy as np

def loadtext(textfile,search_txt1,search_txt2,replace_txt):
    with open(textfile, 'r') as infile, open('et_temp.txt', 'w') as outfile:
        data = infile.read()
        data = data.replace(search_txt1, replace_txt)
        data = data.replace(search_txt2, replace_txt)
        outfile.write(data)
    matrix = np.loadtxt('et1.txt', usecols=range(8))
    return matrix
def main():
    matrix = loadtext('et.txt','X','Y','1')
    print(matrix)


if __name__ == "__main__":
    main()