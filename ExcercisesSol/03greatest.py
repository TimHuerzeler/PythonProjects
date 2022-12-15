def greatest(lst):
    """Returns the greatest element of a list of positive integers"""
    great = 0
    for i in lst:
        if i > int(great):
            great = i
    return great

def main():
    """ Launcher """
    lst = [4, 7, 8, 2, 5]
    print('The greatest element is {}.'.format(greatest(lst)))
    
if __name__ == "__main__":
    main()
