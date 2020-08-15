class Student:
	'''This class developed by virat for demo purpose'''
	def __init__(self,rollno,name):
			self.rollno=rollno
			self.name=name
	def talk(self):
		print("Hello My name is ",self.name)
		print("My rollno is ",self.rollno)
s=Student(100,"Virat")
s.talk()
s1=Student(200,"Ritu")
s1.talk()