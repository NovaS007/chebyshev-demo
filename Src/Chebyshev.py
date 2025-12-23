import tkinter as tk
import tkinter.ttk as ttk

# Create the main window
root = tk.Tk()
root.title("Chebyshev Theorem")

# Configure grid weights for responsiveness
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#=========================== Frame for k-value input ===========================#

# Create a frame for k-value input
k_value_frame = ttk.Frame(root)
k_value_frame.grid(row=0, column=0, sticky="nsew")

# Configure grid weights for responsiveness
k_value_frame.columnconfigure(0, weight=1)
k_value_frame.columnconfigure(1, weight=1)
k_value_frame.rowconfigure(0, weight=1)
k_value_frame.rowconfigure(1, weight=1)

# Create a label prompting the user for k value input
k_value_label = ttk.Label(k_value_frame, text="Please enter a k value for Chebyshev's Theorem:")
k_value_label.grid(row=0, column=0, sticky="nsew")

# Placeholder text for the input field
K_VALUE_TEXT_PLACEHOLDER = "Enter k value here"

# Create a textbox for user input with placeholder behavior
k_value_input = tk.Entry(k_value_frame, fg="grey")
k_value_input.grid(row=1, column=0, sticky="ew")
k_value_input.insert(0, K_VALUE_TEXT_PLACEHOLDER)

# Functions to handle focus in and out events
def on_k_value_focus_in(event):
    if k_value_input.get() == K_VALUE_TEXT_PLACEHOLDER:
        k_value_input.delete(0, tk.END)
        k_value_input.config(fg="white")

# Function to handle focus out event
def on_k_value_focus_out(event):
    if k_value_input.get() == "":
        k_value_input.insert(0, K_VALUE_TEXT_PLACEHOLDER)
        k_value_input.config(fg="grey")

# Function to retrieve and print the k-value entered by the user
def get_k_value():
    k_value = k_value_input.get()
    if k_value == K_VALUE_TEXT_PLACEHOLDER or not k_value.strip():
        print("No k-value entered.")
        return
    print(f"K-value entered: {k_value}")
    k_value_input.delete(0, tk.END)
    k_value_input.insert(0, K_VALUE_TEXT_PLACEHOLDER)
    k_value_input.config(fg="grey")

# The first argument is the event type, the second is the function to call
k_value_input.bind("<FocusIn>", on_k_value_focus_in)
k_value_input.bind("<FocusOut>", on_k_value_focus_out)

#=========================== Frame for data points input ===========================#

# Create a frame for data points input
data_points_frame = ttk.Frame(root)
data_points_frame.grid(row=1, column=0, sticky="nsew")

# Configure grid weights for responsiveness
data_points_frame.columnconfigure(0, weight=1)
data_points_frame.columnconfigure(1, weight=1)
data_points_frame.rowconfigure(0, weight=1)
data_points_frame.rowconfigure(1, weight=1)

# Create a label prompting the user for data points input
data_points_label = ttk.Label(data_points_frame, text="Please enter your population data points (separated by spaces):")
data_points_label.grid(row=0, column=0, sticky="nsew")

# Placeholder text for the input field
DATA_POINTS_TEXT_PLACEHOLDER = "Enter data points here"

# Create a textbox for user input with placeholder behavior
data_points_input = tk.Entry(data_points_frame, fg="grey")
data_points_input.grid(row=1, column=0, sticky="ew")
data_points_input.insert(0, DATA_POINTS_TEXT_PLACEHOLDER)

# Functions to handle focus in and out events
def on_data_point_focus_in(event):
    if data_points_input.get() == DATA_POINTS_TEXT_PLACEHOLDER:
        data_points_input.delete(0, tk.END)
        data_points_input.config(fg="white")

# Function to handle focus out event
def on_data_point_focus_out(event):
    if data_points_input.get() == "":
        data_points_input.insert(0, DATA_POINTS_TEXT_PLACEHOLDER)
        data_points_input.config(fg="grey")

# Function to handle data points submission and returns the data points as a list
def get_data_points() -> list:
    data_points = data_points_input.get()
    if data_points == DATA_POINTS_TEXT_PLACEHOLDER or not data_points.strip():
        print("No data points entered.")
        return []
    data_points_input.delete(0, tk.END)
    data_points_input.insert(0, DATA_POINTS_TEXT_PLACEHOLDER)
    data_points_input.config(fg="grey")

    data_points_as_list = [float(point) for point in data_points.split() if point.strip()]
    print(f"Data points entered: {data_points_as_list}")
    return data_points_as_list

# Bind focus in and out events to the textbox
data_points_input.bind("<FocusIn>", on_data_point_focus_in)
data_points_input.bind("<FocusOut>", on_data_point_focus_out)

# Create a button to submit the data points
submit_data_button = ttk.Button(root, text="Submit", command=lambda: (get_k_value(), get_data_points()))
submit_data_button.grid(row=2, column=0, sticky="ew", pady=5)

# Start the Tkinter event loop
root.mainloop()