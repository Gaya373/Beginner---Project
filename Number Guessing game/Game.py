import random
import math

lower = int(input("Enter lower value:"))
upper = int(input("Enter upper value:"))
Game = random.randint(lower,upper)
print("you've only",round(math.log(upper-lower+1,2)),"chances to guess the number")

count = 0
while count < round(math.log(upper-lower+1,2)):
    count=count+1
    guess=int(input("Guess the Number :"))
    if Game == guess:
        print("Congratulations you did it in",count,"try")
        break
    elif Game > guess:
        print("your guessed too small !")
    elif Game < guess:
        print("your guessed too high !")
if count >= round(math.log(upper-lower+1,2)):
    print("The Number is %d" % Game)
    print("Better luck next time")

    

