import string
import re
from Tkinter import *

class Return(object):
    def __init__(self, x, y, returnText=""):
        self.x, self.y = x, y
        self.width = 100
        self.height = 13
        self.returnText = returnText
        self.tmpText = ""
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.textInput = Entry(width=23,textvariable=v1,xscrollcommand=True)
        #self.textInput.configure(state="disabled")
        v1.set(self.returnText)

    def move(self, x, y):
        self.x, self.y = x, y

    def setText(self, text):
        self.returnText = text

    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="blue", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text="Return: ", anchor="nw", font="Arial 10 bold")
        canvas.create_window(self.x-self.width+55, self.y-self.height+3, window=self.textInput, anchor="nw")

    def inRange(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<y<self.y+self.height):
            return self
        else:
            return None

    def inRangeWithoutPop(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<y<self.y+self.height):
            return self
        else:
            return None


    def __repr__(self):
        string = "Return(x=" + repr(self.x) + ",y=" + repr(self.y) + ",returnText=" + repr(self.returnText) + ")"
        return string

    def __str__(self):
        self.returnText = self.textInput.get()
        s ="return " + self.returnText
        return s