from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
from ScrolledText import *
import sys
from StringIO import StringIO


class Run(object):
    def __init__(self, width=400, height=500, code=""):
        self.width = width
        self.height = height
        self.code = code
        self.error = ""

    def redrawAll(self):
        canvas = self.canvas
        canvas.delete(ALL)
        canvas.create_image(0, 0, image=self.background2, anchor="nw")
        canvas.create_text(10, 10, text="Enter the function name: ", anchor="nw")
        canvas.create_window(150, 10, window=self.functionRun, anchor="nw")
        canvas.create_text(10, 30, text="Enter the function parameters: ", anchor="nw")
        canvas.create_window(175, 30, window=self.functionRunParam, anchor="nw")
        canvas.create_window(10, 70, window=self.run, anchor="w")
        canvas.create_text(10, 100, text="Print Output:", anchor="w", font="Arial 10 bold")
        canvas.create_window(0, 110, window=self.printDisplay, anchor="nw")
        canvas.create_text(10, 300, text="Return Output:", anchor="w", font="Arial 10 bold")
        canvas.create_window(0, 310, window=self.returnDisplay, anchor="nw")
        canvas.create_text(10, self.height-10, text=self.error, anchor="w", font="Arial 14 bold", fill="red")
        

    def runProgram(self):
        self.error = ""
        g = {}
        name = self.functionRun.get()
        param = self.functionRunParam.get()
        buffer = StringIO()
        sys.stdout = buffer
        exec(self.code + "\nprint factorial(5)", g)
        #print eval(name + "(" + param + ")")

        '''if(name == ""):
            self.error = "Wrong function call."
            self.redrawAll()
            return'''
        try:

            #result = eval(name + "(" + param + ")")
            #result = eval()
            sys.stdout = sys.__stdout__

            self.printDisplay.delete("1.0",END)
            self.printDisplay.insert(INSERT, buffer.getvalue())
            self.returnDisplay.delete("1.0",END)
            #self.returnDisplay.insert(INSERT, str(result))
        except:
            self.error = "Wrong function call."
            self.redrawAll()



    def initAnimation(self):
        self.functionRun = Entry(master=self.root, width=31)
        self.functionRunParam = Entry(master=self.root, width=31)
        self.background2 = PhotoImage(master=self.canvas, file="pics\\background.gif")
        self.printDisplay = ScrolledText(master=self.root, width=47, height=11)
        self.returnDisplay = ScrolledText(master=self.root, width=47, height=10)
        self.run = Button(master=self.canvas, text="Run Function", command=self.runProgram)

    def run(self):
        # create the root and the canvas
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.initAnimation()

        self.redrawAll()
        
        self.root.mainloop()

