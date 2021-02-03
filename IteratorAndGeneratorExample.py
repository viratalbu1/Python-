# Iterator is used for creating object for iteratable object such as string, list , tuple
itr_list=iter([1,2,3,4])
itr_tuple=iter((1,2,3,4))
itr_string=iter('String')

print('--------List ------')
for val in itr_list:
    print(val)
print('-----Tuple----------')
for val in itr_tuple:
    print(val)
print('------String---------')
for val in itr_string:
    print(val)



print('Genertor Examples')

def GetCubes(a):
    for num in range(a):
        yield num**3

print(GetCubes(5))
print('This is Object so now we can call this object and get the result')
for val in GetCubes(5):
    print(val)
print('Other Varient for Using Generator')

print(list(GetCubes(2)))
