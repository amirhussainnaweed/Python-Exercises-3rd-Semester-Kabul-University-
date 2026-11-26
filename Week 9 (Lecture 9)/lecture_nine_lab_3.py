
import tkinter as tk
from tkinter import ttk, messagebox

# -----------------------------
# 1. Main Window
# -----------------------------

root = tk.Tk()
root.title("Student Preferences Form")
root.geometry("700x850")
root.minsize(600, 700)

# -----------------------------
# 2. Available Options
# -----------------------------

departments = [
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Information Systems"
]

skills = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "PHP",
    "SQL",
    "React",
    "Laravel",
    "HTML and CSS",
    "C#",
    "Dart",
    "Machine Learning"
]

# -----------------------------
# 3. Tkinter Variables
# -----------------------------

study_mode_var = tk.StringVar(value="")
email_var = tk.BooleanVar(value=False)
sms_var = tk.BooleanVar(value=False)
phone_var = tk.BooleanVar(value=False)
experience_var = tk.IntVar(value=0)

# -----------------------------
# 4. Main Heading
# -----------------------------

heading = tk.Label(
    root,
    text="Student Preferences Form",
    font=("Arial", 20, "bold")
)

heading.pack(pady=15)

# -----------------------------
# 5. Personal Information
# -----------------------------

personal_frame = tk.LabelFrame(
    root,
    text="Personal Information",
    padx=15,
    pady=10
)

personal_frame.pack(fill="x", padx=20, pady=8)

tk.Label(
    personal_frame,
    text="Student Name:"
).pack(anchor="w")

name_entry = tk.Entry(
    personal_frame,
    font=("Arial", 11)
)

name_entry.pack(fill="x", pady=5)

# -----------------------------
# 6. Academic Information
# -----------------------------

academic_frame = tk.LabelFrame(
    root,
    text="Academic Information",
    padx=15,
    pady=10
)

academic_frame.pack(fill="x", padx=20, pady=8)

tk.Label(
    academic_frame,
    text="Department:"
).pack(anchor="w")

department_combo = ttk.Combobox(
    academic_frame,
    values=departments,
    state="readonly"
)

department_combo.pack(fill="x", pady=5)

# -----------------------------
# 7. Study Mode
# -----------------------------

study_frame = tk.LabelFrame(
    root,
    text="Study Mode",
    padx=15,
    pady=10
)

study_frame.pack(fill="x", padx=20, pady=8)

tk.Radiobutton(
    study_frame,
    text="Full-time",
    variable=study_mode_var,
    value="Full-time"
).pack(anchor="w")

tk.Radiobutton(
    study_frame,
    text="Part-time",
    variable=study_mode_var,
    value="Part-time"
).pack(anchor="w")

tk.Radiobutton(
    study_frame,
    text="Online",
    variable=study_mode_var,
    value="Online"
).pack(anchor="w")

# -----------------------------
# 8. Communication Preferences
# -----------------------------

communication_frame = tk.LabelFrame(
    root,
    text="Communication Preferences",
    padx=15,
    pady=10
)

communication_frame.pack(fill="x", padx=20, pady=8)

tk.Checkbutton(
    communication_frame,
    text="Email",
    variable=email_var
).pack(anchor="w")

tk.Checkbutton(
    communication_frame,
    text="SMS",
    variable=sms_var
).pack(anchor="w")

tk.Checkbutton(
    communication_frame,
    text="Phone",
    variable=phone_var
).pack(anchor="w")

# -----------------------------
# 9. Programming Experience
# -----------------------------

experience_frame = tk.LabelFrame(
    root,
    text="Programming Experience (0-10)",
    padx=15,
    pady=10
)

experience_frame.pack(fill="x", padx=20, pady=8)

experience_scale = tk.Scale(
    experience_frame,
    from_=0,
    to=10,
    orient="horizontal",
    variable=experience_var,
    length=400
)

experience_scale.pack(fill="x")

# -----------------------------
# 10. Programming Skills
# -----------------------------

