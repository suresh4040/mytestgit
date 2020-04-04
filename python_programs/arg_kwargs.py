def funcargs(*args):
	print(args[0])

lstss = ["me", "you","them"]

funcargs(*lstss)   # * means send sll the elements of lstss to function as arguments
				   # it will go as tuples always

def ff(*manyy):
	print(manyy[1])
	print(manyy[2])

	for each in manyy:
		print(each)

ll = ["1","2",3]
ff(*ll)

def mm(normal,*args):
	print(normal)
	print(args)

yo = [55,66,77]
mm("normal me", *yo)	

# as rule of thumb normal should be 1st argument, then *args & then **kwargs

def kwwarr(normal,*args,**kwargs):
	print(normal)
	print(args)
	print(kwargs)
	for each in kwargs:
		print(each)      # print only key
	for key, value in kwargs.items():
		print(key,value)	 
normal = "suresh"
aa = [99,88,77,66]
dic = {"sdf":1, "fddd":2}
kwwarr(normal, *aa,**dic)