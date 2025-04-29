import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    """
    A simple number guessing game with a GUI.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 10

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.root, text="Guess the number between 1 and 100:")
        self.instruction_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, width=20)
        self.guess_entry.pack(pady=5)
        self.guess_entry.focus()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="")
        self.feedback_label.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

    def check_guess(self):
        guess_text = self.guess_entry.get().strip()
        if not guess_text.isdigit():
            messagebox.showwarning("Invalid input", "Please enter a valid integer.")
            return

        guess = int(guess_text)
        if guess < 1 or guess > 100:
            messagebox.showwarning("Out of range", "Please guess a number between 1 and 100.")
            return

        self.attempts += 1

        if guess < self.number:
            self.feedback_label.config(text="Too low!")
        elif guess > self.number:
            self.feedback_label.config(text="Too high!")
        else:
            self.feedback_label.config(text=f"Correct! You guessed it in {self.attempts} attempts.")
            self.end_game()
            return

        if self.attempts == self.max_attempts - 1:
            self.feedback_label.config(text="Concentrate! This is your last attempt.")
        elif self.attempts >= self.max_attempts:
            self.feedback_label.config(text=f"Too many attempts! The number was {self.number}.")
            self.end_game()

        self.guess_entry.delete(0, tk.END)

    def end_game(self):
        self.guess_button.config(state=tk.DISABLED)
        self.guess_entry.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.reset_button.config(state=tk.DISABLED)
        self.guess_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