skills_frame = tk.LabelFrame(
    root,
    text="Select Your Programming Skills",
    padx=15,
    pady=10
)

skills_frame.pack(fill="x", padx=20, pady=8)

skills_listbox = tk.Listbox(
    skills_frame,
    selectmode=tk.EXTENDED,
    height=6,
    font=("Arial", 10)
)

skills_listbox.pack(
    fill="x",
    expand=True
)

# Add skills to Listbox

for skill in skills:
    skills_listbox.insert(tk.END, skill)

# -----------------------------
# 11. Summary Area
# -----------------------------

summary_frame = tk.LabelFrame(
    root,
    text="Student Preferences Summary",
    padx=15,
    pady=10
)

summary_frame.pack(fill="both", expand=True, padx=20, pady=8)

summary_text = tk.Text(
    summary_frame,
    height=10,
    font=("Arial", 10),
    wrap="word",
    state="disabled"
)

summary_text.pack(fill="both", expand=True)

# -----------------------------
# 12. Get Experience Category
# -----------------------------

def get_experience_category(level):

    if level <= 2:
        return "Beginner"

    elif level <= 5:
        return "Basic"

    elif level <= 8:
        return "Intermediate"

    else:
        return "Advanced"


# -----------------------------
# 13. Submit and Validate Form
# -----------------------------

def submit_form():

    # Get personal information
    name = name_entry.get().strip()

    # Get academic information
    department = department_combo.get()

    # Get study mode
    study_mode = study_mode_var.get()

    # Get communication preferences
    email = email_var.get()
    sms = sms_var.get()
    phone = phone_var.get()

    # Get programming experience
    experience = experience_var.get()

    # Get selected programming skills
    selected_indices = skills_listbox.curselection()

    selected_skills = [
        skills_listbox.get(index)
        for index in selected_indices
    ]

    # -------------------------
    # Validation
    # -------------------------

    if not name:
        messagebox.showerror(
            "Validation Error",
            "Please enter your student name."
        )
        name_entry.focus_set()
        return

    if not department:
        messagebox.showerror(
            "Validation Error",
            "Please select a department."
        )
        department_combo.focus_set()
        return

    if not study_mode:
        messagebox.showerror(
            "Validation Error",
            "Please select a study mode."
        )
        return

    if not (email or sms or phone):
        messagebox.showerror(
            "Validation Error",
            "Select at least one communication preference."
        )
        return

    if not selected_skills:
        messagebox.showerror(
            "Validation Error",
            "Please select at least one programming skill."
        )
        return

    # -------------------------
    # Prepare Summary
    # -------------------------

    communication = []

    if email:
        communication.append("Email")

    if sms:
        communication.append("SMS")

    if phone:
        communication.append("Phone")

    communication_text = ", ".join(communication)

    skills_text = "\n".join(
        f"  - {skill}"
        for skill in selected_skills
    )

    experience_category = get_experience_category(experience)

    summary = (
        "STUDENT PREFERENCES SUMMARY\n"
        "================================\n\n"
        "PERSONAL INFORMATION\n"
        f"Name: {name}\n\n"
        "ACADEMIC INFORMATION\n"
        f"Department: {department}\n"
        f"Study Mode: {study_mode}\n\n"
        "COMMUNICATION PREFERENCES\n"
        f"Selected Methods: {communication_text}\n\n"
        "PROGRAMMING EXPERIENCE\n"
        f"Experience Level: {experience}/10\n"
        f"Category: {experience_category}\n\n"
        "PROGRAMMING SKILLS\n"
        f"{skills_text}"
    )

    # -------------------------
    # Display Summary
    # -------------------------

    summary_text.config(state="normal")

    summary_text.delete("1.0", tk.END)

    summary_text.insert(tk.END, summary)

    summary_text.config(state="disabled")


# -----------------------------
# 14. Submit Button
# -----------------------------

button_frame = tk.Frame(root)

button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Submit Preferences",
    command=submit_form,
    width=20
).pack(side="left", padx=5)

# -----------------------------
# 15. Start GUI
# -----------------------------

root.mainloop()
