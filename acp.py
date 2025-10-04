import tkinter as tk
from tkinter import messagebox
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * ((1 + rate / 100) ** time) - principal
        simple_result.config(text=f"Simple Interest: ${simple_interest:.2f}")
        compound_result.config(text=f"Compound Interest: ${compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
window = tk.Tk()
window.title("Interest Calculator")
window.geometry("300x250")
tk.Label(window, text="Principal Amount ($):").pack(pady=5)
principal_entry = tk.Entry(window)
principal_entry.pack(pady=5)
tk.Label(window, text="Time Period (years):").pack(pady=5)
time_entry = tk.Entry(window)
time_entry.pack(pady=5)
tk.Label(window, text="Rate of Interest (%):").pack(pady=5)
rate_entry = tk.Entry(window)
rate_entry.pack(pady=5)
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.pack(pady=10)
simple_result = tk.Label(window, text="Simple Interest: $0.00")
simple_result.pack(pady=5)
compound_result = tk.Label(window, text="Compound Interest: $0.00")
compound_result.pack(pady=5)
window.mainloop()
