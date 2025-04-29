def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself at a crossroads in a dark forest.")
    print("Do you want to go left or right?")

    choice1 = input("Enter 'left' or 'right': ").lower()

    if choice1 == "left":
        print("You walk left and encounter a wild river.")
        print("Do you want to swim across or walk along the river?")
        choice2 = input("Enter 'swim' or 'walk': ").lower()

        if choice2 == "swim":
            print("You try to swim but the current is too strong. You drown.")
            print("Game Over.")
        elif choice2 == "walk":
            print("You walk along the river and find a bridge to cross safely.")
            print("You win!")
        else:
            print("Invalid choice. Game Over.")
    elif choice1 == "right":
        print("You walk right and find a sleeping dragon.")
        print("Do you want to sneak past or attack the dragon?")
        choice2 = input("Enter 'sneak' or 'attack': ").lower()

        if choice2 == "sneak":
            print("You sneak past the dragon successfully and escape the forest.")
            print("You win!")
        elif choice2 == "attack":
            print("The dragon wakes up and burns you to ashes.")
            print("Game Over.")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid choice. Game Over.")

if __name__ == "__main__":
    start_game()
