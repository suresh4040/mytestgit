n = ["1","2"]
for item in range(len(n)):
	n[item] = int(n[item])
print(n)
s = list(map(int,n)) # convert map object to list
print(s)
# map takes a function and list as argument.
#

def sq(a):
	return a*a
ll = [2,3,4]
d = list(map(sq,ll))
print(d)
e = list(map(lambda a:a*a, ll))
print(e)

def add(a):
	return a+a

def mult(a):
	return a*a

ll = [add,mult]
for i in range(4):
	ww = list(map(lambda a:a(i),ll))
	print(ww)		
#----------------------------------------------------------------------------------------------------
#Filter

def fil(n):
	return n>3

L = [1,2,3,4,5]
fff = list(filter(fil, L))
print(fff)
#--------------------------------------------------------------------------------
#reduce
oo = [1,2,3]
i = 0
for each in oo:
	i = i +each
print(i)

# using reduce
from functools import reduce
num = reduce(lambda x,y:x+y,oo)
print(num)


