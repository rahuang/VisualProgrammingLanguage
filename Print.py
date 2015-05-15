import string
import re
from Tkinter import *

class Print(object):
    def __init__(self, x, y, printText=""):
        self.x, self.y = x, y
        self.width = 100
        self.height = 25
        self.printText = printText
        self.tmpText = ""
        self.depth = 0
        self.selected = False
        v1 = StringVar()
        self.textInput = Entry(width=31,textvariable=v1,xscrollcommand=True)
        v1.set(self.printText)

    def move(self, x, y):
        self.x, self.y = x, y

    def setText(self, text):
        self.printText = text

    def draw(self, canvas):
        outlineColor = "black"
        if(self.selected):
            outlineColor = "red"
        canvas.create_rectangle(self.x-self.width,self.y-self.height, self.x+self.width, self.y+self.height, fill="PaleGreen", outline=outlineColor)
        canvas.create_text(self.x-self.width+5, self.y-self.height+5, text="Print Box", anchor="nw", font="Arial 10 bold")
        canvas.create_window(self.x-self.width+5, self.y-self.height+25, window=self.textInput, anchor="nw")
        canvas.create_line(self.x-self.width, self.y-self.height+20, self.x+self.width, self.y-self.height+20, width="1")

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

    def process(self):
        for i in xrange(len(self.printText)):
            if(self.printText[i] == "\""):
                self.tmpText += "\\"
            elif(self.printText[i] == "\\"):
                if(i < len(self.printText) - 1 and self.printText[i + 1] in string.ascii_lowercase):
                    pass
                else:
                    pass
                
                self.tmpText += "\\"
                
            self.tmpText += self.printText[i]

        while("var(" in self.tmpText):
            try:
                m = re.search("var\(([A-Za-z0-9_$&+,:;=?@#|'<>.^*()%!-\\\/]+)\)", self.tmpText)
                self.tmpText = self.tmpText.replace(m.group(0), "\" + str(" + m.group(1) + ") + \"")
            except:
                pass

    def __repr__(self):
        string = "Print(x=" + repr(self.x) + ",y=" + repr(self.y) + ",printText=" + repr(self.printText) + ")"
        return string

    def __str__(self):
        self.printText = self.textInput.get()
        self.process()
        s ="print " + "\"" + self.tmpText + "\""
        self.tmpText = ""
        return s