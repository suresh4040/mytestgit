# class method alternative constructor

class college():
	x = 10
	def __init__(self,aname,aage):
		self.name = aname
		self.age = aage

	def meth1():
		pass

	#define a class method
	@classmethod
	def cmeth(cls,val):
		# param = val.split("-")
		# cls.x = val
		# return cls(param[0],param[1])
		return cls(*val.split("-"))

suresh = college("suresh",22)
# suresh.cmeth(20)
print(suresh.x)
nitesh = college.cmeth("nitesh-23")
print(nitesh.name)
print(nitesh.age)


