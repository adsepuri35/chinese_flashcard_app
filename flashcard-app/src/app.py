import tkinter as tk
from tkinter import messagebox

def convert_lesson_string_to_list(lessons_selected):
    lessons = lessons_selected.split(',')
    lesson_list = []

    for lesson in lessons:
        lesson = lesson.strip()
        if '-' in lesson:
            start, end = lesson.split('-')
            if start.isdigit() and end.isdigit():
                lesson_list.extend(range(int(start), int(end) + 1))
            else:
                return None
        elif lesson.isdigit():
            lesson_list.append(int(lesson))
        else:
            return None
        
    return lesson_list

def on_button_click():
    lessons_selected = entry.get()
    lessons_list = convert_lesson_string_to_list(lessons_selected)
    if lessons_selected:
        show_new_screen(lessons_list)
    else:
        messagebox.showwarning("Input Error", "Please enter something")

def show_new_screen(selected_lessons):
    for widget in root.winfo_children():
        widget.pack_forget()

    lessons_text = f"Selected lessons: {', '.join(map(str, selected_lessons))}"
    new_label = tk.Label(root, text=lessons_text, font=("Helvetica", 16))
    new_label.pack(pady=10)

    new_button = tk.Button(root, text="Go Back", command=show_main_screen, font=("Helvetica", 16))
    new_button.pack(pady=10)

def show_main_screen():
    for widget in root.winfo_children():
        widget.pack_forget()

    label.pack(pady=10)
    entry.pack(pady=10)
    button.pack(pady=10)

def main():
    global root, label, entry, button
    root = tk.Tk()
    root.title("Chinese Flashcard App")
    root.geometry("1000x500")

    large_font = ("Helvetica", 16)

    label = tk.Label(root, text="What lessons are you reviewing? (ex. 1, 4-8, 13)", font=large_font)
    label.pack(pady=10)

    # global entry
    entry = tk.Entry(root, width=50, font=large_font)
    entry.pack(pady=10)

    button = tk.Button(root, text="Submit", command=on_button_click, font=large_font)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()