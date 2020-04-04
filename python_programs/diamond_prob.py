								 # A

							# B	      # C

								 # D
						
class A():
	pass

class B(A):
	def met(self):
		print("hh")

class C(A):
	def met(self):
		print("okok")		

class D(C, B):
	pass	

a = A()	
b = B()
c = C()
d = D()

d.met()

# Thats why most of the time its advisable to avoid multiple inheritance as it creates confusion.