from tkinter import *

# Create the main window
# TK() creates a blank window
root = Tk()
root.geometry("640x480")
root.title("Chebyshev")

# Label(root, text="Chebyshev") creates a text label in the window
kValueLabel = Label(root, text="Please enter a k value for Chebyshev's Theorem:")
# Label.pack() adds the label to the window
kValueLabel.pack(padx=5, pady=5)

# Placeholder text for the input field
K_VALUE_TEXT_PLACEHOLDER = "Enter k value here"

# Create a textbox for user input with placeholder behavior
kValueTextBox = Entry(root, fg="grey")
kValueTextBox.pack(padx=5, pady=5)
kValueTextBox.insert(0, K_VALUE_TEXT_PLACEHOLDER)

# Functions to handle focus in and out events
def on_focus_in(event):
    if kValueTextBox.get() == K_VALUE_TEXT_PLACEHOLDER:
        # Clear the placeholder text
        kValueTextBox.delete(0, END)
        # Change text color to white
        kValueTextBox.config(fg="white")

# Function to handle focus out event
def on_focus_out(event):
    # If the textbox is empty, restore the placeholder
    if kValueTextBox.get() == "":
        kValueTextBox.insert(0, K_VALUE_TEXT_PLACEHOLDER)
        kValueTextBox.config(fg="grey")

# Bind focus in and out events to the textbox
# The first argument is the event type, the second is the function to call
kValueTextBox.bind("<FocusIn>", on_focus_in)
kValueTextBox.bind("<FocusOut>", on_focus_out)

# Function to retrieve and print the k-value entered by the user
def get_k_value():
    k_value = kValueTextBox.get()
    if k_value == K_VALUE_TEXT_PLACEHOLDER or not k_value.strip():
        print("No k-value entered.")
        return
    print(f"K-value entered: {k_value}")

# Create a button to submit the k-value
button = Button(root, text="Submit", command=get_k_value)
button.pack(padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()