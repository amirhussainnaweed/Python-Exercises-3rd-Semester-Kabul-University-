import tkinter as tk

#Creating main window
root = tk.Tk()
root.title("Student Registration")
root.geometry("500x600")
root.minsize(500, 400)

#creating the title
title = tk.Label(root, text="Student Registration", font=("Helvetica", 18))
title.pack(pady=10)

#Creating a frame
form_frame = tk.Frame(root, pady=30)

#Creating Student_id
student_id_label = tk.Label(
    form_frame,
    text="Student ID",
)
student_id_entry = tk.Entry(form_frame, width=40)
student_id_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
student_id_entry.grid(row=0, column=1, pady=10)

#Creating Student_Name
student_name_label = tk.Label(
    form_frame,
    text="Name",
)
student_name_entry = tk.Entry(form_frame, width=40)
student_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
student_name_entry.grid(row=1, column=1, pady=10)

#creating student_department
student_department_label = tk.Label(
    form_frame,
    text="Department",
)
student_department_entry = tk.Entry(form_frame, width=40)
student_department_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
student_department_entry.grid(row=2, column=1, pady=10)

#creating student_semester
student_semester_label = tk.Label(
    form_frame,
    text="Semester",
)
student_semester_entry = tk.Entry(form_frame, width=40)
student_semester_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
student_semester_entry.grid(row=3, column=1, pady=10)

#functions
def save_student():
    student_id = student_id_entry.get()
    student_name = student_name_entry.get()
    student_department = student_department_entry.get()
    student_semester = student_semester_entry.get()
    print("Student ID: ", student_id)
    print("Student Name: ", student_name)
    print("Student Department: ", student_department)
    print("Student Semester: ", student_semester)

def clear_student():
    student_id_entry.delete(0, tk.END)
    student_name_entry.delete(0, tk.END)
    student_department_entry.delete(0, tk.END)
    student_semester_entry.delete(0, tk.END)



#final buttons
#creating the save button
buttons_frame = tk.Frame(root)

save_button = tk.Button(
    buttons_frame,
    text="Save",
    width=20,
    command=save_student
)
save_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

#creating clear button
clear_button = tk.Button(
    buttons_frame,
    text="Clear",
    width=20,
    command=clear_student
)
clear_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")


#adding them to the main window
form_frame.pack()
buttons_frame.pack()
root.mainloop()