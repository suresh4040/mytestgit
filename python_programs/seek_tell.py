f = open("t.txt","r+")
print(f.tell()) # shows file pointer
print(f.readline()) #
print(f.tell()) #
print(f.seek(0)) # takes the file pointer to 0th position
print(f.readline())
print(f.seek(2)) # takes to 2nd position & read
print(f.readline())
f.close()
# op:
# 0
# my name is:
# 11
# 0
# my name is:
# 2
#  name is: