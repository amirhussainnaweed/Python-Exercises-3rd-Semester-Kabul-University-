import tkinter as tk

root = tk.Tk()
root.geometry("500x750")
root.minsize(400, 500)
root.title("Interactive GUI")



#functions ====================================================================
def mouse_motion(event):
    coordinates_label.config(
        text=f"x: {event.x} y: {event.y}"
    )

def left_click(event):
    event_label.config(
        text="Last Event: left click"
    )

double_click_counter = 0
def double_click(event):
    global double_click_counter
    double_click_counter += 1
    double_click_label.config(
        text=f"Double Clicks: {double_click_counter}"
    )
    event_label.config(
        text="Last Event: double click"
    )

def mouse_enter(event):
    status_label.config(
        text="Status: Mouse entered the frame"
    )

def mouse_leave(event):
    status_label.config(
        text="Status: Mouse left the frame"
    )
#==============================================================================




#creating event frame
event_frame = tk.Frame(
    root,
    bd=2,
    relief="solid",
)
event_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20,
)

#instruction label
instruction_label = tk.Label(
    event_frame,
    text="Move the mouse or click inside this area",
    font=("Arial", 14, "bold")
)
instruction_label.pack(
    pady=20
)


#feedback labels
coordinates_label = tk.Label(
    root,
    text="Mouse Position: x=0, y=0",
)
coordinates_label.pack(
    pady=20,
    padx=20,
    anchor="w",
)
#===========================
event_label = tk.Label(
    root,
    text="Last Event: None",
)
event_label.pack(
    pady=20,
    padx=20,
    anchor="w"
)
#============================
double_click_label = tk.Label(
    root,
    text="Double Clicks: 0",
)
double_click_label.pack(
    pady=20,
    padx=20,
    anchor="w"
)


#status label
status_label = tk.Label(
    root,
    text="Status: Move the mouse into the frame",
)
status_label.pack(
    pady=10,
    padx=20,
    anchor="w",
)


#events==========================================================
event_frame.bind(
    "<Motion>",
    mouse_motion,
)
event_frame.bind(
    "<Double-Button-1>",
    double_click,
)
event_frame.bind(
    "<Button-1>",
    left_click,
)
event_frame.bind(
    "<Enter>",
    mouse_enter,
)
event_frame.bind(
    "<Leave>",
    mouse_leave,
)






root.mainloop()
