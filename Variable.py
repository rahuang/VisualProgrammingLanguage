import string
from Tkinter import *

class Variable(object):
    def __init__(self, x, y, nameVal=["", ""]):
        self.x, self.y = x, y
        self.width = 100
        self.height = 15
        self.nameVal = nameVal
        self.nameValSelected = None
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.nameInput = Entry(width=10,textvariable=v1)
        v1.set(self.nameVal[0])
        v2 = StringVar()
        self.valueInput = Entry(width=13,textvariable=v2)
        v2.set(self.nameVal[1])

    def move(self, x, y):
        self.x, self.y = x, y

    def setText(self, text):
        self.printText = text

    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="pink", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text="set\t         to ", anchor="nw", font="Arial 10 bold")

        canvas.create_window(self.x-self.width+30, self.y-self.height+5, window=self.nameInput, anchor="nw")

        canvas.create_window(self.x-self.width+110, self.y-self.height+5, window=self.valueInput, anchor="nw")


    def inRange(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<=y<=self.y+self.height):
            return self
        else:
            return None

    def inRangeWithoutPop(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<=y<=self.y+self.height):
            return self
        else:
            return None

    def __repr__(self):
        string = "Variable(x=" + repr(self.x) + ",y=" + repr(self.y) + ",nameVal=" + repr(self.nameVal) + ")"
        return string

    def __str__(self):
        self.nameVal = [self.nameInput.get(), self.valueInput.get()]
        return str(self.nameVal[0]) + " = " + str(self.nameVal[1])