
import tkinter as tk

# -----------------------------
# 1. Main Window
# -----------------------------

root = tk.Tk()
root.title("Bouncing Ball Animation")
root.geometry("800x600")
root.minsize(500, 400)


# -----------------------------
# 2. Animation Variables
# -----------------------------

ball_size = 40

start_x = 100
start_y = 100

dx = 4
dy = 3

initial_dx = dx
initial_dy = dy

running = False
after_id = None


# -----------------------------
# 3. Create Canvas and Ball
# -----------------------------

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True, padx=10, pady=10)

ball = canvas.create_oval(
    start_x,
    start_y,
    start_x + ball_size,
    start_y + ball_size,
    fill="red",
    outline="darkred"
)


# -----------------------------
# 4. Animation Function
# -----------------------------

def animate():
    global dx, dy, after_id

    if not running:
        return

    # Move the ball
    canvas.move(ball, dx, dy)

    # Get ball coordinates
    x1, y1, x2, y2 = canvas.coords(ball)

    # Get Canvas dimensions
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Check left and right boundaries
    if x1 <= 0:
        canvas.move(ball, -x1, 0)
        dx = abs(dx)

    elif x2 >= width:
        canvas.move(ball, width - x2, 0)
        dx = -abs(dx)

    # Get updated coordinates
    x1, y1, x2, y2 = canvas.coords(ball)

    # Check top and bottom boundaries
    if y1 <= 0:
        canvas.move(ball, 0, -y1)
        dy = abs(dy)

    elif y2 >= height:
        canvas.move(ball, 0, height - y2)
        dy = -abs(dy)

    # Schedule the next animation update
    after_id = root.after(20, animate)


# -----------------------------
# 5. Start Animation
# -----------------------------

def start_animation():
    global running

    if not running:
        running = True
        animate()


# -----------------------------
# 6. Pause Animation
# -----------------------------

def pause_animation():
    global running, after_id

    running = False

    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None


# -----------------------------
# 7. Reset Animation
# -----------------------------

def reset_animation():
    global dx, dy

    pause_animation()

    # Restore original speed
    dx = initial_dx
    dy = initial_dy

    # Return ball to starting position
    canvas.coords(
        ball,
        start_x,
        start_y,
        start_x + ball_size,
        start_y + ball_size
    )


# -----------------------------
# 8. Increase Speed
# -----------------------------

def increase_speed():
    global dx, dy

    dx *= 1.2
    dy *= 1.2


# -----------------------------
# 9. Decrease Speed
# -----------------------------

def decrease_speed():
    global dx, dy

    dx /= 1.2
    dy /= 1.2


# -----------------------------
# 10. Create Buttons
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Start",
    command=start_animation
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Pause",
    command=pause_animation
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Reset",
    command=reset_animation
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Faster",
    command=increase_speed
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Slower",
    command=decrease_speed
).pack(side="left", padx=5)


# -----------------------------
# 11. Start GUI
# -----------------------------

root.mainloop()
