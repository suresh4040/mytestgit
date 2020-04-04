class a():
	x = 20
	

obj1 = a() #create object

obj2 = a() #2nd object

obj1.name = "suresh"

print(a) #class
print(a()) #object
print(obj1.name)  #suresh
print(a.x)
obj1.x = 30
print(a.x)  #20
print(obj1.x)  # 30
print(obj1.__dict__)  # using dict attribute , {"name":"suresh","x":30}