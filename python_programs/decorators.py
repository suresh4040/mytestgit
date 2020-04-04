# modifies function's functionality

# def fun(fun1):
# 	fun1()
# 	fun1("yyyy")

# fun(print)

def ff(fun2):
	def fun3():
		print("Hi")	
		fun2()
		print("bye")
	return fun3

def dec1():
	print("hhhh")

ss = ff(dec1)			
ss()

#lets use ff as decorator now
@ff
def dec2():
	print("gg")
dec2()
