
class Test:
	def __init__(self):
		self.a=10
		self.b=20
		self.c=40
	def delete(self):
		del self.b
		del self.c

t1=Test()
t1.delete()
del t1.a
print(t1.__dict__)
