import tkinter as tk
from tkinter import messagebox
from utils import convert_lesson_string_to_list

def create_main_screen(root):
    global lesson_question_label, entry, review_question_label, button, checkbox_frame, hanzi_var, pinyin_var, translations_var

    large_font = ("Helvetica", 16)

    lesson_question_label = tk.Label(root, text="What lessons are you reviewing? (ex. 1, 4-8, 13)", font=large_font)
    lesson_question_label.pack(pady=10)

    entry = tk.Entry(root, width=50, font=large_font)
    entry.pack(pady=10)

    review_question_label = tk.Label(root, text="What are you reviewing?", font=large_font)
    review_question_label.pack(pady=10)

    checkbox_frame = tk.Frame(root)
    checkbox_frame.pack(pady=10)

    hanzi_var = tk.IntVar()
    pinyin_var = tk.IntVar()
    translations_var = tk.IntVar()

    hanzi_checkbox = tk.Checkbutton(checkbox_frame, text="Hanzi", variable=hanzi_var, font=large_font)
    pinyin_checkbox = tk.Checkbutton(checkbox_frame, text="Pinyin", variable=pinyin_var, font=large_font)
    translations_checkbox = tk.Checkbutton(checkbox_frame, text="Translations", variable=translations_var, font=large_font)

    hanzi_checkbox.pack(side=tk.LEFT, padx=5)
    pinyin_checkbox.pack(side=tk.LEFT, padx=5)
    translations_checkbox.pack(side=tk.LEFT, padx=5)

    button = tk.Button(root, text="Submit", command=lambda: submit_button_click(root), font=large_font)
    button.pack(pady=10)

def submit_button_click(root):
    lessons_selected = entry.get()
    lessons_list = convert_lesson_string_to_list(lessons_selected)
    if lessons_list and (hanzi_var.get() + pinyin_var.get() + translations_var.get() > 0):
        show_new_screen(lessons_list, root)
    elif not lessons_list:
        messagebox.showwarning("Input Error", "Please enter a valid lesson string (e.g., 1, 4-8, 13)")
    else:
        messagebox.showwarning("Input Error", "Please select what you would like to review")

def show_new_screen(selected_lessons, root):
    for widget in root.winfo_children():
        widget.pack_forget()

    lessons_text = f"Selected lessons: {', '.join(map(str, selected_lessons))}"
    new_label = tk.Label(root, text=lessons_text, font=("Helvetica", 16))
    new_label.pack(pady=10)

    review_text = "Reviewing: "
    selected_options = []
    if hanzi_var.get():
        selected_options.append("Hanzi")
    if pinyin_var.get():
        selected_options.append("Pinyin")
    if translations_var.get():
        selected_options.append("Translations")

    review_text += ", ".join(selected_options)

    review_label = tk.Label(root, text=review_text, font=("Helvetica", 16))
    review_label.pack(pady=10)

    new_button = tk.Button(root, text="Go Back", command=lambda: show_main_screen(root), font=("Helvetica", 16))
    new_button.pack(pady=10)

def show_main_screen(root):
    for widget in root.winfo_children():
        widget.pack_forget()

    lesson_question_label.pack(pady=10)
    entry.pack(pady=10)
    checkbox_frame.pack(pady=10)
    button.pack(pady=10)