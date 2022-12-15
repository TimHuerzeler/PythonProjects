from functools import reduce

def mul(x, y):
    return x * y

def main():
    lst = [2, 4, 7, 3]

    # with function
    print(reduce(mul, lst))
          
    # with lambda
    print(reduce(lambda x, y: x * y, lst))

if __name__ == "__main__":
    main()

