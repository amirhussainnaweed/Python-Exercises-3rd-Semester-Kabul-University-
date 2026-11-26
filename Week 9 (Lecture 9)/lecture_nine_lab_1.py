import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Settings Panel")
root.geometry("600x650")
root.minsize(500, 550)

#=====================================

default_email = True
default_sms = False
default_desktop = True

default_theme = "System"
default_volume = 50
default_language = "English"

#=======================================

email_var = tk.BooleanVar(value=default_email)
sms_var = tk.BooleanVar(value=default_sms)
desktop_var = tk.BooleanVar(value=default_desktop)

theme_var = tk.StringVar(value=default_theme)

volume_var = tk.IntVar(value=default_volume)


#=========================================

heading = tk.Label(
    root,
    text="Application Settings",
    font=("Arial", 20, "bold")
)
heading.pack(pady=15)

#==========================================

notification_frame = tk.LabelFrame(
    root,
    text="Notification Preferences",
    padx=15,
    pady=10
)
notification_frame.pack(fill="x", padx=20, pady=10)

tk.Checkbutton(
    notification_frame,
    text="Email Notifications",
    variable=email_var
).pack(anchor="w", pady=3)

tk.Checkbutton(
    notification_frame,
    text="SMS Notifications",
    variable=sms_var
).pack(anchor="w", pady=3)

tk.Checkbutton(
    notification_frame,
    text="Desktop Notifications",
    variable=desktop_var
).pack(anchor="w", pady=3)

#======================================================

theme_frame = tk.LabelFrame(
    root,
    text="Application Theme",
    padx=15,
    pady=10
)
theme_frame.pack(fill="x", padx=20, pady=10)

tk.Radiobutton(
    theme_frame,
    text="Light",
    variable=theme_var,
    value="Light"
).pack(anchor="w", pady=3)

tk.Radiobutton(
    theme_frame,
    text="Dark",
    variable=theme_var,
    value="Dark"
).pack(anchor="w", pady=3)

tk.Radiobutton(
    theme_frame,
    text="System",
    variable=theme_var,
    value="System"
).pack(anchor="w", pady=3)

#=======================================

volume_frame = tk.LabelFrame(
    root,
    text="Notification Volume",
    padx=15,
    pady=10
)
volume_frame.pack(fill="x", padx=20, pady=10)

volume_scale = tk.Scale(
    volume_frame,
    from_=0,
    to=100,
    orient="horizontal",
    variable=volume_var,
    length=400
)
volume_scale.pack(fill="x")

# -----------------------------
# 8. Language Selection
# -----------------------------

language_frame = tk.LabelFrame(
    root,
    text="Language",
    padx=15,
    pady=10
)
language_frame.pack(fill="x", padx=20, pady=10)

language_combo = ttk.Combobox(
    language_frame,
    values=[
        "English",
        "Persian",
        "Pashto",
        "Turkish",
        "Arabic"
    ],
    state="readonly"
)

language_combo.set(default_language)
language_combo.pack(fill="x", pady=5)

# -----------------------------
# 9. Summary Area
# -----------------------------

summary_frame = tk.LabelFrame(
    root,
    text="Settings Summary",
    padx=15,
    pady=10
)
summary_frame.pack(fill="x", padx=20, pady=10)

summary_label = tk.Label(
    summary_frame,
    text="Your settings will appear here.",
    justify="left",
    anchor="w",
    font=("Arial", 10)
)
summary_label.pack(fill="x")

# -----------------------------
# 10. Save Settings
# -----------------------------

def save_settings():

    # Get notification settings
    email = email_var.get()
    sms = sms_var.get()
    desktop = desktop_var.get()

    # Get theme
    theme = theme_var.get()

    # Get volume
    volume = volume_var.get()

    # Get language
    language = language_combo.get()

    # Create settings summary
    Summary = (
        f"Email Notifications: {'Enabled' if email else 'Disabled'}\n"
        f"SMS Notifications: {'Enabled' if sms else 'Disabled'}\n"
        f"Desktop Notifications: {'Enabled' if desktop else 'Disabled'}\n"
        f"Theme: {theme}\n"
        f"Notification Volume: {volume}%\n"
        f"Language: {language}"
    )

    # Display summary
    summary_label.config(text="summary")

    status_label.config(text="Settings saved successfully!")

# -----------------------------
# 11. Reset Settings
# -----------------------------

def reset_settings():

    # Restore notification settings
    email_var.set(default_email)
    sms_var.set(default_sms)
    desktop_var.set(default_desktop)

    # Restore theme
    theme_var.set(default_theme)

    # Restore volume
    volume_var.set(default_volume)

    # Restore language
    language_combo.set(default_language)

    # Update summary
    summary_label.config(
        text="Your settings have been reset to their defaults."
    )

    status_label.config(text="Settings reset successfully!")

# -----------------------------
# 12. Save and Reset Buttons
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(
    button_frame,
    text="Save Settings",
    command=save_settings,
    width=15
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Reset Settings",
    command=reset_settings,
    width=15
).pack(side="left", padx=5)

# -----------------------------
# 13. Status Label
# -----------------------------

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    fg="green"
)
status_label.pack(pady=5)

# -----------------------------
# 14. Start GUI
# -----------------------------

root.mainloop()


