import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def toggle_done(event):
    selected_index = listbox_tasks.curselection()
    if not selected_index:
        return
    index = selected_index[0]
    task_text = listbox_tasks.get(index)
    if task_text.startswith("✔️ "):
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, task_text[2:])
    else:
        listbox_tasks.delete(index)
        listbox_tasks.insert(index, "✔️ " + task_text)
    listbox_tasks.selection_set(index)

root = tk.Tk()
root.title("Interactive To-Do List")

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

entry_task = tk.Entry(frame_top, width=40)
entry_task.pack(side=tk.LEFT, padx=(0,10))

button_add = tk.Button(frame_top, text="Add Task", width=10, command=add_task)
button_add.pack(side=tk.LEFT)

# Frame for Listbox + Scrollbar
frame_list = tk.Frame(root)
frame_list.pack()

listbox_tasks = tk.Listbox(frame_list, width=50, height=15, selectmode=tk.SINGLE)
listbox_tasks.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

button_delete = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
button_delete.pack(pady=(0,10))

listbox_tasks.bind('<Double-Button-1>', toggle_done)

root.mainloop()
