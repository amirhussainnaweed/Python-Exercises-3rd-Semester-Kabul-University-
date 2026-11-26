import tkinter as tk
from tkinter import ttk

# -----------------------------
# 1. Main Window
# -----------------------------

root = tk.Tk()
root.title("Course Selection")
root.geometry("650x650")
root.minsize(550, 550)

# -----------------------------
# 2. Course List
# -----------------------------

courses = [
    "Python Programming",
    "Java Programming",
    "Database Systems",
    "Web Development",
    "Data Structures",
    "Algorithms",
    "Computer Networks",
    "Operating Systems",
    "Software Engineering",
    "Artificial Intelligence",
    "Computer Architecture",
    "Cyber Security",
    "Mobile Application Development",
    "Machine Learning",
    "Advanced Programming"
]

# -----------------------------
# 3. Main Heading
# -----------------------------

heading = tk.Label(
    root,
    text="University Course Selection",
    font=("Arial", 20, "bold")
)
heading.pack(pady=15)

# -----------------------------
# 4. Course Selection Frame
# -----------------------------

course_frame = tk.LabelFrame(
    root,
    text="Select Your Courses",
    padx=15,
    pady=10
)
course_frame.pack(fill="both", expand=True, padx=20, pady=10)

# -----------------------------
# 5. Create Listbox
# -----------------------------

course_listbox = tk.Listbox(
    course_frame,
    selectmode=tk.EXTENDED,
    height=12,
    font=("Arial", 11)
)

course_listbox.pack(
    side="left",
    fill="both",
    expand=True
)

# Add courses to Listbox
for course in courses:
    course_listbox.insert(tk.END, course)

# -----------------------------
# 6. Create Vertical Scrollbar
# -----------------------------

scrollbar = tk.Scrollbar(
    course_frame,
    orient="vertical",
    command=course_listbox.yview
)

scrollbar.pack(side="right", fill="y")

course_listbox.config(
    yscrollcommand=scrollbar.set
)

# -----------------------------
# 7. Selection Counter
# -----------------------------

count_label = tk.Label(
    root,
    text="Selected Courses: 0",
    font=("Arial", 11, "bold")
)
count_label.pack(pady=5)

# -----------------------------
# 8. Semester Selection
# -----------------------------

semester_frame = tk.LabelFrame(
    root,
    text="Select Semester",
    padx=15,
    pady=10
)
semester_frame.pack(fill="x", padx=20, pady=10)

semester_combo = ttk.Combobox(
    semester_frame,
    values=[
        "Semester 1",
        "Semester 2",
        "Semester 3",
        "Semester 4",
        "Semester 5",
        "Semester 6",
        "Semester 7",
        "Semester 8"
    ],
    state="readonly"
)

semester_combo.set("Semester 1")
semester_combo.pack(fill="x", pady=5)

# -----------------------------
# 9. Summary Area
# -----------------------------

summary_frame = tk.LabelFrame(
    root,
    text="Selection Summary",
    padx=15,
    pady=10
)
summary_frame.pack(fill="x", padx=20, pady=10)

summary_label = tk.Label(
    summary_frame,
    text="Your selected courses will appear here.",
    justify="left",
    anchor="w",
    font=("Arial", 10),
    wraplength=550
)
summary_label.pack(fill="x")

# -----------------------------
# 10. Update Selection Count
# -----------------------------

def update_selection_count(event=None):

    selected_indices = course_listbox.curselection()

    count = len(selected_indices)

    count_label.config(
        text=f"Selected Courses: {count}"
    )

# -----------------------------
# 11. Display Selected Courses
# -----------------------------

def display_selection():

    # Get selected course indexes
    selected_indices = course_listbox.curselection()

    # Get selected course names
    selected_courses = [
        course_listbox.get(index)
        for index in selected_indices
    ]

    # Get selected semester
    semester = semester_combo.get()

    # Check whether any course is selected
    if not selected_courses:

        summary_label.config(
            text="Please select at least one course."
        )
        return

    # Create course list for summary
    course_text = "\n".join(
        f"{index + 1}. {course}"
        for index, course in enumerate(selected_courses)
    )

    # Display final summary
    summary = (
        f"Semester: {semester}\n\n"
        f"Selected Courses:\n{course_text}\n\n"
        f"Total Courses: {len(selected_courses)}"
    )

    summary_label.config(text=summary)

# -----------------------------
# 12. Clear Selection
# -----------------------------

def clear_selection():

    # Clear all selected courses
    course_listbox.selection_clear(0, tk.END)

    # Update selection counter
    update_selection_count()

    # Clear summary
    summary_label.config(
        text="Your selected courses will appear here."
    )

# -----------------------------
# 13. Handle Listbox Selection Event
# -----------------------------

course_listbox.bind(
    "<<ListboxSelect>>",
    update_selection_count
)

# -----------------------------
# 14. Create Buttons
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Display Selection",
    command=display_selection,
    width=18
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear Selection",
    command=clear_selection,
    width=18
).pack(side="left", padx=5)

# -----------------------------
# 15. Start GUI
# -----------------------------

root.mainloop()
