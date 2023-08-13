import tkinter as tk

def change_color(color):
    canvas.itemconfig(circle, fill=color)

# Create the main window
root = tk.Tk()
root.title("Circle Color Changer")

# Create a canvas to draw on
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw a circle on the canvas
circle = canvas.create_oval(150, 150, 250, 250, fill='red')

# Create buttons to change the circle color
red_button = tk.Button(root, text="Red", command=lambda: change_color('red'))
blue_button = tk.Button(root, text="Blue", command=lambda: change_color('blue'))

# Place buttons on the window
red_button.pack()
blue_button.pack()

# Start the GUI event loop
root.mainloop()
