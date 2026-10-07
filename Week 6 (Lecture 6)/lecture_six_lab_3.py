import tkinter as tk

root = tk.Tk()

root.title("Profile card")
root.geometry("600x600")
root.minsize(600, 600)

#creating the profile frame
profile_frame = tk.Frame(root, padx=20, pady=20)
profile_frame.pack(fill="both", expand=True)

heading_label = tk.Label(
    profile_frame,
    text="Profile card",
    font=("Arial", 20, "bold"),
)
heading_label.pack(
    pady=(0, 20)
)


profile_image = tk.PhotoImage(
    file="profile.png"
)
image_label = tk.Label(
    profile_frame,
    image=profile_image,
)
image_label.pack(pady=10)


name_label = tk.Label(
    profile_frame,
    text="Amir Hussain Naweed",
    font=("Arial", 14, "bold"),
)
name_label.pack(
    pady=(10, 5)
)

department_label = tk.Label(
    profile_frame,
    text="Computer Science",
    font=("Arial", 13)
)
department_label.pack(
    pady=3
)


email_label = tk.Label(
    profile_frame,
    text="amirhussainnaweed@gmail.com",
    font=("Arial", 11)
)
email_label.pack(
    pady=3
)



button_frame = tk.Frame(profile_frame)
button_frame.pack(pady=20)

edit_button = tk.Button(
    button_frame,
    text="Edit",
    padx=20
)
edit_button.pack(
    side="left",
    padx=10
)

close_button = tk.Button(
    button_frame,
    text="Close",
    padx=20,
    command=root.destroy
)
close_button.pack(
    side="left",
    padx=10
)













root.mainloop()