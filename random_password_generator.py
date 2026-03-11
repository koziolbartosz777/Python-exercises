# import random 
# import string

# signs = string.ascii_letters + string.digits + "!@#$%^&*()"
# password=""

# while True:
#     pass_length = int(input("Enter your password length: "))
#     if pass_length<=0:
#         continue
#     break
    

# for i in range(pass_length):
#     choice = random.choice(signs)
#     password+=choice


# print(password)

#------------------------------------------------------------------

# import random
# import string

# def generate_password():

#     password = ""

#     length = int(input("Enter your password length: ").strip())
#     include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
#     include_special = input("Include special characters? (yes/no): ").strip().lower()
#     include_digits = input("Include digits? (yes/no): ").strip().lower()

#     characters = string.ascii_lowercase

#     if include_uppercase in ("yes", "y"):
#         characters+=string.ascii_uppercase
#         password += random.choice(string.ascii_uppercase)
#     if include_special in ("yes", "y"):
#         characters+=string.punctuation
#         password += random.choice(string.punctuation)
#     if include_digits in ("yes", "y"):
#         characters+=string.digits
#         password += random.choice(string.digits)

#     curr_pass_len = len(password)
#     remaining_pass_len = length - curr_pass_len

#     for _ in range(remaining_pass_len):
#         password+=random.choice(characters)    
    
#     password_list = list(password)
#     random.shuffle(password_list)
#     password = "".join(password_list)

#     print(password)


# generate_password()

#------------------------------------------------------------------

import random
import string
import tkinter as tk
from tkinter import messagebox

# Funkcja generująca hasło
def generate_password():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    if length < 1:
        messagebox.showerror("Error", "Password length must be at least 1")
        return

    characters = string.ascii_lowercase
    password = ""

    if include_uppercase:
        characters += string.ascii_uppercase
        password += random.choice(string.ascii_uppercase)

    if include_special:
        characters += string.punctuation
        password += random.choice(string.punctuation)

    if include_digits:
        characters += string.digits
        password += random.choice(string.digits)

    remaining_len = length - len(password)
    for _ in range(remaining_len):
        password += random.choice(characters)

    # Tasowanie hasła
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    password_display.delete(0, tk.END)
    password_display.insert(0, password)

def copy_password():
    password = password_display.get()
    if password:
        try:
            root.clipboard_clear()
            root.clipboard_append(password)
            root.update()
            messagebox.showinfo("Copied", "Password has been copied")
        except Exception as e:
            messagebox.showerror("Error", f"Could not copy password: {e}")
    else:
        messagebox.showwarning("Warning", "No password to copy")

# Tworzenie GUI
root = tk.Tk()
root.title("Password Generator")

# Długość hasła
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)
length_entry.insert(0, "12")  # domyślna długość

# Opcje
uppercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).grid(row=1, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2, sticky="w")
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).grid(row=3, column=0, columnspan=2, sticky="w")

# Przycisk generowania
tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)

#Przycisk kopiowania hasła
tk.Button(root, text="Copy password", command=copy_password).grid(row=6, column=0, columnspan=2, pady=5)


# Pole wyświetlające hasło
password_display = tk.Entry(root, width=30)
password_display.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()