x = 10
i = 5
while(True):
    y = int(input("guess a number , Max 5 guesses:\n"))
    i = i - 1
    print("guesses left: "+ str(i))
    if i == 0:
        print("You have reached ur max guesses!",  i+5 )
        print("Game over")
        break
    if y<10:
        print("less")
    else:
        print("good")
        break
