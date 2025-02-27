import tkinter as tk
from gui import create_main_screen

def main():
    root = tk.Tk()
    root.title("Chinese Flashcard App")
    root.geometry("1000x500")

    create_main_screen(root)

    root.mainloop()

if __name__ == "__main__":
    main()