def NaiveLCM(a,b):
    result=max(a,b)
    while True:
        if result%a==0 and result%b==0:
            return result
        result=result+1
    return result
def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)
def OptimalLCM(a,b):
    HCF=GCD(a,b)
    return a*b/HCF

if __name__=='__main__':
    print('The LCM is :',NaiveLCM(10,2))
    print('The Optimal Solution of LCM is :', OptimalLCM(10, 2))