
import tkinter as tk


# -----------------------------
# Create the main window
# -----------------------------
root = tk.Tk()
root.title("Keyboard-Controlled Player")
root.geometry("700x550")
root.minsize(500, 400)


# -----------------------------
# Player settings
# -----------------------------
start_x = 50
start_y = 50
player_size = 40

normal_speed = 10
fast_speed = 20


# -----------------------------
# Create the Canvas
# -----------------------------
canvas = tk.Canvas(
    root,
    bg="white"
)

canvas.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# -----------------------------
# Create the player
# -----------------------------
player = canvas.create_rectangle(
    start_x,
    start_y,
    start_x + player_size,
    start_y + player_size,
    fill="blue",
    outline="darkblue"
)


# -----------------------------
# Coordinate display
# -----------------------------
coordinate_label = tk.Label(
    root,
    text="Player Position: X=50, Y=50",
    font=("Arial", 11)
)

coordinate_label.pack(pady=10)


# -----------------------------
# Update coordinates
# -----------------------------
def update_coordinates():
    x1, y1, x2, y2 = canvas.coords(player)

    coordinate_label.config(
        text=f"Player Position: X={int(x1)}, Y={int(y1)}"
    )


# -----------------------------
# Move the player
# -----------------------------
def move_player(event):

    global normal_speed

    # Handle Reset key
    if event.keysym.lower() == "r":

        x1, y1, x2, y2 = canvas.coords(player)

        canvas.move(
            player,
            start_x - x1,
            start_y - y1
        )

        update_coordinates()
        return "break"

    # Determine movement speed
    if event.state & 0x0001:
        speed = fast_speed
    else:
        speed = normal_speed

    # Determine movement direction
    dx = 0
    dy = 0

    if event.keysym == "Left":
        dx = -speed

    elif event.keysym == "Right":
        dx = speed

    elif event.keysym == "Up":
        dy = -speed

    elif event.keysym == "Down":
        dy = speed

    else:
        return

    # Get current player coordinates
    x1, y1, x2, y2 = canvas.coords(player)

    # Get Canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Check left boundary
    if x1 + dx < 0:
        dx = -x1

    # Check right boundary
    elif x2 + dx > canvas_width:
        dx = canvas_width - x2

    # Check top boundary
    if y1 + dy < 0:
        dy = -y1

    # Check bottom boundary
    elif y2 + dy > canvas_height:
        dy = canvas_height - y2

    # Move the player
    canvas.move(player, dx, dy)

    # Update coordinates
    update_coordinates()

    return "break"


# -----------------------------
# Bind keyboard events
# -----------------------------
root.bind_all(
    "<KeyPress>",
    move_player
)


# -----------------------------
# Set initial keyboard focus
# -----------------------------
canvas.focus_set()


# -----------------------------
# Start the application
# -----------------------------
root.mainloop()
