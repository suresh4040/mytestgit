# operator overloading
# go through operator documentations - mapping operators to function 
class college():
	def __init__(self,aname,price):
		self.name = aname
		self.price = price

	def anyfunc(self):
		return f"I am just a test function"\

	@staticmethod
	def statmeth():
		return f"i am static"

	@classmethod
	def clsmeth(cls,other):
		cls.age = other
		return cls.age

	def __add__(self,second):  # operator overloading
		return self.price + second.price 	

	def __truediv__(self,other):
		return self.price / other.price	

	def __repr__(self):
		return f"i am repr"	    # repr will be 2nd preference if str method is declared , __str__ ,  both run when we call just object of class

	def __str__(self):
		return f"i am self string"
	def __mod__(self,other):
		return self.price | self.price		  

	def __or__(self,other):
		return self.price | other.price	
o = college("suresh",50)
# print(o.anyfunc())    # i am just a test function
# print(o.statmeth())   # i am static
# print(o.clsmeth(25))  # 25
p = college("nitesh",60)

print(o + p)  # operator overloading  110
print(o / p)  # 0.8333
print(o)      # executes str method =  i am self string
print(o % p)  #
print(o | p)