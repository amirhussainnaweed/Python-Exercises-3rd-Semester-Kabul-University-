import tkinter as tk
from encodings.idna import sace_prefix

root = tk.Tk()
root.title("Simple Text Editor")
root.title("Second lab of lecture six")
root.geometry("700x600")
root.minsize(500, 350)

#functions
def clear_text():
    text_field.delete("1.0", tk.END)
    status_label.config(
        text="Status: Text cleared!",
        fg="black"
    )

def insert_text():
    text_field.insert("1.0", """Welcome to the Simple Text Editor.

This is sample text inserted by the program.

You can edit this text, clear it, or disable the editor.

Tkinter makes it possible to create graphical applications
using Python.""")
    status_label.config(
        text="Status: Text inserted!",
        fg="black"
    )
def disable():
    text_field.configure(state="disabled")
    status_label.config(
        text="Status: Text disabled!",
        fg="black"
    )
    clear_button.config(
        state="disabled",
    )
    insert_button.config(
        state="disabled",
    )
    save_button.config(
        state="disabled",
    )
    load_button.config(
        state="disabled",
    )

def enable():
    text_field.configure(state="normal")
    status_label.config(
        text="Status: Text enabled!",
        fg="black"
    )
    clear_button.config(
        state="normal",
    )
    insert_button.config(
        state="normal",
    )
    save_button.config(
        state="normal",
    )
    load_button.config(
        state="normal",
    )

#==========================================================================================================
#optional section, reading and loading from file:
def save_notes():
    notes = text_field.get("1.0", tk.END)
    with open(
        "lecture_six_second_lab_notes.txt",
        "a",
        encoding="utf-8",
    ) as file:
        file.write(notes)
    status_label.config(
        text="Status: Notes saved!",
        fg="green",
        font=("Arial", 12),
    )

def load_notes():
    with open(
        "lecture_six_second_lab_notes.txt",
        "r",
        encoding="utf-8",
    ) as file:
        content = file.read()
    text_field.insert("1.0", content)
    status_label.config(
        text="Status: Notes loaded!",
        fg="green",
        font=("Arial", 12),
    )

#====================================================================================================

#header frame component
header_frame = tk.Frame(root)
title_label = tk.Label(header_frame,text="Simple Text Editor",fg="black")
title_label.pack(padx=10, pady=5)

#main frame component
main_frame = tk.Frame(root)
text_field = tk.Text(main_frame,wrap="word")
text_field.pack(padx=10, pady=10, fill="both", expand=True)
status_label = tk.Label(main_frame,text="Status: Ready",fg="black")
status_label.pack(padx=10, pady=10)

#action_frame component
action_frame = tk.Frame(root)
clear_button = tk.Button(action_frame,text="Clear", command=clear_text, padx=10)
clear_button.pack(padx=20, pady=10, side="left")
insert_button = tk.Button(action_frame,text="Insert", command=insert_text, padx=10)
insert_button.pack(padx=20, pady=10, side="left")
disable_button = tk.Button(action_frame, text="Disable", command=disable, padx=10)
disable_button.pack(padx=20, pady=10, side="left")
enable_button = tk.Button(action_frame, text="Enable", command=enable, padx=10)
enable_button.pack(padx=20, pady=20, side="left")

#save and load buttons
save_button = tk.Button(action_frame, text="Save", command=save_notes, padx=10)
save_button.pack(padx=20, pady=10, side="left")
load_button = tk.Button(action_frame, text="Load", command=load_notes, padx=10)
load_button.pack(padx=20, pady=10, side="left")


header_frame.pack(fill="x")
main_frame.pack(expand=True, fill="both")
action_frame.pack(fill="x")

root.mainloop()