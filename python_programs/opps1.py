class college():
	xx = 2
	def cmeth(self):
		return f"suresh age is {self.age}"
	def nmeth(self):
		return f"nitesh age is {self.age}"	 

suresh = college()
nitesh = college()

suresh.age = 25
nitesh.age = 24

print(suresh.cmeth())
print(nitesh.nmeth())
print(suresh.xx)  #2
suresh.xx = 3
print(suresh.xx)  #3
print(college.xx) #2

# constructor
# class d():
	# pass
# suresh = d("name","age")	#not possible to pass arguments
# give arguments to a class -----------
class college():
	def __init__(self, aname,aage): # self = sureshobj
		self.name = aname
		self.age = aage


sureshobj = college("suresh",25)	 # these aruguments are gonig to init 
print(sureshobj.name, sureshobj.age)

#class method

class college():
	leave = 10

	def __init__(self):
		pass

	def d(self):
		pass

	@classmethod
	def cmeth(cls, leave):
		cls.leave = leave

suresh = college()			
college.cmeth(20)
suresh.cmeth(20)
print(college.leave)
print(suresh.leave)