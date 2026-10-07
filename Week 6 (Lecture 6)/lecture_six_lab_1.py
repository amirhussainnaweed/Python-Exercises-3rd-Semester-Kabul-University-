import tkinter as tk

root = tk.Tk()
root.title("Student form")
root.geometry("600x300")
root.minsize(600, 600)


#functions
def save_form():
    name = full_name_entry.get()
    id = student_id_entry.get()
    email = student_email_entry.get()
    phone = student_phone_entry.get()
    address = student_address_text.get("1.0", tk.END)

    print("Name: "+name)
    print("ID: "+id)
    print("Email: "+email)
    print("Phone: "+phone)
    print("Address: "+address)

    status_label.config(
        text="Student form saved successfully",
        fg="green",
    )

def clear_form():
    full_name_entry.delete(0, tk.END)
    student_id_entry.delete(0, tk.END)
    student_email_entry.delete(0, tk.END)
    student_phone_entry.delete(0, tk.END)
    student_address_text.delete("1.0", tk.END)

    status_label.config(
        text="Status: Form cleared.",
        fg="black",
    )





#header frame component
header_frame = tk.Frame(root)
title_label = tk.Label(header_frame, text="Title of the lab 6", font=("Arial", 12, "bold"))
title_label.pack(pady=10)



#form frame component
form_frame = tk.Frame(root)
form_frame.columnconfigure(1, weight=1)
full_name = tk.Label(form_frame, text="enter name")
full_name.grid(row=0, column=0, pady=10, padx=10, sticky="w")
full_name_entry = tk.Entry(form_frame)
full_name_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")

student_id = tk.Label(form_frame, text="enter student id")
student_id.grid(row=1, column=0, pady=10, padx=10, sticky="w")
student_id_entry = tk.Entry(form_frame)
student_id_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

student_email = tk.Label(form_frame, text="enter student email")
student_email.grid(row=2, column=0, pady=10, padx=10, sticky="w")
student_email_entry = tk.Entry(form_frame)
student_email_entry.grid(row=2, column=1, pady=10, padx=10, sticky="ew")

student_phone = tk.Label(form_frame, text="enter student phone")
student_phone.grid(row=3, column=0, pady=10, padx=10, sticky="w")
student_phone_entry = tk.Entry(form_frame)
student_phone_entry.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

student_address = tk.Label(form_frame, text="enter sudent address")
student_address.grid(row=4, column=0, pady=10, padx=10, sticky="nw")
student_address_text = tk.Text(
    form_frame,
    height=10,
    width=30,
)
student_address_text.grid(row=4, column=1, pady=10, padx=10, sticky="nsew")

status_label = tk.Label(form_frame, text="Status: Ready", font=("Arial", 12))
status_label.grid(row=5, column=0,columnspan=2,  pady=10, padx=10)


#action fram components
action_frame = tk.Frame(root)
save_button = tk.Button(action_frame, text="Save", command=save_form, padx=10)
save_button.pack(pady=10,padx=10, side="left" )
clear_button = tk.Button(action_frame, text="Clear", command=clear_form, padx=10)
clear_button.pack(pady=10,padx=10,  side="left")


header_frame.pack(fill="x")
form_frame.pack(fill="both", expand=True)
action_frame.pack()

root.mainloop()