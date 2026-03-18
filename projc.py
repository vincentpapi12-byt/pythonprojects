
import math
import random
#For the number guessing game, think in steps:
#Generate a random number
#Ask user for input
#Compare guess to number
#Give feedback (too high / too low)
#Loop until correct


import random

number = random.randint(1, 200)

tries=0
while True:
 try: 
     
    guess = int(input("Guess the number: "))
    tries+=1
    if guess == number:
       # print("THE GUESS IS CORRECT!")
        print(f"Correct! The number was {number}")
        print(f"Tries={tries}")
        break
    elif guess > number:
        print("Too high, try again.")
    elif guess < number:
        print("Too low, try again.")
        
 except ValueError:
     print("That is not a valid number ,Please enter integer")