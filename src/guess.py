import random

MAX_ATTEMPTS = 10

while True:

    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have chosen a number between 1 and 100.")

    while True:

        guess_input = input("Your guess: ")

        # Validate input
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        # Hint logic
        if guess < secret_number:
            print("Too small.")
        elif guess > secret_number:
            print("Too big.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

        # Check attempt limit
        if attempts >= MAX_ATTEMPTS:
            print(f"You ran out of attempts. The number was {secret_number}.")
            break

    # Ask to play again
    play_again = input("Play again? (y/n): ").lower()

    if play_again != "y":
        print("Thanks for playing!")
        break