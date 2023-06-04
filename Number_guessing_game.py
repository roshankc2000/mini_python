#number guessing game
import random
x = random.randrange(1,100)

print("Guess the number in 8 Chances : ")
live = 8
while live >=0 :
    guess = int(input("Enter a no :"))
    if guess != x :
        if x>guess :
            print("Please guess a higher number.")
        else :
            print("Please guess a number lower number.")
    else:
        print("Congratulations! You guessed it right.")
        break
    live-=1
if (live == 0) :
    print("life khatam! Game Over")