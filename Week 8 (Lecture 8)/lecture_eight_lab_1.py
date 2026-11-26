import tkinter as tk

# -----------------------------
# Create the main window
# -----------------------------
root = tk.Tk()
root.title("Mouse Drawing Pad")
root.geometry("800x600")
root.minsize(600, 450)

# -----------------------------
# Brush-size variable
# -----------------------------
brush_size = 8

# -----------------------------
# Create the Canvas
# -----------------------------
canvas = tk.Canvas(
    root,
    bg='white',
    cursor="cross"
)

canvas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)

# -----------------------------
# Coordinate and brush labels
# -----------------------------
coordinate_label = tk.Label(
    root,
    text="Mouse Position: X=0, Y=0"
)
coordinate_label.pack(pady=5)

brush_label = tk.Label(
    root,
    text=f"Brush Size: {brush_size}"
)
brush_label.pack(pady=5)

# -----------------------------
# Update mouse coordinates
# -----------------------------
def update_coordinates(event):
    coordinate_label.config(
        text=f"Mouse Position: X={event.x}, Y={event.y}"
    )

# -----------------------------
# Draw while dragging
# -----------------------------
def draw(event):
    radius = brush_size

    canvas.create_oval(
        event.x - radius,
        event.y - radius,
        event.x + radius,
        event.y + radius,
        fill="black",
        outline="black"
    )

# -----------------------------
# Clear the Canvas
# -----------------------------
def clear_canvas():
    canvas.delete("all")

# -----------------------------
# Increase brush size
# -----------------------------
def increase_brush():
    global brush_size

    brush_size = min(brush_size + 2, 40)

    brush_label.config(
        text=f"Brush Size: {brush_size}"
    )

# -----------------------------
# Decrease brush size
# -----------------------------
def decrease_brush():
    global brush_size

    brush_size = max(brush_size - 2, 2)

    brush_label.config(
        text=f"Brush Size: {brush_size}"
    )

# -----------------------------
# Erase nearby marks
# -----------------------------
def erase_nearby(event):
    erase_radius = 15

    nearby_items = canvas.find_overlapping(
        event.x - erase_radius,
        event.y - erase_radius,
        event.x + erase_radius,
        event.y + erase_radius
    )

    for item in nearby_items:
        canvas.delete(item)

# -----------------------------
# Create the control buttons
# -----------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_canvas
)
clear_button.pack(side="left", padx=5)

increase_button = tk.Button(
    button_frame,
    text="Larger Brush",
    command=increase_brush
)
increase_button.pack(side="left", padx=5)

decrease_button = tk.Button(
    button_frame,
    text="Smaller Brush",
    command=decrease_brush
)
decrease_button.pack(side="left", padx=5)

# -----------------------------
# Bind mouse events
# -----------------------------
canvas.bind(
    "<Motion>",
    update_coordinates
)

canvas.bind(
    "<B1-Motion>",
    draw
)

canvas.bind(
    "<Button-3>",
    erase_nearby
)

# -----------------------------
# Start the application
# -----------------------------
root.mainloop()
