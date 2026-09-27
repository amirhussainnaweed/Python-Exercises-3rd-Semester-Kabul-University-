import tkinter as tk

#Creating the main window
root = tk.Tk()
root.title("Advanced Programming Lab")
root.geometry("800x500")
root.minsize(600, 300)

#Creating the heading
heading = tk.Label(
    root,
    text="Advanced Programming Lab",
)

#one container for the buttons
button_frame = tk.Frame()

#Creating buttons and make them feel horizontally
button1 = tk.Button(button_frame, text="Button 1")
button2 = tk.Button(button_frame, text="Button 2")
button3 = tk.Button(button_frame, text="Button 3")


heading.pack(
    pady=20
)
button_frame.pack(
    fill="x",
    padx=20,
    pady=10
)
button1.pack(fill="x",pady=5)
button2.pack(fill="x" ,pady=5)
button3.pack(fill="x" ,pady=5)

root.mainloop()