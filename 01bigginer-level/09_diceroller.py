import random

def roll_dice(num_dice=1, num_sides=6):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls

def main():
    print("Dice Roller")
    try:
        num_sides = 6
        num_dice = int(input("Enter number of dice to roll: "))
        if num_dice < 1 :
            print("Number of dice must be at least 1")
            return
    except ValueError:
        print("Please enter valid integers.")
        return

    rolls = roll_dice(num_dice, num_sides)
    print(f"Rolls: {rolls}")
    print(f"Total: {sum(rolls)}")

if __name__ == "__main__":
    main()
