#Print a downward half-pyramid pattern of stars

def pyramid():
    num1 = 54321
    num1 = str(num1)
    length = len(num1)
    print(num1)
    print(len(num1))

    for i in range(length,1):
        print(*i*(num1[i]), sep=' ')

pyramid()