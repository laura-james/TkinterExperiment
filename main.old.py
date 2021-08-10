import tkinter as tk
window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="magenta",  # Set the background color to black
    width=100,
    height=10
)
label.pack()
def btnthing():
    label["text"] = "button clicked you said " + entry.get()

button = tk.Button(
    text="Click me!",
    width=25,
    height=15,
    bg="blue",
    fg="yellow",
    command = btnthing
)
button.pack()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


def handle_click(event):
    print("The anything was clicked!"+entry.get())
    label["text"] = "you said " +  entry.get()

#button.bind("<Button-1>", handle_click) #burron-1 means left mouse btn
window.mainloop()