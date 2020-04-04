#lamda or anonymous function

def lm(a,b):
	return a+b

print(lm(2,3))

xx = lambda a,b:a+b

print(xx(1,2))

def func(a):
	return a[0]

a = [[5,6],[3,4]]
a.sort(key=func)
print(a)

a = [[5,6],[3,4]]
a.sort(key=lambda a:a[0])  # key is argument takes a function
print(a)