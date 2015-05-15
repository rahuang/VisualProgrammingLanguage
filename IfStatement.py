import string
from Nested import Nested
from Tkinter import *


class IfStatement(Nested):
    def __init__(self, x, y, condition="", do=[], width=100, height=25):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.condition = condition
        self.do = do
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.conditionInput = Entry(width=28,textvariable=v1)
        v1.set(self.condition)

    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="CadetBlue1", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text="if: ", anchor="nw", font="Arial 10 bold")
        canvas.create_window(self.x-self.width+25, self.y-self.height+1, window=self.conditionInput, anchor="nw")
        canvas.create_line(self.x-self.width, self.y-self.height+20, self.x+self.width, self.y-self.height+20, width="1")
        canvas.create_text(self.x-self.width+5, self.y-self.height+25, text="do", anchor="nw", font="Arial 10 bold")
        for i in xrange(len(self.do)):
            self.do[i].draw(canvas)

    def __repr__(self):
        string = "IfStatement(x=" + repr(self.x) + ",y=" + repr(self.y) + ",condition=" + repr(self.condition) 
        string += ",do=" + repr(self.do) + ",width=" + repr(self.width) + ",height=" + repr(self.height) + ")"
        return string

    def __str__(self):
        self.condition = self.conditionInput.get()
        s = "if (" + self.condition + "):\n"
        for i in xrange(len(self.do)):
            self.do[i].depth = self.depth + 1
            s += self.depth*"    " +str(self.do[i])
            s += "\n" if (i != len(self.do) - 1) else ""
        return s