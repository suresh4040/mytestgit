class A():
	var = "in a"
	def __init__(self):
		self.var1 = "I am in class A constr"
		self.var = "instance var A"  # overrided
		self.special = "spec A"

class B(A):
	var = "in b"		
	def __init__(self):
		
		super().__init__()	 # call init of A
		self.var1 = "I am in class B constr"
		self.var = "instance var B"  #
		# super().__init__() # if we use it in this line then after init of B , init of A will execute
		print(super().var)


a = A()
b = B()
print(b.var) # here class A init will nt execute if we dont use super bcoz init is overrided in B
print(b.special)