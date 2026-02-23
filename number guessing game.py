import random

print("=== Number Guessing Game ===")
print("1. Easy (1-50, 10 attempts)")
print("2. Medium (1-100, 7 attempts)")
print("3. Hard (1-200, 5 attempts)")

difficulty = input("\nChoose difficulty (1/2/3): ")

# set range and attempts based on difficulty
if difficulty == "1":
    lower_bound = 1
    upper_bound = 50
    max_tries = 10
elif difficulty == "2":
    lower_bound = 1
    upper_bound = 100
    max_tries = 7
elif difficulty == "3":
    lower_bound = 1
    upper_bound = 200
    max_tries = 5
else:
    print("Invalid choice, defaulting to Medium.")
    lower_bound = 1
    upper_bound = 100
    max_tries = 7

# computer picks a random number in the range
secret_number = random.randint(lower_bound, upper_bound)
attempts_used = 0
guessed_correctly = False

print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
print(f"You have {max_tries} attempts. Good luck!\n")

while attempts_used < max_tries:
    remaining = max_tries - attempts_used
    try:
        user_guess = int(input(f"Attempt {attempts_used + 1}/{max_tries} - Your guess: "))

        # make sure guess is within the valid range
        if user_guess < lower_bound or user_guess > upper_bound:
            print(f"Please guess between {lower_bound} and {upper_bound}!")
            continue

        attempts_used += 1

        if user_guess == secret_number:
            print(f"\nCORRECT! You got it in {attempts_used} attempt(s)!")
            guessed_correctly = True
            break
        elif user_guess < secret_number:
            print(f"Too LOW! Go higher. ({remaining - 1} attempts left)")
        else:
            print(f"Too HIGH! Go lower. ({remaining - 1} attempts left)")

    except ValueError:
        print("Please type a whole number!")

# show result at end
if not guessed_correctly:
    print(f"\nGame Over! The number was {secret_number}. Better luck next time!")

play_again = input("\nPlay again? (yes/no): ")
if play_again.lower() == "yes":
    exec(open(_file_).read())  # restart the game