import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attampts=0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        user_guess = input("Enter your guess (or 'exit' to quit): ")
        if user_guess.lower() == 'exit':
            print("Thanks for playing!")
            break
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        attampts+=1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attampts} attempts.")
            break

        
if __name__ == "__main__":
    number_guessing_game()