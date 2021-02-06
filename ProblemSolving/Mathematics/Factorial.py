def FindFactorial1(n):
# factorial for n is n*n-1*n-2*....1
    fact=1
    if n==0:
        return 1
    else:
        while(n>0):
            fact=n*fact
            n=n-1
        return fact
def FindFactorial2(n):
    if n==0:
        return 1
    else:
        return n*FindFactorial2(n-1)

def FindFactorial3(n):
    fact = 1
    start=0
    if n==0:
        fact = 1
    else:
        while(start<=n):
            yield fact
            start=start+1
            fact=fact*start


if __name__=='__main__':
    print('One way to find Factorial')
    print('Factorial value = ',FindFactorial1(3))
    print('Method No 2 for Finding Factorial')
    print('Factorail value',FindFactorial2(4))
    print('Finding FactorialUsing Lambda')
    fact=lambda x:1 if x==0 else x*fact(x-1)
    print('Factorial Value = ',fact(5))
    print('Factorial Using Generator')
    a=FindFactorial3(5)
    print('The Factorial value ',list(a)[-1])
    print('Find the Factorial for list of values [1,2,4,6,7]')
    print('Using map Function for finding factorial')
    print('The Factorial values are ',list(map(FindFactorial2,[1,2,4,6,7])))
    print('Find Factorial values using lambda list')
    print('The Factorial Values are ',list(map(fact,[1,2,4,6,7])))
