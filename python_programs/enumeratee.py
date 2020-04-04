ss = ["ss","dd","ff","gg"]

i = 1
for item in ss:
	if i%2 is not 0:
		print(item)
	i += 1
		
for index, item in enumerate(ss):
	if index%2 == 0:
		print(item)		 
import sys
print(sys.path)