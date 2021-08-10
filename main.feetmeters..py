#https://tkdocs.com/tutorial/firstexample.html
from tkinter import *
from tkinter import ttk  #this is for themed widgets more modern than older ones and support styles

def calculate(*args):
    '''
    function to calculate the meters from feet - uses * 10000 +0.5 to remove any floating pt nonsense:
    '''
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        print("error! only put in valid numbers ")
        pass


root = Tk() #start Tkinter
root.title("Feet to Meters") #window title
# https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame
# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
s.configure('TFrame', background='green')

mainframe = ttk.Frame(root, padding="0 3 12 12")
mainframe.grid(column=0, row=0)
# The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar() #flexible string type that auto updates
feet_entry = ttk.Entry(mainframe, width=17, textvariable=feet)
feet_entry.grid(column=2, row=1) #where to put it on the screen - note it is NOT zero indexed

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E)) # sticky will stick the label to the WEST and EAST

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3) # command tells TKinter what function to run

ttk.Label(mainframe, text="feet", relief="groove").grid(column=3, row=1)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
ttk.Label(mainframe, text="meters").grid(column=3, row=2)

for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15) # just adds padding between the widgets

feet_entry.focus() # put cursor in the entry box
root.bind("<Return>", calculate) # bind pressing Return to the calculate function

root.mainloop()