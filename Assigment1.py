import math
def Get_DivisiblyBy7AndNotMutipleOf5(val):
    if val%7==0 and val%5!=0:
        return True
    else:
        return False
def ReverseString(name):
    return name[::-1]
def VolumeOfSpehere(diameter):
    return (4/3)*math.pi*(diameter/2)**2
if __name__ == "__main__":
    ## Question 1
    for val in range(2000,3000):
        if Get_DivisiblyBy7AndNotMutipleOf5(val):
            print(val)
        else:
            pass

    ## Question 2
    # Input User for First Name
    name=input().split()
    print(ReverseString(name[0]),ReverseString(name[1]))

    ## Question 3
    print(VolumeOfSpehere(12))


