#Name:Abhishek Jasiwal
#github@User_ID : abhishek-iiit

try:
    from tkinter import *
except ImportError:
    from tkinter import *
import time
from powgenfunction import RandPass

# Defining Function
def pwGenerator(size=8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]
    PASSWORD.set(new_password)
    strength_label.configure(foreground="white", background=pw_color, text=pw_strength, font=('arial', 10, 'bold'), bd=10, height=1, width=10)
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(.02)
    gui.update()
    gui.mainloop()


# GUI Section
gui = Tk()
gui.title("Password Generator by Abhishek Jaiswal")
width = 600
height = 200
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
gui.geometry("%dx%d+%d+%d" % (width, height, x, y))

PASSWORD = StringVar()
PW_SIZE = IntVar()
e1 = Entry(gui, text=PW_SIZE)
PW_SIZE.set(8)

# Size of the Frame
Top = Frame(gui, width=width)
Top.pack(side=TOP)
Form = Frame(gui, width=width)
Form.pack(side=TOP)
Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

# Labeling the box
title_label = Label(Top, width=width, font=('arial', 12, 'bold'),text="Select your Password Length ,then Click Generate Now", bd=1, relief=SOLID)
title_label.pack(fill=X)
password_label = Label(Form, font=('arial', 15), text="Password", bd=10)
password_label.grid(row=0, pady=10)
strength_label = Label(Form, font=('arial', 12, 'bold'), foreground="white",background="#6d0001", text="Weak", bd=10, height=1, width=10)
strength_label.grid(row=0, column=3, pady=10, padx=10)
lbl_pw_size = Label(Form, font=('arial', 15), text="Size", bd=10)
lbl_pw_size.grid(row=1, pady=10)
instr_label = Label(Bot, width=width, font=('arial', 12, 'bold'),text="Copy your result from Clipboard.", bd=1, relief=SOLID)
instr_label.pack(fill=X)

# Widget
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)
pw_size = Scale(Form, from_=8, to=24, length=230, width=24,sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, font=(18))
pw_size.grid(row=1, column=1, columnspan=2)

btn_generate = Button(Form, text="Generate Now", width=20,command=lambda: pwGenerator(PW_SIZE))
btn_generate.grid(row=2, column=1, columnspan=2)

# Calling the function
gui.mainloop()
