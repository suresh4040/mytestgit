#snake water gun
# 10 tims play vs computer
#choose snake or water or gun
#take input s or w or g
# snake > water ,water>gun , gun>snake

import random

i = 0
x = 0
y = 0
print("BEST OUT OF 5 TRIES")
while (i<5):
	choice_list = ["s","w","g"]
	comp = random.choice(choice_list)
	me = str(input("Enter ur choice : "))

	#my wins
	if me == "s" and comp == "w":
		x += 1
		print(f"comp choose : {comp}")
		print("u won")
	if me == "w" and comp =="g":
		x += 1
		print(f"comp choose : {comp}")
		print("u won")
	if me == "g" and comp == "s":
		x += 1
		print(f"comp choose : {comp}")
		print("u won")

	#comp wins
	if me == "w" and comp == "s":
		y += 1
		print(f"comp choose : {comp}")
		print("comp won")
	if me == "g" and comp =="w":
		y += 1
		print(f"comp choose : {comp}")
		print("comp won")
	if me == "s" and comp == "g":
		y += 1
		print(f"comp choose : {comp}")
		print("comp won")			
	i += 1
print()
print(f"Your number of wins {x}")
print(f"Comp number of wins {y}")

if x>y:
	print("You are the winner")
else:
	print("comp is the winner")	

print("Game over")	