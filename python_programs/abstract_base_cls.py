# class works like a base class 

#abc meta class
from abc import ABCMeta, abstractmethod

class shape(metaclass=ABCMeta):
	@abstractmethod  # means all have to define it (all classes )
	def area(self):   # so this area method must be defines in Rectangle class else it gives error
		return 0
 
class Rectangle(shape):
	type = "Rectangle"
	sides = 4
	def __init__(self):
		self.length = 6
		self.breadth = 7
	def area(self):          # its an abstarct method which must be defined
		return f" i am area"	
r = Rectangle()
print(r.area())

# above will raise error if  we dont define area method which is an abstarct method


 # if python > 3.4
 # then 
from abc import ABC

class shape(ABC):
 	@abstractmethod
 	def area(self):
 		return 0


class Rectangle(shape):
	type = "Rectangle"
	sides = 4
	def __init__(self):
		self.length = 6
		self.breadth = 7
	def area(self):          # its an abstarct method which must be defined
		return f" i am area"	
r = Rectangle()
print(r.area())


# op
# i am area
# i am area
