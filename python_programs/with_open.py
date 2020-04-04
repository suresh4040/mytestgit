with open("t.txt") as f:
    a = f.read(3)
    print(a)
# here no need to close file as with will handle it
f = open("t.txt")
s = f.read()
print(s)
f.close()
