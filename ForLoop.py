import string
from Nested import Nested
from Tkinter import *

class ForLoop(Nested):
    def __init__(self, x, y, forRange=["", "", ""], do=[], width=120, height=25):
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.range = forRange
        self.selectedRange = None
        self.do = do
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.varInput = Entry(width=4,textvariable=v1)
        v1.set(self.range[0])
        v2 = StringVar()
        self.startInput = Entry(width=4,textvariable=v2)
        v2.set(self.range[1])
        v3 = StringVar()
        self.endInput = Entry(width=4,textvariable=v3)
        v3.set(self.range[2])
            
    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        #text = "loop from: " + self.range[0] + " to: " + self.range[1] + " (inclusive)"
        text = "loop variable:        from:         to: "
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="gold", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text=text, anchor="nw", font="Arial 10 bold")

        canvas.create_window(self.x-self.width+95, self.y-self.height+1, window=self.varInput, anchor="nw")
        canvas.create_window(self.x-self.width+160, self.y-self.height+1, window=self.startInput, anchor="nw")
        canvas.create_window(self.x-self.width+210, self.y-self.height+1, window=self.endInput, anchor="nw")

        canvas.create_line(self.x-self.width, self.y-self.height+20, self.x+self.width, self.y-self.height+20, width="1")
        canvas.create_text(self.x-self.width+5, self.y-self.height+25, text="do", anchor="nw", font="Arial 10 bold")
        for i in xrange(len(self.do)):
            self.do[i].draw(canvas)

    def __repr__(self):
        string = "ForLoop(x=" + repr(self.x) + ",y=" + repr(self.y) + ",forRange=" + repr(self.range) 
        string += ",do=" + repr(self.do) + ",width=" + repr(self.width) + ",height=" + repr(self.height) + ")"
        return string

    def __str__(self):
        self.range = [self.varInput.get(), self.startInput.get(), self.endInput.get()]
        s = "for " + str(self.range[0]) + " in xrange(" + str(self.range[1]) + ", " 
        s += self.range[2] + "+1):\n"
        for i in xrange(len(self.do)):
            self.do[i].depth = self.depth + 1
            s += self.depth*"    " +str(self.do[i])
            s += "\n" if i != len(self.do) - 1 else ""
        return s