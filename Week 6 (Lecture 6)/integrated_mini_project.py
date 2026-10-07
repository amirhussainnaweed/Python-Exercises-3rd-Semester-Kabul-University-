import tkinter as tk
from tkinter import ttk, messagebox


FILE_NAME = "students.txt"


def save_student():
    student_id = id_entry.get().strip()
    full_name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()
    department = department_combo.get().strip()
    semester = semester_combo.get().strip()
    notes = notes_text.get("1.0", tk.END).strip()

    if not student_id or not full_name or not email or not phone or not department or not semester:
        status_label.config(text="Please fill in all required fields.")
        return

    if "@" not in email:
        status_label.config(text="Please enter a valid email address.")
        return

    record = (
        f"ID: {student_id}\n"
        f"Name: {full_name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Department: {department}\n"
        f"Semester: {semester}\n"
        f"Notes: {notes}\n"
        f"{'-' * 50}\n"
    )

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(record)

        status_label.config(text="Student record saved successfully.")
        messagebox.showinfo("Success", "Student record has been saved.")

    except OSError:
        status_label.config(text="Could not save the student record.")


def clear_form():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    department_combo.set("")
    semester_combo.set("")
    notes_text.delete("1.0", tk.END)
    status_label.config(text="Form cleared.")


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("Student Registration System")
root.geometry("750x700")
root.minsize(650, 600)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

header_frame = ttk.Frame(root, padding=20)
header_frame.grid(row=0, column=0, sticky="ew")
header_frame.columnconfigure(0, weight=1)

title_label = ttk.Label(
    header_frame,
    text="Student Registration System",
    font=("Arial", 22, "bold")
)
title_label.grid(row=0, column=0)

subtitle_label = ttk.Label(
    header_frame,
    text="Advanced Programming - Student Registration",
    font=("Arial", 10)
)
subtitle_label.grid(row=1, column=0, pady=(5, 0))

main_frame = ttk.Frame(root, padding=(20, 0, 20, 20))
main_frame.grid(row=1, column=0, sticky="nsew")

main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(2, weight=1)

personal_frame = ttk.LabelFrame(
    main_frame,
    text="Personal Information",
    padding=15
)
personal_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))

personal_frame.columnconfigure(1, weight=1)
personal_frame.columnconfigure(3, weight=1)

ttk.Label(personal_frame, text="Student ID:").grid(
    row=0, column=0, padx=5, pady=7, sticky="w"
)

id_entry = ttk.Entry(personal_frame)
id_entry.grid(
    row=0, column=1, padx=5, pady=7, sticky="ew"
)

ttk.Label(personal_frame, text="Full Name:").grid(
    row=0, column=2, padx=5, pady=7, sticky="w"
)

name_entry = ttk.Entry(personal_frame)
name_entry.grid(
    row=0, column=3, padx=5, pady=7, sticky="ew"
)

ttk.Label(personal_frame, text="Email:").grid(
    row=1, column=0, padx=5, pady=7, sticky="w"
)

email_entry = ttk.Entry(personal_frame)
email_entry.grid(
    row=1, column=1, padx=5, pady=7, sticky="ew"
)

ttk.Label(personal_frame, text="Phone:").grid(
    row=1, column=2, padx=5, pady=7, sticky="w"
)

phone_entry = ttk.Entry(personal_frame)
phone_entry.grid(
    row=1, column=3, padx=5, pady=7, sticky="ew"
)

academic_frame = ttk.LabelFrame(
    main_frame,
    text="Academic Information",
    padding=15
)
academic_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))

academic_frame.columnconfigure(1, weight=1)
academic_frame.columnconfigure(3, weight=1)

ttk.Label(academic_frame, text="Department:").grid(
    row=0, column=0, padx=5, pady=7, sticky="w"
)

department_combo = ttk.Combobox(
    academic_frame,
    values=[
        "Computer Science",
        "Information Systems",
        "Software Engineering",
        "Information Technology",
        "Data Science"
    ],
    state="readonly"
)
department_combo.grid(
    row=0, column=1, padx=5, pady=7, sticky="ew"
)

ttk.Label(academic_frame, text="Semester:").grid(
    row=0, column=2, padx=5, pady=7, sticky="w"
)

semester_combo = ttk.Combobox(
    academic_frame,
    values=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8"
    ],
    state="readonly"
)
semester_combo.grid(
    row=0, column=3, padx=5, pady=7, sticky="ew"
)

notes_frame = ttk.LabelFrame(
    main_frame,
    text="Notes",
    padding=15
)
notes_frame.grid(row=2, column=0, sticky="nsew", pady=(0, 10))

notes_frame.columnconfigure(0, weight=1)
notes_frame.rowconfigure(0, weight=1)

notes_text = tk.Text(
    notes_frame,
    height=8,
    wrap="word"
)
notes_text.grid(row=0, column=0, sticky="nsew")

notes_scrollbar = ttk.Scrollbar(
    notes_frame,
    orient="vertical",
    command=notes_text.yview
)
notes_scrollbar.grid(row=0, column=1, sticky="ns")

notes_text.config(yscrollcommand=notes_scrollbar.set)

action_frame = ttk.Frame(main_frame)
action_frame.grid(row=3, column=0, sticky="ew", pady=(0, 10))

action_frame.columnconfigure(0, weight=1)
action_frame.columnconfigure(1, weight=1)
action_frame.columnconfigure(2, weight=1)

save_button = ttk.Button(
    action_frame,
    text="Save",
    command=save_student
)
save_button.grid(row=0, column=0, padx=5, sticky="ew")

clear_button = ttk.Button(
    action_frame,
    text="Clear",
    command=clear_form
)
clear_button.grid(row=0, column=1, padx=5, sticky="ew")

exit_button = ttk.Button(
    action_frame,
    text="Exit",
    command=exit_program
)
exit_button.grid(row=0, column=2, padx=5, sticky="ew")

status_frame = ttk.LabelFrame(
    main_frame,
    text="Status",
    padding=10
)
status_frame.grid(row=4, column=0, sticky="ew")

status_frame.columnconfigure(0, weight=1)

status_label = ttk.Label(
    status_frame,
    text="Ready.",
    anchor="center"
)
status_label.grid(row=0, column=0, sticky="ew")

root.mainloop()