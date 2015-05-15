from __future__ import with_statement # for Python 2.5 and 2.6
from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
from function import function
from Print import Print
from IfStatement import IfStatement
from ElifStatement import ElifStatement
from ElseStatement import ElseStatement
from dashboard import dashboard
from ForLoop import ForLoop
from Nested import Nested
from Variable import Variable
from WhileLoop import WhileLoop
from Return import Return
from Expression import Expression
from Tab import Tab
from Run import Run
import HelpScreen
import random
import contextlib
import urllib
import os
import tkMessageBox
import tkSimpleDialog
import tkFileDialog
import copy


class runVisualProgrammer(EventBasedAnimationClass):

    def leftMousePressed(self, event):
        x, y = (event.x_root - self.root.winfo_rootx(), 
            event.y_root - self.root.winfo_rooty())
        if(self.whichScreen == "program"):
            self.leftMousePressedProgram(x, y)
            str(self.function[self.functionNum])
        elif(self.whichScreen == "start"):
            self.leftMousePressedStart(x, y)
        elif(self.whichScreen == "help1" or self.whichScreen == "help2"):
            self.leftMousePressedHelp(x, y)

    def leftMousePressedStart(self, x, y):
        if(self.cx-100<=x<=self.cx+100 and self.cy-5<=y<=self.cy+55):
            self.switchScreen("program")
        elif(self.cx-80<=x<=self.cx+80 and self.cy-20+100<=y<=self.cy+20+100):
            self.switchScreen("help1")

    def leftMousePressedHelp(self, x, y):
        self.initStartandSplash()
        if(self.helpScreenPos == 8):
            if(self.cx-100<=x<=self.cx+100 and self.cy+70<=y<=self.cy+130):
                self.switchScreen("program")
        if(50<=x<=200 and 50<=y<=80):
            if(self.whichScreen == "help1"): self.switchScreen("start")
            else: self.switchScreen("program")
        elif(0<=x<=self.backArrow.width() and self.cy-self.backArrow.height()/2
            <=y<=self.cy+self.backArrow.height()/2):
            if(self.helpScreenPos > 0):
                self.helpScreenPos -= 1
        elif(self.width-self.forwardArrow.width()<=x<=self.width and 
            self.cy-self.forwardArrow.height()/2<=y<=
            self.cy+self.forwardArrow.height()/2):
            if(self.helpScreenPos < 8):
                self.helpScreenPos += 1

    def leftMousePressedProgram(self, x, y):
        self.error = ""
        if(self.inRangeTabs(x, y)): return
        obj = self.dashboard.inRange(x, y)
        if(isinstance(obj, Print)):
            self.tmpDrag = Print(x, y)
            self.Draggable = True
        elif(isinstance(obj, ElseStatement)):
            self.tmpDrag = ElseStatement(x, y, do=[])
            self.Draggable = True
        elif(isinstance(obj, ElifStatement)):
            self.tmpDrag = ElifStatement(x, y, do=[])
            self.Draggable = True
        elif(isinstance(obj, IfStatement)):
            self.tmpDrag = IfStatement(x, y, do=[])
            self.Draggable = True
        elif(isinstance(obj, ForLoop)):
            self.tmpDrag = ForLoop(x, y, do=[])
            self.Draggable = True
        elif(isinstance(obj, WhileLoop)):
            self.tmpDrag = WhileLoop(x, y, do=[])
            self.Draggable = True
        elif(isinstance(obj, Variable)):
            self.tmpDrag = Variable(x, y)
            self.Draggable = True
        elif(isinstance(obj, Return)):
            self.tmpDrag = Return(x, y)
            self.Draggable = True
        elif(isinstance(obj, Expression)):
            self.tmpDrag = Expression(x, y)
            self.Draggable = True
        else:
            if(self.highLighted != None):
                self.highLighted.selected = False
            self.tmpDrag = self.function[self.functionNum].inRange(x, y)
            if(self.tmpDrag != None):
                self.highLighted = self.tmpDrag
                self.highLighted.selected = True
                self.Draggable = True

    def leftMouseMoved(self, event):
        x, y = (event.x_root - self.root.winfo_rootx(), 
            event.y_root - self.root.winfo_rooty())
        if(self.whichScreen == "program"):
            if(self.Draggable):
                self.tmpDrag.move(x, y)


    def leftMouseReleased(self, event):
        e = "Wrong placement of Elif and Else Statements."
        if(self.whichScreen == "program"):
            x, y = (event.x_root - self.root.winfo_rootx(), 
                event.y_root - self.root.winfo_rooty())
            if(self.Draggable):
                if(x <= self.funcLine and y >= 85):
                    tmp = self.function[self.functionNum].inRangeWithoutPop(x,y)
                    if(isinstance(tmp, Nested)):
                        tmp.addDo(self.tmpDrag)
                        if(not self.checkElif(tmp)):
                            self.removeElif(tmp)
                            self.error += e
                    else:
                        self.function[self.functionNum].addDo(self.tmpDrag)
                        if(not self.checkElif(self.function[self.functionNum])):
                            self.removeElif(self.function[self.functionNum])
                            self.error += e
                self.tmpDrag, self.Draggable = None, False
                self.function[self.functionNum].processObj()
            tmpString = repr(self.function[self.functionNum])
            fN = self.functionNum
            if(tmpString != self.undoList[fN][self.undoPosList[fN]]):
                self.undoList[fN] = self.undoList[fN][:self.undoPosList[fN]+1]\
                 + [tmpString]
                self.undoPosList[fN] = len(self.undoList[fN])-1
                

    def onTimerFired(self):
        self.redrawAll()
        if(self.whichScreen == "help1" or self.whichScreen == "help2"):
            if(self.helpScreenPos == 3):
                self.timer += 1
                if(self.timer == 230):
                    self.demoVariable = Variable(1050, 200)
                    self.demoIfStatment = IfStatement(1050, 240, do=[])
                    self.demoPrint = Print(880, 210)
                    self.timer = 0
                self.canvas.after(self.timerDelay, self.onTimerFired)
            elif(self.helpScreenPos == 4):
                self.timer += 1
                if(self.timer == 200):
                    self.demoIfStatment2 = IfStatement(1050, 240, do=[])
                    self.demoElifStatment = ElifStatement(1050, 280, do=[])
                    self.timer = 0
                self.canvas.after(self.timerDelay, self.onTimerFired)
            else:
                self.canvas.after(self.timerDelay * 20, self.onTimerFired)

    def removeElif(self, tmp):
        for i in xrange(len(tmp.do)):
            if(tmp.do[i] is self.tmpDrag):
                tmp.do.pop(i)
                return

    def checkElif(self, tmp):
        pos = 0
        while(pos < len(tmp.do)):
            if(type(tmp.do[pos]) == IfStatement):
                pos += 1
                while(pos < len(tmp.do)):
                    if(type(tmp.do[pos]) == ElifStatement):
                        pos += 1
                    elif(type(tmp.do[pos]) == ElseStatement):
                        pos += 1
                        break
                    else:
                        break
            elif(type(tmp.do[pos]) == ElifStatement or 
                type(tmp.do[pos]) == ElseStatement):
                return False
            else:
                pos += 1
        return True

    def inRangeTabs(self, x, y):
        for i in xrange(len(self.tabButtons)):
            if(self.tabButtons[i].inRange(x, y)):
                self.switchFunctions(i)
                return True
        if(len(self.tabButtons) > 1):
            for i in xrange(len(self.tabButtons)):
                if(self.tabButtons[i].inRangeClose(x, y)):
                    self.function.pop(i)
                    self.tabButtons.pop(i)
                    self.undoList.pop(i)
                    self.undoPosList.pop(i)
                    if(i == self.functionNum):
                        if (i <= len(self.tabButtons) - 1):
                            self.switchFunctions(self.functionNum)
                        else:
                            self.functionNum = self.functionNum - 1
                            self.tabButtons[self.functionNum].selected = True
                    else:
                        if(i < self.functionNum):
                            self.functionNum = self.functionNum - 1
                        else:
                            self.functionNum = self.functionNum
                    self.processTabs()
                    return True
        return False

    def processTabs(self):
        x = 40
        for i in xrange(len(self.tabButtons)):
            self.tabButtons[i].setXY(x, self.tabButtons[i].y)
            x += 70

    def convertToPython(self):
        self.dashboard.displayCode(str(self.function[self.functionNum]))
        for i in xrange(len(self.tabButtons)):
            self.tabButtons[i].setName(self.function[i].funcName)
        self.runFunction.config(state='normal')

    def convertAllToPython(self):
        tmpString = ""
        for i in xrange(len(self.function)):
            tmpString += str(self.function[i]) + "\n"
        self.dashboard.displayCode(tmpString)
        for i in xrange(len(self.tabButtons)):
            self.tabButtons[i].setName(self.function[i].funcName)
        self.runFunction.config(state='normal')

    def runPython(self):
        code = self.dashboard.st.get("1.0",END)
        try:
            exec(code)
            Run(400, 500, code).run()
        except:
            self.error = "The code you have written is not in the right format."


    def switchScreen(self, screen):
        self.helpScreenPos = 0
        if(screen == "program"):
            self.initMenu()       
        elif(screen == "help2"):
            self.menu.entryconfig("File", state="disabled")
            self.menu.entryconfig("Help", state="disabled")
        self.whichScreen = screen
        if(screen == "help1" or screen == "help2"):
            self.onTimerFired()
        self.redrawAll()

    def switchFunctions(self, pos):
        self.tabButtons[self.functionNum].selected = False
        self.functionNum = pos
        self.tabButtons[self.functionNum].selected = True

    def newFunction(self):
        if(len(self.tabButtons) <= 10 and self.whichScreen == "program"):
            self.function.append(function(name="func"+str(self.count), do=[]))
            self.count += 1
            if len(self.tabButtons) != 0:
                x, y = (self.tabButtons[-1].x + 70, self.tabButtons[-1].y) 
            else:
                x, y = (40, 60)
            self.tabButtons.append(Tab(x, y, self.function[-1].funcName))
            self.switchFunctions(len(self.function) - 1)
            self.undoList.append(["function(name='func',param=[],do=[])"])
            self.undoPosList.append(0)
        self.redrawAll()


    def saveFunction(self):
        if(self.whichScreen == "program"):
            f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:
                return
            text = repr(self.function[self.functionNum])
            f.write(text)
            f.close()
        self.redrawAll()
            
    def openFunction(self):
        if(len(self.tabButtons) <= 10 and self.whichScreen == "program"):
            ftypes = [('Text Files', '*.txt')]
            dlg = tkFileDialog.Open(filetypes = ftypes)
            fl = dlg.show()
            if fl != '':
                text = self.readFile(fl)
                try:
                    func = eval(eval(repr(text)))
                    self.function.append(func)
                    self.count += 1
                    if len(self.tabButtons) != 0:
                        x, y=(self.tabButtons[-1].x + 70,self.tabButtons[-1].y) 
                    else:
                        x, y = (40, 60)
                    self.tabButtons.append(Tab(x,y,self.function[-1].funcName))
                    self.switchFunctions(len(self.function) - 1)
                    self.undoList.append([text])
                    self.undoPosList.append(0)
                except:
                    self.error = "Wrong file format to open."
        self.redrawAll()
        return None

    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text
            
    def drawDashboard(self):
        canvas = self.canvas
        canvas.create_image(0, 0, anchor="nw", image=self.background)
        canvas.create_line(self.funcLine, 0, self.funcLine, self.height, 
            width=4, fill="gray")
        canvas.create_window(800, 290, window=self.convertButton, anchor="w")
        canvas.create_window(1000, 290,window=self.convertAllButton,anchor="w")
        canvas.create_window(1200, 290, window=self.runFunction, anchor="w")
        self.dashboard.draw(canvas)

    def drawFunction(self):
        self.function[self.functionNum].draw(self.canvas)

    def drawDrag(self):
        if(self.tmpDrag != None):
            self.tmpDrag.draw(self.canvas)

    def drawError(self):
        canvas = self.canvas
        canvas.create_text(self.funcLine/2, self.height-30, text=self.error, 
            font="Arial 12 bold", fill="red")

    def drawProgram(self):
        canvas = self.canvas
        canvas.create_text(self.funcLine/2, 15, text="Workspace", 
            font="Arial 18 bold")
        self.drawError()
        for i in xrange(len(self.tabButtons)):
            self.tabButtons[i].draw(canvas)


    def drawStart(self):
        canvas = self.canvas
        canvas.create_image(0, 0, anchor="nw", image=self.startBackground)
        canvas.create_text(self.cx, self.cy-200, text="Visual Programming", 
            font="Arial 35 bold", fill="blue")
        canvas.create_text(self.cx, self.cy-150, text="Language", 
            font="Arial 35 bold", fill="blue")
        canvas.create_text(self.cx, self.cy-75, text="by: Richard Huang", 
            font="Arial 20 bold", fill="black")
        buttonW, buttonH = 100, 30
        canvas.create_rectangle(self.cx-buttonW, self.cy-buttonH+25, 
            self.cx+buttonW, self.cy+buttonH+25, fill="green")
        canvas.create_text(self.cx, self.cy+25, text="Start Programming!", 
            font="Arial 15 bold")
        buttonW, buttonH = 80, 20
        canvas.create_rectangle(self.cx-buttonW, self.cy-buttonH+100, 
            self.cx+buttonW, self.cy+buttonH+100, fill="red")
        canvas.create_text(self.cx, self.cy+100, text="Tutorial", 
            font="Arial 12 bold")

    def redrawAll(self):
        canvas = self.canvas
        canvas.delete(ALL)
        if(self.whichScreen == "start"):
            self.drawStart()
        elif(self.whichScreen == "program"):
            self.drawDashboard()
            self.drawFunction()
            self.drawDrag()
            self.drawProgram()
        elif(self.whichScreen == "help1" or self.whichScreen == "help2"):
            HelpScreen.drawHelp(self)

    def initDashBoard(self):
        dashPrint = Print(self.width - 8*self.size, 60)
        dashForLoop = ForLoop(self.width - 8*self.size, 115)
        dashWhileLoop = WhileLoop(self.width - 8*self.size,170)
        dashExpression = Expression(self.width - 8*self.size,215)
        dashReturn = Return((self.funcLine+self.width)/2,250)

        dashVariable = Variable(self.width - 3*self.size, 50)
        dashIfStatement = IfStatement(self.width - 3*self.size, 95)
        dashElifStatement = ElifStatement(self.width - 3*self.size, 150)
        dashElseStatement = ElseStatement(self.width - 3*self.size, 205)
        self.dashboard = dashboard(self.width, self.height)

        self.dashboard.addLabel(dashPrint)
        self.dashboard.addLabel(dashIfStatement)
        self.dashboard.addLabel(dashElifStatement)
        self.dashboard.addLabel(dashForLoop)
        self.dashboard.addLabel(dashVariable)
        self.dashboard.addLabel(dashWhileLoop)
        self.dashboard.addLabel(dashReturn)
        self.dashboard.addLabel(dashElseStatement)
        self.dashboard.addLabel(dashExpression)

    def initMenu(self):
        self.menu = Menu(self.root)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu2 = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="New", command=self.newFunction)
        self.filemenu.add_command(label="Open", command=self.openFunction)
        self.filemenu.add_command(label="Save", command=self.saveFunction)
        self.filemenu2.add_command(label="Help", 
            command=(lambda:self.switchScreen("help2")))
        

        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.menu.add_cascade(label="Help", menu=self.filemenu2)
        self.root.config(menu=self.menu)

    def initStartandSplash(self):
        self.startBackground = PhotoImage(file="pics\start_background.gif")
        self.background = PhotoImage(file="pics\\background.gif")
        self.backArrow = PhotoImage(file="pics\\back_arrow.gif")
        self.backArrow = self.backArrow.subsample(2,2)
        self.forwardArrow = PhotoImage(file="pics\\forward_arrow.gif")
        self.forwardArrow = self.forwardArrow.subsample(2,2)
        self.programScreenShot = PhotoImage(file="pics\\program_screenshot.gif")
        self.programScreenShot2=PhotoImage(file="pics\\program_screenshot2.gif")
        self.programScreenShot3=PhotoImage(file="pics\\program_screenshot3.gif")
        self.programScreenShot4=PhotoImage(file="pics\\program_screenshot4.gif")
        self.programScreenShot5=PhotoImage(file="pics\\program_screenshot5.gif")
        self.demoVariable = Variable(1050, 200)
        self.demoIfStatment = IfStatement(1050, 240, do=[])
        self.demoIfStatment2 = IfStatement(1050, 240, do=[])
        self.demoElifStatment = ElifStatement(1050, 280)
        self.demoPrint = Print(880, 210)
        self.timer = 0

    def undo(self):
        fN = self.functionNum
        if(self.undoPosList[fN] > 0):
            self.undoPosList[fN] -= 1
            self.function[fN] = eval(self.undoList[fN][self.undoPosList[fN]])
        self.redrawAll()

    def redo(self):
        fN = self.functionNum
        if(self.undoPosList[fN] < len(self.undoList[fN]) - 1):
            self.undoPosList[fN] += 1
            self.function[fN] = eval(self.undoList[fN][self.undoPosList[fN]])
        self.redrawAll()


    def initAnimation(self):
        self.x = -1
        self.y = -1
        self.size = 50
        self.root.title("Visual Programming Language")
        self.error = ""
        self.count = 1
        self.cx, self.cy = self.width/2, self.height/2
        self.funcLine = self.cx + 100
        self.functionNum = 0
        self.function = [function(do=[])]
        self.undoList = [["function(name='func',param=[],do=[])"]]
        self.undoPosList = [0]
        self.Draggable = False
        self.tmpDrag = None
        self.initDashBoard()
        self.highLighted = None
        self.whichScreen = "start"
        self.convertButton = Button(self.canvas, text="Convert to Python", 
            command=self.convertToPython)
        self.convertAllButton = Button(self.canvas, 
            text="Convert All to Python", command=self.convertAllToPython)
        self.runFunction = Button(self.canvas, text="Run Python Code", 
            command=self.runPython, state=DISABLED)



        self.tabButtons = [Tab(40,40, self.function[0].funcName)]
        self.tabButtons[0].selected = True

        self.initStartandSplash()
        self.helpScreenPos = 0
        self.root.bind('<Control-n>', (lambda x:self.newFunction()))
        self.root.bind('<Control-o>', (lambda x:self.openFunction()))
        self.root.bind('<Control-s>', (lambda x:self.saveFunction()))
        self.root.bind('<Control-z>', (lambda x:self.undo()))
        self.root.bind('<Control-y>', (lambda x:self.redo()))

        
rvp = runVisualProgrammer(1360, 700)
rvp.run()