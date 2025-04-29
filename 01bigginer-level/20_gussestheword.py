import random

def guess_the_word():
    words = ['python', 'programming', 'challenge', 'computer', 'science', 'openai']
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    word_letters = set(word)

    print("Welcome to Guess the Word!")
    print("Try to guess the word by guessing one letter at a time.")

    while attempts > 0 and word_letters:
        display_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word: " + ' '.join(display_word))
        print(f"Attempts left: {attempts}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("Good guess!")
        else:
            attempts -= 1
            guessed_letters.add(guess)
            print("Wrong guess.")

        print()

    if not word_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    guess_the_word()
