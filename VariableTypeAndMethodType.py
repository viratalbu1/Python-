class Student:
    clgname="BKIT"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Hello my name is ",self.name)
        print("My Roll no is ",self.rollno)
    def Findaverage(self,x,y):
        print("Average is ",x+y/2)
  
    def PrintCollageName():
        print(clgname)
        
    
    
    
    
s1=Student("Virat",101)
s1.PrintCollageName()