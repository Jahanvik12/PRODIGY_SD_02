import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 0 and 1000.")

    secret_number = random.randint(0, 1000)

    attempts = 0

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number", secret_number , "in" , attempts, "attempts.")
            break

guess_the_number()
