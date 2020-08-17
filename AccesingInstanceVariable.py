#This Example is used for understanding what is instance variable 
class test:
	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
	def info(self):
		print(self.name)
		print(self.rollno)

#In Above Example state creation of constructor and object method 
# For Accessing it just create Object 
t=test("Virat",1)
t.info() #This method will print the value of instance variable 
print(t.name)
#above and below method will also give yo the instance variable value 
print(t.rollno) 