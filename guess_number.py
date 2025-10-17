import random

number = random.randint(1, 20)
tries = 0

print("Welcome to Guess the Number Game!")
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    tries += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {tries} tries.")
        break
