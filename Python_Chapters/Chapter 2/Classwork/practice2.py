# Guessing Game
import random


def guessing_game():
    number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(
                    f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                print("Thank you for playing the Guessing Game!")
                play_again = input(
                    "Do you want to play again? (yes/no): ").strip().lower()
                if play_again == 'yes':
                    guessing_game()
                else:
                    print("Goodbye!")
        except ValueError:
            print("Invalid input. Please enter a number.")


guessing_game()
