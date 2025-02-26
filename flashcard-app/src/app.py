import tkinter as tk
from tkinter import messagebox

def on_button_click():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Information", f"You entered: {user_input}")
    else:
        messagebox.showwarning("Input Error", "Please enter something")

# Main function to create the GUI
def main():
    root = tk.Tk()
    root.title("Chinese Flashcard App")
    root.geometry("1000x500")

    large_font = ("Helvetica", 16)

    label = tk.Label(root, text="What lessons are you reviewing? (ex. 1, 4-8, 13)", font=large_font)
    label.pack(pady=10)

    global entry
    entry = tk.Entry(root, width=50, font=large_font)
    entry.pack(pady=10)

    button = tk.Button(root, text="Submit", command=on_button_click, font=large_font)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()