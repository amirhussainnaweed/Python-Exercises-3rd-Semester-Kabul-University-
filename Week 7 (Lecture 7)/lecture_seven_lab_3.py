import tkinter as tk

root = tk.Tk()
root.title("Keyboard Events")
root.geometry("400x350")

#==================== functions ===========================
def validate_form():
    username = username_entry.get().strip()
    password = password_entry.get()

    if not username:
        return False, "Please enter your username"
    if not password:
        return False, "Please enter your password"

    return True, "You have logged in"

def login(event=None):
    is_valid, message = validate_form()
    print(type(validate_form()))
    if is_valid:
        status_label.config(text=message)
    else:
        status_label.config(text=message)



def focus_in(event):
    field_name = event.widget.get()
    status_label.config(
        text=f"Active field: {event.widget.winfo_name()}"
    )

def focus_out(event):
    status_label.config(
        text="Status: Field Inactive"
    )


def clear_form(event=None):
    username_entry.delete(0, "end")
    password_entry.delete(0, "end")

    status_label.config(text="Status: Form Cleared")
    username_entry.focus_set()


def show_focus(field_name):
    def handler(event):
        status_label.config(
            text=f"Active field: {field_name}"
        )
    return handler







title_label = tk.Label(
    root,
    text="User Login",
    font=("Arial", 20, "bold"),
)
title_label.pack(pady=20)

username_label = tk.Label(
    root,
    text="Username:",
)
username_label.pack()
username_entry = tk.Entry(
    root,
    width=30,
)
username_entry.pack(pady=10)

password_label = tk.Label(
    root,
    text="Password:",
)
password_label.pack()
password_entry = tk.Entry(
    root,
    width=30,
    show="*",
)
password_entry.pack(pady=10)


login_button = tk.Button(
    root,
    text="Login",
)
login_button.pack(pady=10)

status_label = tk.Label(
    root,
    text="Status: Ready",
)
status_label.pack(pady=5)


#configuration of the functions into buttons and binding events
login_button.config(command=login)

username_entry.bind(
    "<Return>",
    login
)
password_entry.bind(
    "<Return>",
    login
)


username_entry.bind(
    "<FocusIn>",
    show_focus("Username")
)
username_entry.bind(
    "<FocusOut>",
    show_focus("Username inactive")
)
password_entry.bind(
    "<FocusIn>",
    show_focus("Password")
)
password_entry.bind(
    "<FocusOut>",
    show_focus("Password inactive")
)

root.bind_all(
    "<Escape>",
    clear_form
)

username_entry.focus_set()



















root.mainloop()