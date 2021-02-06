def CountTrailingZeros(n):
    count=0
    for i in range(5,n+1,5):
        count=int(n/i)+count
    return count


if __name__=='__main__':
    print('Provide the factorial no that you want to count the trailing zeros')
    fact=int(input())
    count=CountTrailingZeros(fact)
    print('The no of zero in ',fact,'! is ',count)