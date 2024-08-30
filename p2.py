import tkinter as tk
from tkinter import messagebox

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def perform_encryption():
    try:
        text = text_entry.get()
        shift = int(shift_entry.get())
        encrypted_message = encrypt(text, shift)
        result_label.config(text="Encrypted Message: " + encrypted_message)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift key.")

def perform_decryption():
    try:
        text = text_entry.get()
        shift = int(shift_entry.get())
        decrypted_message = decrypt(text, shift)
        result_label.config(text="Decrypted Message: " + decrypted_message)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for the shift key.")

# Setting up the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption and Decryption")
root.geometry("400x300")

# Adding widgets
tk.Label(root, text="Enter Message:").pack(pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

tk.Label(root, text="Enter Shift Key:").pack(pady=10)
shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

tk.Button(root, text="Encrypt", command=perform_encryption).pack(pady=10)
tk.Button(root, text="Decrypt", command=perform_decryption).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Starting the Tkinter event loop
root.mainloop()
