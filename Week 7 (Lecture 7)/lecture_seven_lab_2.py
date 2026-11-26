import tkinter as tk

root = tk.Tk()
root.title("Document Read")
root.geometry("500x500")
root.minsize(500, 500)


#=====================  functions  =============
def key_pressed(event):
    last_key_label.config(
        text=f"Last key Pressed: {event.keysym}"
    )
    event_details_label.config(
        text=f"Keysym: {event.keysym} | Char: {repr(event.char)}"
    )


def clear_display(event):
    last_key_label.config(
        text="Last Key Pressed: None"
    )
    event_details_label.config(
        text="Keysym: None | Char: None"
    )
    status_label.config(
        text="Status: Display Cleared"
    )

def save_status(event):
    status_label.config(
        text=f"Status: Saved"
    )

def entry_key_pressed(event):
    entry_label_event.config(
        text=f"Entry event: {event.keysym} | Char: {repr(event.char)}"
    )





title_label = tk.Label(
    root,
    text="Keyborad events lab",
    font=("Arial", 20),
)
title_label.pack(pady=15)

last_key_label = tk.Label(
    root,
    text="Last Key Pressed: None",
)
last_key_label.pack(pady=10)

event_details_label = tk.Label(
    root,
    text="Keysym: None | Char: None",
)
event_details_label.pack(pady=10)




#entry label and testing the events here
entry_label_event = tk.Label(
    root,
    text="Entry event: None | Char: None",
)
entry_label_event.pack(pady=10)


entry_label = tk.Label(
    root,
    text="Test keyboard focus in this entry:",
)
entry_label.pack(pady=(20, 5))
entry = tk.Entry(
    root, width=35
)
entry.pack(pady=5)


status_label = tk.Label(
    root,
    text="Status: Ready",
)
status_label.pack(pady=20)


#===================== binding the events

root.bind(
    "<KeyPress>",
    key_pressed
)
root.bind(
    "<Escape>",
    clear_display
)
root.bind(
    "<Control-s>",
    save_status
)


entry.bind(
    "<KeyPress>",
    entry_key_pressed
)







root.mainloop()