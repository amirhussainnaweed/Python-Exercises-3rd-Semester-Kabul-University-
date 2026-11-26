import random
import tkinter as tk
from tkinter import ttk


class SnakeGame(tk.Tk):
    """A small, polished Snake game built with Tkinter."""

    BG = "#0b1220"
    PANEL = "#111c2e"
    PANEL_BORDER = "#22334d"
    CANVAS = "#0f1a2b"
    GRID = "#17263b"
    TEXT = "#e6edf7"
    MUTED = "#91a4bf"
    ACCENT = "#46e6a5"
    ACCENT_DARK = "#1fa979"
    FOOD = "#ff6b7a"
    SNAKE_HEAD = "#7cf2c2"
    SNAKE_BODY = "#46d9a0"

    CELL = 24
    COLS = 25
    ROWS = 22

    def __init__(self):
        super().__init__()

        self.title("Snake — Tkinter Edition")
        self.configure(bg=self.BG)
        self.resizable(False, False)

        self.running = False
        self.paused = False
        self.game_over = False
        self.after_id = None
        self.score = 0
        self.high_score = 0
        self.speed = 105
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        self.snake = []
        self.food = None

        self._setup_styles()
        self._build_layout()
        self._bind_controls()
        self.reset_round()

    def _setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure(
            "Game.TButton",
            background=self.ACCENT_DARK,
            foreground="#ffffff",
            borderwidth=0,
            padding=(12, 9),
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Game.TButton", background=[("active", self.ACCENT)])
        style.configure(
            "Ghost.TButton",
            background=self.PANEL,
            foreground=self.TEXT,
            borderwidth=1,
            relief="solid",
            padding=(12, 8),
            font=("Segoe UI", 10),
        )
        style.map("Ghost.TButton", background=[("active", self.PANEL_BORDER)])

    def _build_layout(self):
        outer = tk.Frame(self, bg=self.BG, padx=22, pady=22)
        outer.pack()

        header = tk.Frame(outer, bg=self.BG)
        header.pack(fill="x", pady=(0, 16))

        tk.Label(
            header,
            text="SNAKE",
            bg=self.BG,
            fg=self.ACCENT,
            font=("Segoe UI", 25, "bold"),
        ).pack(side="left")
        tk.Label(
            header,
            text="Tkinter Edition",
            bg=self.BG,
            fg=self.MUTED,
            font=("Segoe UI", 11),
        ).pack(side="left", padx=(12, 0), pady=(8, 0))

        content = tk.Frame(outer, bg=self.BG)
        content.pack()

        self.sidebar = tk.Frame(
            content,
            bg=self.PANEL,
            width=220,
            height=self.ROWS * self.CELL,
            highlightbackground=self.PANEL_BORDER,
            highlightthickness=1,
        )
        self.sidebar.pack(side="left", fill="y", padx=(0, 18))
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="CURRENT RUN",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w", padx=18, pady=(24, 5))

        self.score_value = tk.Label(
            self.sidebar,
            text="000",
            bg=self.PANEL,
            fg=self.TEXT,
            font=("Consolas", 30, "bold"),
        )
        self.score_value.pack(anchor="w", padx=16)

        tk.Label(
            self.sidebar,
            text="BEST SCORE",
            bg=self.PANEL,
            fg=self.MUTED,
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w", padx=18, pady=(24, 5))

        self.best_value = tk.Label(
            self.sidebar,
            text="000",
            bg=self.PANEL,
            fg=self.ACCENT,
            font=("Consolas", 22, "bold"),
        )
        self.best_value.pack(anchor="w", padx=16)

        self.status_value = tk.Label(
            self.sidebar,
            text="Ready when you are",
            bg=self.PANEL,
            fg=self.MUTED,
            justify="left",
            wraplength=175,
            font=("Segoe UI", 10),
        )
        self.status_value.pack(anchor="w", padx=18, pady=(28, 18))

        ttk.Button(
            self.sidebar,
            text="Start Game",
            style="Game.TButton",
            command=self.start_game,
        ).pack(fill="x", padx=16, pady=(0, 9))
        ttk.Button(
            self.sidebar,
            text="Restart",
            style="Ghost.TButton",
            command=self.restart_game,
        ).pack(fill="x", padx=16, pady=(0, 20))

        help_box = tk.Frame(self.sidebar, bg="#0d1727", padx=14, pady=13)
        help_box.pack(fill="x", side="bottom", padx=12, pady=12)
        tk.Label(
            help_box,
            text="CONTROLS",
            bg="#0d1727",
            fg=self.ACCENT,
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w")
        tk.Label(
            help_box,
            text="Arrow keys / WASD\nSpace  Pause\nR  Restart",
            bg="#0d1727",
            fg=self.MUTED,
            justify="left",
            font=("Segoe UI", 9),
        ).pack(anchor="w", pady=(7, 0))

        board_frame = tk.Frame(content, bg=self.PANEL, padx=8, pady=8)
        board_frame.pack(side="left")
        self.canvas = tk.Canvas(
            board_frame,
            width=self.COLS * self.CELL,
            height=self.ROWS * self.CELL,
            bg=self.CANVAS,
            highlightthickness=0,
        )
        self.canvas.pack()

        footer = tk.Label(
            outer,
            text="Eat the pink squares, grow your score, and avoid the walls.",
            bg=self.BG,
            fg=self.MUTED,
            font=("Segoe UI", 9),
        )
        footer.pack(anchor="w", pady=(12, 0))

    def _bind_controls(self):
        self.bind_all("<Up>", lambda _event: self.change_direction((0, -1)))
        self.bind_all("<Down>", lambda _event: self.change_direction((0, 1)))
        self.bind_all("<Left>", lambda _event: self.change_direction((-1, 0)))
        self.bind_all("<Right>", lambda _event: self.change_direction((1, 0)))
        self.bind_all("<w>", lambda _event: self.change_direction((0, -1)))
        self.bind_all("<s>", lambda _event: self.change_direction((0, 1)))
        self.bind_all("<a>", lambda _event: self.change_direction((-1, 0)))
        self.bind_all("<d>", lambda _event: self.change_direction((1, 0)))
        self.bind_all("<space>", lambda _event: self.toggle_pause())
        self.bind_all("<r>", lambda _event: self.restart_game())

    def reset_round(self):
        self.running = False
        self.paused = False
        self.game_over = False
        self.score = 0
        self.direction = (1, 0)
        self.next_direction = (1, 0)
        center_y = self.ROWS // 2
        self.snake = [(8, center_y), (7, center_y), (6, center_y)]
        self.food = self._new_food()
        self._update_scoreboard()
        self.status_value.config(text="Ready when you are")
        self.draw()

    def _new_food(self):
        available = [
            (x, y)
            for x in range(self.COLS)
            for y in range(self.ROWS)
            if (x, y) not in self.snake
        ]
        return random.choice(available)

    def start_game(self):
        if self.running:
            return
        if self.game_over:
            self.reset_round()
        self.running = True
        self.paused = False
        self.status_value.config(text="Game on — keep moving!")
        self._schedule_tick()

    def restart_game(self):
        self.reset_round()
        self.start_game()

    def toggle_pause(self):
        if not self.running or self.game_over:
            return
        self.paused = not self.paused
        self.status_value.config(text="Paused — press Space to resume" if self.paused else "Game on — keep moving!")
        self.draw()

    def change_direction(self, new_direction):
        if self.game_over:
            return
        current_x, current_y = self.direction
        new_x, new_y = new_direction
        if (new_x, new_y) == (-current_x, -current_y):
            return
        self.next_direction = new_direction
        if not self.running:
            self.start_game()

    def _schedule_tick(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        self.after_id = self.after(self.speed, self.tick)

    def tick(self):
        self.after_id = None
        if not self.running:
            return
        if self.paused:
            self._schedule_tick()
            return

        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        move_x, move_y = self.direction
        new_head = (head_x + move_x, head_y + move_y)

        hit_wall = not (0 <= new_head[0] < self.COLS and 0 <= new_head[1] < self.ROWS)
        hit_self = new_head in self.snake[:-1]
        if hit_wall or hit_self:
            self.finish_game()
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1
            self.high_score = max(self.high_score, self.score)
            self.food = self._new_food()
            self._update_scoreboard()
        else:
            self.snake.pop()

        self.draw()
        self._schedule_tick()

    def finish_game(self):
        self.running = False
        self.game_over = True
        self.status_value.config(text="Game over — press R to try again")
        self._update_scoreboard()
        self.draw()

    def _update_scoreboard(self):
        self.score_value.config(text=f"{self.score:03d}")
        self.best_value.config(text=f"{self.high_score:03d}")

    def draw(self):
        self.canvas.delete("all")

        for x in range(0, self.COLS * self.CELL + 1, self.CELL):
            self.canvas.create_line(x, 0, x, self.ROWS * self.CELL, fill=self.GRID)
        for y in range(0, self.ROWS * self.CELL + 1, self.CELL):
            self.canvas.create_line(0, y, self.COLS * self.CELL, y, fill=self.GRID)

        if self.food:
            x, y = self.food
            pad = 5
            self.canvas.create_oval(
                x * self.CELL + pad,
                y * self.CELL + pad,
                (x + 1) * self.CELL - pad,
                (y + 1) * self.CELL - pad,
                fill=self.FOOD,
                outline="",
            )

        for index, (x, y) in enumerate(self.snake):
            pad = 2 if index == 0 else 3
            self.canvas.create_rectangle(
                x * self.CELL + pad,
                y * self.CELL + pad,
                (x + 1) * self.CELL - pad,
                (y + 1) * self.CELL - pad,
                fill=self.SNAKE_HEAD if index == 0 else self.SNAKE_BODY,
                outline="",
            )

        if not self.running and not self.game_over:
            self._overlay("PRESS START", "Use the arrow keys or WASD to begin")
        elif self.paused:
            self._overlay("PAUSED", "Press Space to continue")
        elif self.game_over:
            self._overlay("GAME OVER", f"Score: {self.score}   •   Press R to restart")

    def _overlay(self, title, subtitle):
        width = self.COLS * self.CELL
        height = self.ROWS * self.CELL
        self.canvas.create_rectangle(0, 0, width, height, fill=self.BG, stipple="gray50", outline="")
        self.canvas.create_text(
            width // 2,
            height // 2 - 20,
            text=title,
            fill=self.TEXT,
            font=("Segoe UI", 22, "bold"),
        )
        self.canvas.create_text(
            width // 2,
            height // 2 + 18,
            text=subtitle,
            fill=self.MUTED,
            font=("Segoe UI", 10),
        )


if __name__ == "__main__":
    SnakeGame().mainloop()
