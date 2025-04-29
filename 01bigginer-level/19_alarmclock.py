import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    threading.Thread(target=alarm_thread, args=(alarm_time,), daemon=True).start()

def alarm_thread(alarm_time):
    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            messagebox.showinfo("Alarm", "Time's up!")
            break
        time.sleep(1)

root = tk.Tk()
root.title("Alarm Clock")

tk.Label(root, text="Set Alarm (24-hour format)").grid(row=0, columnspan=3)

hour = tk.StringVar(root)
minute = tk.StringVar(root)
second = tk.StringVar(root)

hour_entry = tk.Entry(root, textvariable=hour, width=3)
hour_entry.grid(row=1, column=0)
minute_entry = tk.Entry(root, textvariable=minute, width=3)
minute_entry.grid(row=1, column=1)
second_entry = tk.Entry(root, textvariable=second, width=3)
second_entry.grid(row=1, column=2)

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.grid(row=2, columnspan=3, pady=10)

root.mainloop()
