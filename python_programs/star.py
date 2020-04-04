r = int(input("Enter no of rows"))
ss = int(input(" type 1 for pyramid or 0 for reverse"))
ty = bool(ss)
if ty == True:
	for i in range(0,r):
		for j in range(i+1):
			print("*", end="")
		print("\n")
elif ty == False:
	for i in range(0,r):
		for j in range(r-i):
			print("*", end="")
		print("\n")