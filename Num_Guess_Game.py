import random

def guess_the_number():

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    guess_count = 0

    print("This is a Number Guessing Game-\n\n")

    while True:
        guess = int(input("Guess the Secret Number(1-100): "))

        if guess == secret_number:
            guess_count += 1
            print(f"Congratulations! You guessed the number in {guess_count} attempts and the secret number is {guess}.")
            break
        elif guess < secret_number:
            print("The number you guess is less than the secret number. Try Again!")
        else:
            print("The number you guess is higher than the secret number. Try Again!")

        guess_count += 1


guess_the_number()