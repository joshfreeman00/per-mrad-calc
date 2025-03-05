import tkinter as tk
from tkinter import filedialog, messagebox
import random
import math

def calculate_per():
    try:
        per_max = float(per_max_entry.get())
        per_min = float(per_min_entry.get())
        result = 10*(math.log10(per_max/per_min))
        data_listbox.insert(tk.END, f"PER: {result}")
        messagebox.showinfo("PER", f"PER: {result:.4f}")
    except ValueError:
        data_listbox.insert(tk.END, "Invalid input")

def calculate_insertion_loss():
    try:
        il_input = float(il_input_entry.get())
        il_output = float(il_output_entry.get())
        result = 10*(math.log10(il_input/il_output))
        data_listbox.insert(tk.END, f"Insertion Loss: {result}")
        messagebox.showinfo("Insertion Loss", f"Insertion Loss: {result:.4f}")
    except ValueError:
        data_listbox.insert(tk.END, "Invalid input")

def calculate_return_loss():
    try:
        rl_input = float(rl_input_entry.get())
        rl_output = float(rl_output_entry.get())
        result = 10*(math.log10(rl_output/rl_input))
        data_listbox.insert(tk.END, f"Return Loss: {result}")
        messagebox.showinfo("Return Loss", f"Return Loss: {result:.4f}")
    except ValueError:
        data_listbox.insert(tk.END, "Invalid input")

def calculate_mrad():
    try:
        x1 = float(x1_entry.get())
        y1 = float(y1_entry.get())
        x2 = float(x2_entry.get())
        y2 = float(y2_entry.get())
        distance_mm = float(distance_entry.get())

        sum_x = (x2 - x1) ** 2
        sum_y = (y2 - y1) ** 2
        radius = math.sqrt(sum_x + sum_y) / 2
        mrad = radius / distance_mm
        data_listbox.insert(tk.END, f"  x1 = {x1:.2f} μm, y1 = {y1:.2f} μm\n"
        f"  x2 = {x2:.2f} μm, y2 = {y2:.2f} μm\n"
        f"  mrad = {mrad:.4f}")
        messagebox.showinfo("mRad", f"mRad: {mrad:.4f}")
    except ValueError:
        data_listbox.insert(tk.END, "Invalid input")

def clear_data():
    data_listbox.delete(0, tk.END)
    messagebox.showinfo("Success", "Data cleared.")

# Create the main application window
root = tk.Tk()
root.title("Beam Data Collection App")
root.geometry("600x800")

# Create a frame for the calculations
data_frame = tk.Frame(root)
data_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=10)
data_listbox = tk.Listbox(data_frame, height=10, width=80)
data_listbox.pack(fill=tk.BOTH, expand=False)

# Frame for PER, IL and RL calculation
calc_frame = tk.Frame(root)
calc_frame.pack(pady=(10))

# Inputs for the PER calculation
tk.Label(calc_frame, text="Enter PER max (uW):").grid(row=0, column=0, padx=10)
per_max_entry = tk.Entry(calc_frame)
per_max_entry.grid(row=1, column=0, pady=5)

tk.Label(calc_frame, text="Enter PER min (uW):").grid(row=2, column=0, padx=10)
per_min_entry = tk.Entry(calc_frame)
per_min_entry.grid(row=3, column=0, pady=10)

# Button to calculate the PER
tk.Button(calc_frame, text="Calculate PER", command=calculate_per).grid(row=4, column=0, padx=10, pady=5)

# Inputs for the Insertion Loss calculation
tk.Label(calc_frame, text="Enter IL in (mW):").grid(row=0, column=1, padx=10)
il_input_entry = tk.Entry(calc_frame)
il_input_entry.grid(row=1, column=1, pady=5)

tk.Label(calc_frame, text="Enter IL out (mW):").grid(row=2, column=1, padx=10)
il_output_entry = tk.Entry(calc_frame)
il_output_entry.grid(row=3, column=1, padx=10)

# Button to calculate the Insertion Loss

tk.Button(calc_frame, text="Calculate IL", command=calculate_insertion_loss).grid(row=4, column=1, padx=10, pady=5)

#Inputs for the RL calculation
tk.Label(calc_frame, text="Enter RL in (mW):").grid(row=0, column=2, padx=10)
rl_input_entry = tk.Entry(calc_frame)
rl_input_entry.grid(row=1, column=2, padx=10)

tk.Label(calc_frame, text="Enter RL out (uW):").grid(row=2, column=2, padx=10)
rl_output_entry= tk.Entry(calc_frame)
rl_output_entry.grid(row=3, column=2, padx=10)

# Button to calculate the RL

tk.Button(calc_frame, text="Calculate RL", command=calculate_return_loss).grid(row=4, column=2, padx=10, pady=5)

# Frame for mRad calculation
mrad_frame = tk.Frame(root)
mrad_frame.pack(padx=10, pady=10)

## Inputs for the mRad calculation
tk.Label(mrad_frame, text="Enter x1 (μm):").grid(row=0, column=0, padx=5, pady=5)
x1_entry = tk.Entry(mrad_frame)
x1_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(mrad_frame, text="Enter y1 (μm):").grid(row=0, column=2, padx=5, pady=5)
y1_entry = tk.Entry(mrad_frame)
y1_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(mrad_frame, text="Enter x2 (μm):").grid(row=1, column=0, padx=5, pady=5)
x2_entry = tk.Entry(mrad_frame)
x2_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(mrad_frame, text="Enter y2 (μm):").grid(row=1, column=2, padx=5, pady=5)
y2_entry = tk.Entry(mrad_frame)
y2_entry.grid(row=1, column=3, padx=5, pady=5)
# Distance in millimeters
tk.Label(mrad_frame, text="Distance (mm):").grid(row=2, column=0, padx=5, pady=5)
distance_entry = tk.Entry(mrad_frame)
distance_entry.grid(row=2, column=1, padx=5, pady=5)

# Button to calculate the mRad

tk.Button(mrad_frame, text="Calculate mRad", command=calculate_mrad).grid(row=2, column=2, padx=5, pady=5)

# Buttons for clearing the data
tk.Button(root, text="Clear Data", command=clear_data).pack(pady=5)

root.mainloop()