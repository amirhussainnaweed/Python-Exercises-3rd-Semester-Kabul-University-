
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# -----------------------------
# 1. Connect to the database
# -----------------------------

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# -----------------------------
# 2. Create the students table
# -----------------------------

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        department TEXT NOT NULL,
        semester INTEGER NOT NULL
    )
""")

connection.commit()

# -----------------------------
# 3. Main Window
# -----------------------------

root = tk.Tk()
root.title("Student Management System")
root.geometry("750x650")
root.minsize(650, 550)

# -----------------------------
# 4. Variables
# -----------------------------

name_var = tk.StringVar()
email_var = tk.StringVar()
department_var = tk.StringVar()
semester_var = tk.StringVar()
search_var = tk.StringVar()

selected_student_id = None
student_ids = []

departments = [
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Information Systems"
]

semesters = [str(i) for i in range(1, 9)]

# -----------------------------
# 5. Main Heading
# -----------------------------

heading = tk.Label(
    root,
    text="Student Management System",
    font=("Arial", 20, "bold")
)

heading.pack(pady=15)

# -----------------------------
# 6. Student Form
# -----------------------------

form_frame = tk.LabelFrame(
    root,
    text="Student Information",
    padx=15,
    pady=10
)

form_frame.pack(fill="x", padx=20, pady=10)

# Name

tk.Label(
    form_frame,
    text="Name:"
).grid(row=0, column=0, sticky="w", pady=5)

name_entry = tk.Entry(
    form_frame,
    textvariable=name_var,
    width=40
)

name_entry.grid(row=0, column=1, sticky="ew", pady=5)

# Email

tk.Label(
    form_frame,
    text="Email:"
).grid(row=1, column=0, sticky="w", pady=5)

email_entry = tk.Entry(
    form_frame,
    textvariable=email_var,
    width=40
)

email_entry.grid(row=1, column=1, sticky="ew", pady=5)

# Department

tk.Label(
    form_frame,
    text="Department:"
).grid(row=2, column=0, sticky="w", pady=5)

department_combo = ttk.Combobox(
    form_frame,
    textvariable=department_var,
    values=departments,
    state="readonly"
)

department_combo.grid(row=2, column=1, sticky="ew", pady=5)

# Semester

tk.Label(
    form_frame,
    text="Semester:"
).grid(row=3, column=0, sticky="w", pady=5)

semester_combo = ttk.Combobox(
    form_frame,
    textvariable=semester_var,
    values=semesters,
    state="readonly"
)

semester_combo.grid(row=3, column=1, sticky="ew", pady=5)

form_frame.columnconfigure(1, weight=1)

# -----------------------------
# 7. Student List
# -----------------------------

list_frame = tk.LabelFrame(
    root,
    text="Stored Students",
    padx=10,
    pady=10
)

list_frame.pack(fill="both", expand=True, padx=20, pady=10)

student_listbox = tk.Listbox(
    list_frame,
    height=10,
    font=("Arial", 10)
)

student_listbox.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar = tk.Scrollbar(
    list_frame,
    orient="vertical",
    command=student_listbox.yview
)

scrollbar.pack(side="right", fill="y")

student_listbox.config(
    yscrollcommand=scrollbar.set
)

# -----------------------------
# 8. Clear Form
# -----------------------------

def clear_form():

    global selected_student_id

    selected_student_id = None

    name_var.set("")
    email_var.set("")
    department_var.set("")
    semester_var.set("")

    student_listbox.selection_clear(0, tk.END)

    name_entry.focus_set()


# -----------------------------
# 9. Validate Form Data
# -----------------------------

def get_form_data():

    name = name_var.get().strip()
    email = email_var.get().strip()
    department = department_var.get()
    semester = semester_var.get()

    # Check required fields

    if not name:
        messagebox.showerror(
            "Validation Error",
            "Please enter the student's name."
        )
        name_entry.focus_set()
        return None

    if not email:
        messagebox.showerror(
            "Validation Error",
            "Please enter the student's email."
        )
        email_entry.focus_set()
        return None

    if not department:
        messagebox.showerror(
            "Validation Error",
            "Please select a department."
        )
        department_combo.focus_set()
        return None

    if not semester:
        messagebox.showerror(
            "Validation Error",
            "Please select a semester."
        )
        semester_combo.focus_set()
        return None

    # Basic email validation

    if "@" not in email or "." not in email.split("@")[-1]:
        messagebox.showerror(
            "Validation Error",
            "Please enter a valid email address."
        )
        email_entry.focus_set()
        return None

    return name, email, department, int(semester)


# -----------------------------
# 10. Display Students
# -----------------------------

def display_students(search_text=""):

    global student_ids, selected_student_id

    # Clear old list

    student_listbox.delete(0, tk.END)

    student_ids = []
    selected_student_id = None

    # Retrieve records

    if search_text.strip():

        cursor.execute("""
            SELECT id, name, email, department, semester
            FROM students
            WHERE name LIKE ?
            ORDER BY id DESC
        """, (f"%{search_text.strip()}%",))

    else:

        cursor.execute("""
            SELECT id, name, email, department, semester
            FROM students
            ORDER BY id DESC
        """)

    records = cursor.fetchall()

    # Display records in Listbox

    for student in records:

        student_id = student[0]
        name = student[1]
        email = student[2]
        department = student[3]
        semester = student[4]

        student_ids.append(student_id)

        student_listbox.insert(
            tk.END,
            f"ID: {student_id} | {name} | {email} | "
            f"{department} | Semester {semester}"
        )


# -----------------------------
# 11. Add Student
# -----------------------------

def add_student():

    data = get_form_data()

    if data is None:
        return

    name, email, department, semester = data

    try:

        cursor.execute("""
            INSERT INTO students (name, email, department, semester)
            VALUES (?, ?, ?, ?)
        """, (name, email, department, semester))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Student added successfully."
        )

        display_students(search_var.get())
        clear_form()

    except sqlite3.IntegrityError:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            "This email already exists. Please use another email."
        )

    except sqlite3.Error as error:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            f"An error occurred:\n{error}"
        )


# -----------------------------
# 12. Load Selected Student
# -----------------------------

def load_student(event):

    global selected_student_id

    selection = student_listbox.curselection()

    if not selection:
        return

    # Get selected index

    index = selection[0]

    # Get the corresponding database ID

    selected_student_id = student_ids[index]

    # Retrieve the selected record

    cursor.execute("""
        SELECT name, email, department, semester
        FROM students
        WHERE id = ?
    """, (selected_student_id,))

    student = cursor.fetchone()

    if student:

        name_var.set(student[0])
        email_var.set(student[1])
        department_var.set(student[2])
        semester_var.set(str(student[3]))


# -----------------------------
# 13. Update Student
# -----------------------------

def update_student():

    global selected_student_id

    if selected_student_id is None:

        messagebox.showerror(
            "Selection Error",
            "Please select a student to update."
        )

        return

    data = get_form_data()

    if data is None:
        return

    name, email, department, semester = data

    try:

        cursor.execute("""
            UPDATE students
            SET name = ?, email = ?, department = ?, semester = ?
            WHERE id = ?
        """, (
            name,
            email,
            department,
            semester,
            selected_student_id
        ))

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Student updated successfully."
        )

        display_students(search_var.get())
        clear_form()

    except sqlite3.IntegrityError:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            "This email already belongs to another student."
        )

    except sqlite3.Error as error:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            f"An error occurred:\n{error}"
        )


# -----------------------------
# 14. Delete Student
# -----------------------------

def delete_student():

    global selected_student_id

    if selected_student_id is None:

        messagebox.showerror(
            "Selection Error",
            "Please select a student to delete."
        )

        return

    # Confirm deletion

    confirmation = messagebox.askyesno(
        "Confirm Deletion",
        "Are you sure you want to delete this student?"
    )

    if not confirmation:
        return

    try:

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (selected_student_id,)
        )

        connection.commit()

        messagebox.showinfo(
            "Success",
            "Student deleted successfully."
        )

        display_students(search_var.get())
        clear_form()

    except sqlite3.Error as error:

        connection.rollback()

        messagebox.showerror(
            "Database Error",
            f"An error occurred:\n{error}"
        )


# -----------------------------
# 15. Search Students
# -----------------------------

def search_students():

    search_text = search_var.get().strip()

    display_students(search_text)


# -----------------------------
# 16. Show All Students
# -----------------------------

def show_all_students():

    search_var.set("")

    display_students()


# -----------------------------
# 17. Buttons
# -----------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Add Student",
    command=add_student,
    width=15
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Update Student",
    command=update_student,
    width=15
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete Student",
    command=delete_student,
    width=15
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear Form",
    command=clear_form,
    width=15
).grid(row=0, column=3, padx=5)

# -----------------------------
# 18. Search Area
# -----------------------------

search_frame = tk.LabelFrame(
    root,
    text="Search Students by Name",
    padx=10,
    pady=10
)

search_frame.pack(fill="x", padx=20, pady=10)

search_entry = tk.Entry(
    search_frame,
    textvariable=search_var
)

search_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

tk.Button(
    search_frame,
    text="Search",
    command=search_students
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Show All",
    command=show_all_students
).pack(side="left", padx=5)

# -----------------------------
# 19. Listbox Selection Event
# -----------------------------

student_listbox.bind(
    "<<ListboxSelect>>",
    load_student
)

# -----------------------------
# 20. Initial Display
# -----------------------------

display_students()

# -----------------------------
# 21. Close Application
# -----------------------------

def close_application():

    connection.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_application
)

# -----------------------------
# 22. Start GUI
# -----------------------------

root.mainloop()
