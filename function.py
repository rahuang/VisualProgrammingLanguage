from Tkinter import *
from Print import Print
from IfStatement import IfStatement
from ForLoop import ForLoop
from Variable import Variable
from WhileLoop import WhileLoop
from Return import Return
from Expression import Expression


class function(object):
    def __init__(self, name="func", param=[], do=[], width=1360):
        self.param = param
        self.do = do
        self.funcName = name
        self.depth = 1
        self.width = width
        self.nameInput = StringVar()
        self.functionNameInput = Entry(width=10, textvariable=self.nameInput)
        self.nameInput.set(self.funcName)

        self.paramInput = StringVar()
        self.functionParamInput = Entry(width=10, textvariable=self.paramInput)
        tmpString = ""
        for i in xrange(len(self.param)):
            tmpString += self.param[i]
            if(i < len(self.param)-1):
                 tmpString += ", "
        self.paramInput.set(tmpString)
        self.notepadBackground = PhotoImage(file="pics\\notepad.gif")


    def setName(self):
        self.funcName = self.functionNameInput.get()

    def setParams(self):
        if(self.functionParamInput.get() == ""):
            self.param = ""
        else:
            self.param = self.functionParamInput.get().split(",")

    def addDo(self, obj):
        self.do.append(obj)
        self.do.sort(key=lambda obj: obj.y)
        #print self.do

    def processObj(self):
        for i in xrange(len(self.do)):
            try:
                self.do[i].processObj()
            except:
                pass

    def draw(self, canvas):
        canvas.create_image(0, 85, image=self.notepadBackground, anchor="nw")
        canvas.create_text(10, 70, text="Enter function name: ", font="Arial 12", anchor="w")
        canvas.create_window(160, 70, window=self.functionNameInput, anchor="w")
        canvas.create_text(230, 70, text="Enter function params: ", font="Arial 12", anchor="w")
        canvas.create_window(390, 70, window=self.functionParamInput, anchor="w")
        canvas.create_line(0, 85, self.width/2+100, 85, width=4, fill="gray")
        if(self.do != []):
            for i in xrange(len(self.do)):
                statement = self.do[i]
                statement.draw(canvas)

    def inRange(self, x, y):
        for i in xrange(len(self.do)-1, -1, -1):
            tmp = self.do[i].inRange(x, y)
            if(tmp != None):
                if(self.do[i] is tmp and isinstance(self.do[i], IfStatement)):
                    self.do.pop(i)
                elif(self.do[i] is tmp and isinstance(self.do[i], ForLoop)):
                    self.do.pop(i)
                elif(self.do[i] is tmp and isinstance(self.do[i], WhileLoop)):
                    self.do.pop(i)
                elif(isinstance(self.do[i], Print)):
                    self.do.pop(i)
                elif(isinstance(self.do[i], Variable)):
                    self.do.pop(i)
                elif(isinstance(self.do[i], Return)):
                    self.do.pop(i)
                elif(isinstance(self.do[i], Expression)):
                    self.do.pop(i)
                return tmp
        return None

    def inRangeWithoutPop(self, x, y):
        for i in xrange(len(self.do)-1, -1, -1):
            tmp = self.do[i].inRangeWithoutPop(x, y)
            if(tmp != None):
                return tmp
        return None

    def __repr__(self):
        string = "function("
        string += "name=" + repr(self.funcName) + ","
        string += "param=" + repr(self.param) + ","
        string += "do=" + repr(self.do)
        string += ")"
        return string

    def __str__(self):
        self.setName()
        self.setParams()
        string = "def "
        params = ""
        if(len(self.param) > 0):
            for i in xrange(len(self.param)):
                params += self.param[i].strip() + ", " if i != len(self.param)-1 else self.param[i].strip()

        string += self.funcName + "(" + params + "):\n"
        for i in xrange(len(self.do)):
            self.do[i].depth = self.depth + 1
            string += self.depth*"    " +str(self.do[i]) + "\n"
        return string
