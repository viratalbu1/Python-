# Lambda Function are Annonomus Function That mean function without name so we dont have
# to Explicitly define function for any call we can put in any variable declaration and use that declaration for
# further use
a=lambda x:x+1
print(a(2))

# Another Example Use Lambda function for finding celcius to far

faren=lambda x:1.8*x+32
print('This is the current temp in my city Patna 5C')
print('This is the converted temp of Patna ',faren(5),'F by using lambda')

# Another Varient for using Lambda when we have list
print('The temp for 5 days in c is [5,6,8,3,11]')
ll=[5,6,8,3,11]
print('This is the temp in F for 5 days ',list(map(faren,ll)))

# Another Varient for Lambda Function
two_number_val=lambda x,y:(x+y,x-y)
print(two_number_val(10,8))
# Lets Take ANother Example for Lambda
change_upperCase=lambda x:x.upper()
print(change_upperCase('virat'))


# map(func, *iterables) –> map object
# Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted

print(list(map(change_upperCase,['Virat','Singh','Map Reduce'])))

#Reduce Function
from functools import reduce
max_val=lambda x,y: x if (x>y) else y
print('Find Max value in list [31,98,77,65,102,309,222,213,510]')
print(reduce(max_val,[31,98,77,65,102,309,222,213,510]))