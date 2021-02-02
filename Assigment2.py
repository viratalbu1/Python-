def TrinaglePattern(height):
    for i in range(height):
        for j in range(i):
            print('*',end='')
        print()
    for i in range(height,-1,-1):
        for j in range(i):
            print('*',end='')
        print()
def ReverseString(str):
    return str[::-1]
if __name__=='__main__':
    # Question 1
    TrinaglePattern(5)
    # Question 2
    print(ReverseString('ineuron'))