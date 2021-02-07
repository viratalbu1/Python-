def GCDNaive(a,b):
    if a==0:
        return 0
    elif b==0:
        return 0
    else:
        result=min(a,b)
        while result>0:
            if a%result==0 and b%result==0:
                break
            result=result-1
    return result

def EculidainMethod(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a






def OptimizedEculidain(a,b):
    if b==0:
        return a
    else:
        return OptimizedEculidain(b,a%b)



if __name__=='__main__':
    print('This is the Naive Approach for finding GCD of two no \n',GCDNaive(10,0))
    print('This is the Eculidian Approach Approach for finding GCD of two no \n', EculidainMethod(10, 2))
    print('This is the Eculidian Approach Approach for finding GCD of two no \n', OptimizedEculidain(10, 5))