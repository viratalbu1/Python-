import  math
def isPrime(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
def OptimizedPrimeCheck(a):
    if a==1:
        return False
    for i in range(2,int(math.sqrt(a))):
        if a%i==0:
            return False
    return True
if __name__=='__main__':
    print('Checking prime for time complexity O(n)',isPrime(5))
    print('Checking prime for time complexity O(root n)', OptimizedPrimeCheck(5))