import random

secret_number = random.randint(1, 100)
attempts = 0

print("welcome to my first game")

while True:
    guess = int(input("guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("too low! try again.")
    elif guess > secret_number:
        print("too high! try again.")
    else:
        print(f"congratulations! you've guessed the number {secret_number} in {attempts} attempts.")
        play_again = input("do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            secret_number = random.randint(1, 100)
            attempts = 0
            print("new game started! guess a number between 1 and 100.")
        else:
            print("thanks for playing! goodbye.")
            break
