# public
# private - only and only own class can access 
# protected  - its own class and its subclasses can access it but other classes cant
class Emp():
	pub = 2
	_prot = 3 # protected 
	__priv = 4

d = Emp()	
print(d._prot) #3
# print(d.__priv) #error , cant access private var like this

print(d._Emp__priv) # can access like this , called name mangelling

# _class__private_var

