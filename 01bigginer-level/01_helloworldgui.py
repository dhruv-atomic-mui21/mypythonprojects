import tkinter as tk
from tkinter import messagebox

class HelloWorldGUI:
    """
    A simple GUI application that greets the user.
    """

    def __init__(self, root):
        """
        Initialize the GUI components.
        """
        self.root = root
        self.root.title("Hello World GUI")

        # Create a menu bar with an Exit option
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Create a frame for better layout
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        # Label widget
        self.label = tk.Label(self.frame, text="Enter your name:")
        self.label.grid(row=0, column=0, sticky="w")

        # Entry widget for user input
        self.name_entry = tk.Entry(self.frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=10)

        # Button widget to trigger greeting
        self.greet_button = tk.Button(self.frame, text="Greet Me", command=self.show_greeting)
        self.greet_button.grid(row=1, column=0, columnspan=2, pady=10)

    def show_greeting(self):
        """
        Show a personalized greeting message.
        """
        name = self.name_entry.get().strip()
        if name:
            messagebox.showinfo("Greeting", f"Hello, {name}!")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HelloWorldGUI(root)
    root.mainloop()
