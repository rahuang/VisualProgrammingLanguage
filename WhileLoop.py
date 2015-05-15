import string
from Nested import Nested
from Tkinter import *

class WhileLoop(Nested):
    def __init__(self, x, y, condition="", do=[], width=100, height=25):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.condition = condition
        self.selectedRange = None
        self.do = do
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.conditionInput = Entry(width=19,textvariable=v1)
        v1.set(self.condition)
            
    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        #text = "loop from: " + self.range[0] + " to: " + self.range[1] + " (inclusive)"
        text = "loop while: "
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="LightGoldenrod1", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text=text, anchor="nw", font="Arial 10 bold")

        canvas.create_window(self.x-self.width+80, self.y-self.height+1, window=self.conditionInput, anchor="nw")

        canvas.create_line(self.x-self.width, self.y-self.height+20, self.x+self.width, self.y-self.height+20, width="1")
        canvas.create_text(self.x-self.width+5, self.y-self.height+25, text="do", anchor="nw", font="Arial 10 bold")
        for i in xrange(len(self.do)):
            self.do[i].draw(canvas)

    def __repr__(self):
        string = "WhileLoop(x=" + repr(self.x) + ",y=" + repr(self.y) + ",condition=" + repr(self.condition) 
        string += ",do=" + repr(self.do) + ",width=" + repr(self.width) + ",height=" + repr(self.height) + ")"
        return string

    def __str__(self):
        self.condition = self.conditionInput.get()
        self.condition = self.condition.replace("=", "==")
        s = "while(" + str(self.condition) + "):\n"
        for i in xrange(len(self.do)):
            self.do[i].depth = self.depth + 1
            s += self.depth*"    " +str(self.do[i])
            s += "\n" if i != len(self.do) - 1 else ""
        return s