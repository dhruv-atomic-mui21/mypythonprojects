import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "User"
    else:
        return "Computer"

def play():
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "Tie":
            print("It's a tie!")
        elif winner == "User":
            print("You win!")
        else:
            print("Computer wins!")
        print()

if __name__ == "__main__":
    play()
