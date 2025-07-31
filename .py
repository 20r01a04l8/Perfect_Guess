import random

# For selecting choices
def select_choices():
    print("Enter the choice: ")
    print("Easy level: (1-20)")
    print("Medium level: (21-100)")
    print("Hard level: (100-500)")
    while True:
        choice = input("Enter your choice: ")
        try:
            if choice=="1":
                return 1,20
            elif choice=="2":
                return 21,100
            elif choice=="3":
                return 100,500
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid value or choice. Please enter 1, 2 or 3.")

#Function for playing game
def play_game():
    low,high = select_choices()
    number_to_guess = random.randint(low,high)
    attempt=0
    print(f"Ok! I'm thinking of a number between {low} and {high}.")
    print("You have to guess it. After each guess, I'll tell you if your guess was too high or too low.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempt+=1
            if guess < low or guess > high:
                print("Please enter a number between",low,"and",high,".")
            elif guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number correctly in ",attempt,"attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main Function
def main():
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        main()

if __name__ == "__main__":
    main()
