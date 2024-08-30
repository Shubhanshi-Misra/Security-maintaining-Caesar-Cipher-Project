from tkinter import *
from tkinter import messagebox
import base64
import os

def main_screen():
    screen = TK()
    screen.geometry("pip375x398")

    #icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False,image_icon)
    screen.title("PctApp")

    Label()
    screen.mainloop()



