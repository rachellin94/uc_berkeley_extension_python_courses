# high-low.py: a simple guess the number game
import random

secret = random.randint(1, 501)
count = 0
name=input("Please enter your name.")
print(f"Hi,{name}!")

while True: 
    count += 1
    guess = input(f"Guess #{count} Enter your guess (1-500) or type 'quit' to exit: ")
    if guess == 'quit':
        break
    if int(guess) == secret:
        print(f"{name}! Correct! That's the right number.")
        break
    elif int(guess) < secret:
        print(f"{name}! Your guess is too low.")
    elif int(guess) > secret:
        print(f"{name}! Your guess is too high.")
    

    if abs(secret - int(guess)) <= 10:
        print("You are getting close")

print("game over")

