# A simple password generator application 
import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_entry.get()
    
    # Validate that the length is a positive integer
    try:
        length = int(length)
        if length < 1:
            raise ValueError("Password length must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
        return
    
    # Determine the character set based on checkboxes
    characters = ""
    if var_uppercase.get():
        characters += string.ascii_uppercase
    if var_lowercase.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation
    
    # Check if any character set is selected
    if not characters:
        messagebox.showwarning("No Character Set Selected", "Please select at least one character set.")
        return
    
    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)  # Clear any existing text
    password_entry.insert(0, password)

# Function to copy password to clipboard
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Please generate a password first.")

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Password Length
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkbox options for character types
var_uppercase = tk.BooleanVar(value=True)
var_lowercase = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack(anchor='w')
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor='w')

# Password display and action buttons
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
