import tkinter as tk
from tkinter import filedialog, messagebox
import random
import math

def calculate_per():
    try:
        per_max = float(entry1.get())
        per_min = float(entry2.get())
        result = 10*(math.log10(per_max/per_min))
        data_listbox.insert(tk.END, f"PER: {result}")
        messagebox.showinfo("PER", f"PER: {result:.4f}")
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
root.geometry("800x800")

# Create a frame for the PER and mRad calculations
data_frame = tk.Frame(root)
data_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
data_listbox = tk.Listbox(data_frame, height=10, width=80)
data_listbox.pack(fill=tk.BOTH, expand=True)

# Inputs for the PER calculation
tk.Label(root, text="Enter PER max (uW):").pack(pady=(10, 0))
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter PER min (uW):").pack(pady=(10, 0))
entry2 = tk.Entry(root)
entry2.pack(pady=5)
# Button to calculate the PER
tk.Button(root, text="Calculate PER", command=calculate_per).pack(pady=10)

## Inputs for the mRad calculation
tk.Label(root, text="Enter x1 (μm):").pack(pady=(10, 0))
x1_entry = tk.Entry(root)
x1_entry.pack(pady=5)

tk.Label(root, text="Enter y1 (μm):").pack(pady=(10, 0))
y1_entry = tk.Entry(root)
y1_entry.pack(pady=5)

tk.Label(root, text="Enter x2 (μm):").pack(pady=(10, 0))
x2_entry = tk.Entry(root)
x2_entry.pack(pady=5)

tk.Label(root, text="Enter y2 (μm):").pack(pady=(10, 0))
y2_entry = tk.Entry(root)
y2_entry.pack(pady=5)

# Distance in millimeters
tk.Label(root, text="Distance (mm):").pack(pady=(10, 0))
distance_entry = tk.Entry(root)
distance_entry.pack(pady=5)

# Button to calculate the mRad

tk.Button(root, text="Calculate mRad", command=calculate_mrad).pack(pady=10)

# Buttons for clearing the data
tk.Button(root, text="Clear Data", command=clear_data).pack(pady=5)

root.mainloop()