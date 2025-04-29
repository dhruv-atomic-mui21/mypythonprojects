import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_rates():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return data['rates']
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve exchange rates.")
        return None

def convert():
    rates = get_rates()
    if rates is None:
        return
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()
        if from_currency not in rates or to_currency not in rates:
            messagebox.showerror("Error", "Invalid currency selected.")
            return
        converted_amount = amount / rates[from_currency] * rates[to_currency]
        label_result.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

root = tk.Tk()
root.title("Currency Converter")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Amount:").grid(row=0, column=0, sticky=tk.W)
entry_amount = tk.Entry(frame)
entry_amount.grid(row=0, column=1)

tk.Label(frame, text="From:").grid(row=1, column=0, sticky=tk.W)
combo_from = ttk.Combobox(frame, values=[])
combo_from.grid(row=1, column=1)

tk.Label(frame, text="To:").grid(row=2, column=0, sticky=tk.W)
combo_to = ttk.Combobox(frame, values=[])
combo_to.grid(row=2, column=1)

button_convert = tk.Button(frame, text="Convert", command=convert)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="", font=('Arial', 14))
label_result.pack(pady=10)

def populate_currencies():
    rates = get_rates()
    if rates:
        currencies = sorted(rates.keys())
        combo_from['values'] = currencies
        combo_to['values'] = currencies
        combo_from.set('USD')
        combo_to.set('EUR')

populate_currencies()

root.mainloop()
