class Employee:
    '''This is the class example for self method '''
    
    def __init__(self,Ename,Eno,Eloc):
        self.Ename=Ename
        self.Eno=Eno
        self.Eloc=Eloc
    def info(self):
        print("Hello myself ",self.Ename)
        print("My Eno is ",self.Eno)
        print("I am from ",self.Eloc)


e1=Employee("Virat","100","Patna")
e2=Employee("Virat Singh","200","Bangalore")
e1.info()
print("---"*10)
e2.info()
print(Employee.__doc__)
# This .__doc__ method is used for the documentation written under tripple quotation 