import tkinter as tk

class FlashcardQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")

        self.flashcards = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "What is 2 + 2?", "answer": "4"},
            {"question": "What is the largest planet?", "answer": "Jupiter"},
            {"question": "Who wrote 'Hamlet'?", "answer": "William Shakespeare"},
        ]
        self.current_index = 0

        self.question_label = tk.Label(root, text="", font=('Arial', 18), wraplength=400)
        self.question_label.pack(pady=20)

        self.answer_label = tk.Label(root, text="", font=('Arial', 16), fg="blue", wraplength=400)
        self.answer_label.pack(pady=10)

        self.show_answer_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_button.pack(pady=5)

        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)

        self.prev_button = tk.Button(nav_frame, text="Previous", command=self.prev_flashcard)
        self.prev_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(nav_frame, text="Next", command=self.next_flashcard)
        self.next_button.grid(row=0, column=1, padx=10)

        self.update_flashcard()

    def update_flashcard(self):
        self.answer_label.config(text="")
        question = self.flashcards[self.current_index]["question"]
        self.question_label.config(text=question)

    def show_answer(self):
        answer = self.flashcards[self.current_index]["answer"]
        self.answer_label.config(text=answer)

    def next_flashcard(self):
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            self.update_flashcard()

    def prev_flashcard(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_flashcard()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardQuizApp(root)
    root.mainloop()
