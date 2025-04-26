import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-10)") 
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")
    print("4. Custom (1-1000)")
    print("5. Cheat mode (reveal the number)")
    print("6. Exit")

    difficulty = input("Enter your choice (1-6): ")

    if difficulty == '1':
        number_to_guess = random.randint(1, 10)
        max_attempts = 5
    elif difficulty == '2':
        number_to_guess = random.randint(1, 50)
        max_attempts = 9
    elif difficulty == '3':
        number_to_guess = random.randint(1, 100)
        max_attempts = 10
    elif difficulty == '4':
        number_to_guess = random.randint(1, 1000)
        max_attempts = 15
    elif difficulty == '5':
        number_to_guess = random.randint(1, 1000)
        print(f"Cheat mode activated! The number is {number_to_guess}.")
        return  
    elif difficulty == '6':
        print("Thanks for playing!")
        return
    else:
        print("Invalid choice. Please try again.")
        return

    attempts = 0
    print(f"You have {max_attempts} attempts to guess the number between 1 and {number_to_guess}.")

    score = 0

    
    while attempts < max_attempts:
        user_guess = input("Enter your guess (or 'exit' to quit): ")
        if user_guess.lower() == 'exit':
            print("Thanks for playing!")
            break

       
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

       
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            score = max_attempts - attempts + 1
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts! 🎉")
            print(f"Your score is: {score}")
            break
    else:
        print(f"Game Over! You have used all {max_attempts} attempts. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    number_guessing_game()
