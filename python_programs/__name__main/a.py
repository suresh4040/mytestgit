def func1():
	return "f1"

def func2():
	return "f2"	




if __name__ == '__main__':
	s = func1()
	print(s)
	t = func2()
	print(t)

# Above main function will only execute when we call a.py , if we call b.py and we already import a function 
# func1
# in b.py ,, then only func1 will execute as we used main in a.py ,  else 1st a.py completly execute and then b.py	