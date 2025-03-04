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

def calculate_mrad(x1, y1, x2, y2, distance_mm):
    """
    Calculate mrad using the provided beam diameters and distance.
    """
    sum_x = (x2 - x1) ** 2
    sum_y = (y2 - y1) ** 2
    radius = math.sqrt(sum_x + sum_y) / 2
    mrad = radius / distance_mm
    return mrad

def get_data(distance_mm):
    """
    Simulate collecting four pieces of data (beam diameters in micrometers).
    """

    x1 = random.uniform(-1400, -1600)
    y1 = random.uniform(600, 900)
    x2 = random.uniform(-300, -450)
    y2 = random.uniform(1600, 1950)

    mrad = calculate_mrad(x1, y1, x2, y2, distance_mm)
    return x1, y1, x2, y2, mrad

def run_script():
    try:
        num_iterations = int(iteration_entry.get())
        distance_mm = float(distance_entry.get())
        mrad_values = []

        for i in range(num_iterations):
            x1, y1, x2, y2, mrad_value = get_data(distance_mm)
            mrad_values.append(mrad_value)
            update_data_window(i + 1, x1, y1, x2, y2, mrad_value)
            # Update the GUI on each iteration to display the result immediately
            root.update_idletasks()

        average_mrad = sum(mrad_values) / len(mrad_values)
        messagebox.showinfo("Success", f"Data collected.\nAverage mrad: {average_mrad:.4f}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Selected File", f"You selected: {file_path}")

def update_data_window(iteration, x1, y1, x2, y2, mrad):
    """
    Update the Listbox to display measurements and calculated mrad.
    """
    data_text = (
        f"Test {iteration}:\n"
        f"  x1 = {x1:.2f} μm, y1 = {y1:.2f} μm\n"
        f"  x2 = {x2:.2f} μm, y2 = {y2:.2f} μm\n"
        f"  mrad = {mrad:.4f}"
    )
    data_listbox.insert(tk.END, data_text)

def clear_data():
    data_listbox.delete(0, tk.END)
    messagebox.showinfo("Success", "Data cleared.")

# Create the main application window
root = tk.Tk()
root.title("Beam Data Collection App")
root.geometry("800x600")

# Create a frame for the PER calculation
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

# Entry for specifying number of iterations
tk.Label(root, text="Number of iterations:").pack(pady=(10, 0))
iteration_entry = tk.Entry(root)
iteration_entry.pack(pady=5)

# Entry for specifying distance in millimeters
tk.Label(root, text="Distance (mm):").pack(pady=(10, 0))
distance_entry = tk.Entry(root)
distance_entry.pack(pady=5)

# Buttons for running the script, selecting a file, and clearing the data
tk.Button(root, text="Run Script", command=run_script).pack(pady=5)
tk.Button(root, text="Select File", command=open_file).pack(pady=5)
tk.Button(root, text="Clear Data", command=clear_data).pack(pady=5)

root.mainloop()