from Tkinter import *
from ScrolledText import *

class dashboard(object):
    def __init__(self, width, height):
        self.labels = []
        self.convertedCode = ""
        self.st = ScrolledText(width=70, height=21)
        self.st.pack(side=RIGHT)
        self.code = ""
        self.width = width
        self.height = height
        self.cx, self.cy = self.width/2, self.height/2
        self.funcLine = self.cx + 100

    def displayCode(self, code):
        self.code = code
        self.st.delete("1.0",END)
        self.st.insert(INSERT, code)
        

    def inRange(self, x, y):
        for i in xrange(len(self.labels)):
            obj = self.labels[i].inRange(x, y)
            if(obj != None):
                return obj
        return None

    def addLabel(self, obj):
        self.labels.append(obj)

    def draw(self, canvas):
        canvas.create_text((self.width+self.funcLine)/2, 20, text="Dashboard", font="Arial 18 bold")
        canvas.create_line(self.funcLine, 310, self.width, 310, width=4, fill="gray")
        canvas.create_text((self.width+self.funcLine)/2, 330, text="Python Code Translation", font="Arial 14 bold")

        canvas.create_window(self.funcLine, 345, window=self.st, anchor="nw")
        for i in xrange(len(self.labels)):
            self.labels[i].draw(canvas)

    def setConvertCode(self, code):
        self.convertedCode = code

