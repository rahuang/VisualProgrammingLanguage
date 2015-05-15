import string
import re
from Tkinter import *

class Expression(object):
    def __init__(self, x, y, expText=""):
        self.x, self.y = x, y
        self.width = 100
        self.height = 13
        self.expText = expText
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.textInput = Entry(width=30,textvariable=v1,xscrollcommand=True)
        v1.set(self.expText)

    def move(self, x, y):
        self.x, self.y = x, y

    def setText(self, text):
        self.returnText = text

    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="purple", outline=outlineColor)
        canvas.create_window(self.x-self.width+10, self.y-self.height+3, window=self.textInput, anchor="nw")

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
        string = "Expression(x=" + repr(self.x) + ",y=" + repr(self.y) + ",expText=" + repr(self.expText) + ")"
        return string

    def __str__(self):
        self.expText = self.textInput.get()
        s = self.expText
        return s