import tkinter as tk
from tkinter import Text

#window configuration
root = tk.Tk()
root.title("Responsive Layout")
root.geometry("500x400")
root.minsize(500, 400)

header = tk.Frame(root)
content = tk.Frame(root)
footer = tk.Frame(root)

#header section
header.pack(
    fill="x"
)

header_label = tk.Label(
    header,
    text="Student Registration",
    font=("Helvetica", 16)
)
header_label.pack(pady=10)


#content section
content.pack(
    fill="both",
    expand=True
)
name_label = tk.Label(
    content,
    text="Name",
)
name_entry = tk.Entry(
    content
)
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
content.columnconfigure(1, weight=1)

department_label = tk.Label(
    content,
    text="Department"
)
department_entry = tk.Entry(
    content
)
department_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
department_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


#footer section
footer.pack(
    fill="x"
)
footer_text = tk.Label(
    footer,
    text="Advanced Object Oriented Programming in Python"
)
footer_text.pack(pady=10)

root.mainloop()


