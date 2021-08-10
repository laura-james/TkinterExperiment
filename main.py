from tkinter import *
from tkinter import ttk  #this is for themed widgets more modern than older ones and support styles
import random
def generateElfName(*args):

    names = ["sneezy","dopey","happy","dozy","grumpy","grumpy","arnold schwarznegger"]
    fname = firstname.get()
    lname = lastname.get()
    elfname.set( fname + " " + lname + " your elfname is " + random.choice(names) )

root = Tk() #start Tkinter
root.title("Get your Elf Name!") #window title
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
# The columnconfigure/rowconfigure bits tell Tk that the frame should expand
# # to fill any extra space if the window is resized.
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Initialize style
s = ttk.Style()
# Create style used by default for all Frames
#s.configure('TFrame', background='green')
s.configure('TLabel', background='green', font='Century 22')
s.configure('TButton', background='magenta', font='Century 22')
s.configure('TEntry', background='magenta', font='Century 22') #doesnt work

ttk.Label(mainframe, text="Enter First Name").grid(column=1, row=1)
ttk.Label(mainframe, text="Enter Last Name").grid(column=1, row=2)
firstname = StringVar() #flexible string type that auto updates
firstname_entry = ttk.Entry(mainframe, width=17, textvariable=firstname,font='Century', 22, 'bold')
firstname_entry.grid(column=2, row=1) # where to put it on the screen - note it is NOT zero indexed
lastname = StringVar() #flexible string type that auto updates
lastname_entry = ttk.Entry(mainframe, width=17, textvariable=lastname)
lastname_entry.grid(column=2, row=2) # where to put it on the screen - note it is NOT zero indexed
ttk.Button(mainframe, text="Generate Elf Name",command=generateElfName).grid(column=2, row=3) # command tells TKinter what function to run
elfname = StringVar()
ttk.Label(mainframe, textvariable=elfname,font=('Century 22'),width=50).grid(column=0, row=4, columnspan=3, sticky=(W,E)) # sticky will stick the label to the WEST and EAST

root.mainloop()
