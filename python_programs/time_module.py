import time

initial_time = time.time()
print(initial_time)

def ff():
	for i in range(4):
		time.sleep(1)
		print("suresh")
ff()
time_taken = time.time() - initial_time
print(time_taken)

i = 0
while(i<2):
	print("yyyyy")
	i += 1

time_taken = time.time() - initial_time
print(time_taken)

local_time = time.asctime(time.localtime(time.time()))
print(local_time)