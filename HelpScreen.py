from Tkinter import *
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

def drawHelp(self):
    canvas = self.canvas
    canvas.create_image(0, 0, anchor="nw", image=self.background)
    canvas.create_rectangle(50, 50, 220, 80, fill="blue")
    if(self.whichScreen == "help1"):
        canvas.create_text(135, 65, text="Back to Home", font="Arial 14 bold")
    else:
        canvas.create_text(135, 65, text="Back to Program", font="Arial 14 bold")
    if(self.helpScreenPos == 0):
        canvas.create_text(self.cx, self.cy-300, text="Help", font="Arial 30 bold", fill="blue")
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "Hello, welcome to the Visual Programming Language!\n\n"
        string += "This program will help you learn how to program, by using visual blocks.\n\n"
        string += "You will be able to program simple functions by dragging and dropping differnt command blocks.\n\n"
        string += "This will allow you to program without worrying about annoying syntax.\n\n"
        string += "You can also convert your visual program back into python code!\n\n\n"
        string += "After finishing this tutorial, you'll be able to make your own program in no time!"
        canvas.create_text(self.cx, self.cy, text=string, font="Arial 14 bold", justify="center")
    elif(self.helpScreenPos == 1):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 2)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "This is what the program looks like. You will learn what each section does.\n"
        canvas.create_text(self.cx, self.cy-100, text=string, font="Arial 14 bold", justify="center")
        canvas.create_image(self.cx, self.cy+100, image=self.programScreenShot)
    elif(self.helpScreenPos == 2):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 3)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "First let's talk about the Dashboard.\n"
        string += "You will find all your visual command blocks here.\n"
        string += "Here is what each block does:"
        canvas.create_text(self.cx, self.cy-200, text=string, font="Arial 14 bold", justify="center")

        Print(300, 230, printText="Hello World!").draw(canvas)
        string = "Print boxes are used to print or display things on the screen.\n"
        string += "Just type exactly what you want print.\n"
        string += "If you want to print out a variable value type 'var(variableName)'\n"
        string += "or a calculation type 'var(3*5)'."
        canvas.create_text(300, 300, text=string, font="Arial 8 bold", justify="center")

        Variable(670, 230, nameVal=["x", 5]).draw(canvas)
        string = "Set boxes are used to set variables.\n"
        string += "Type in the name of the variable in the first box and its value in the next.\n"
        string += "It will assign the variable to that value.\n"
        string += "So in this case variable 'x' is equal to 5.\n"
        string += "To set variables to text simply but quotes around it."
        canvas.create_text(670, 300, text=string, font="Arial 8 bold", justify="center")

        IfStatement(1020, 230, condition="x >= 5").draw(canvas)
        ElifStatement(1020, 290, condition="x == 4").draw(canvas)
        ElseStatement(1020, 350).draw(canvas)
        string = "If Statement boxes are used to do things if certain conditions are true.\n"
        string += "Type the condidion in the input box.\n"
        string += "You can put other command boxes inside the do part.\n"
        string += "So in this case, if x is greater than euqal to 5, then it will do everything in the do.\n\n"
        string += "Else If or Elif Statements are connected with If Statement.\n"
        string += "It is used for another condition if the first condition is not true.\n"
        string += "There could be multiple elif statements.\n"
        string += "If one of the them is true, the rest won't even be tested.\n\n"
        string += "Else Statements is the default thing to do if\n"
        string += "all the if and elif statements fail.\n\n"
        string += "Note: Elif and Else statments can't be placed before If statements."
        canvas.create_text(1020, 500, text=string, font="Arial 8 bold", justify="center")

        ForLoop(300, 400, forRange=["i", 1, 5]).draw(canvas)
        WhileLoop(300, 460, condition="x > 5").draw(canvas)
        string = "These are the 2 types of Loops: For Loops and While Loops.\n"
        string += "For Loops loop through the do section for a certain number of times.\n"
        string += "While Loops loop through the do section until the condition becomes false.\n"
        string += "For Loops, the 1st input is the variable name, and the 2nd and 3rd is the range of the loop inclusive.\n"
        string += "While Loops, the input is the condition for the loop to keep on looping.\n"
        canvas.create_text(300, 550, text=string, font="Arial 8 bold", justify="center")

        Expression(650, 380).draw(canvas)
        canvas.create_text(650, 410, text="You can put any correct Python code if you want \n(can be used for recursion).", font="Arial 8 bold", justify="center")
        Return(650, 450).draw(canvas)
        canvas.create_text(650, 480, text="Put the value or variable you want the function to return.", font="Arial 8 bold", justify="center")


    elif(self.helpScreenPos == 3):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 4)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "Now let's go over how to create a function.\n"
        string += "You want to drag and drop a command box to the workspace.\n"
        string += "You can also drag and drop boxes in other boxes that contain a do."
        canvas.create_text(self.cx, self.cy-250, text=string, font="Arial 14 bold", justify="center")
        canvas.create_image(self.cx, self.cy+75, image=self.programScreenShot2)
        self.demoVariable.draw(canvas)
        if(self.timer > 70):
            self.demoIfStatment.draw(canvas)
        if(self.timer > 135):
            self.demoPrint.draw(canvas)
        if(self.timer < 65):
            self.demoVariable.move(self.demoVariable.x-8, self.demoVariable.y+2)
        elif(self.timer < 130):
            self.demoIfStatment.move(self.demoIfStatment.x-8, self.demoIfStatment.y+3)
        elif(self.timer < 185):
            self.demoPrint.move(self.demoPrint.x-6, self.demoPrint.y+4)
        elif(self.timer == 185):
            self.demoIfStatment.addDo(self.demoPrint)
    elif(self.helpScreenPos == 4):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 5)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "The program checks for errors as well.\n"
        string += "It will not let you put and Else or Elif Statement before an If Statement.\n"
        string += "It will remove it from the function if done so."
        canvas.create_text(self.cx, self.cy-250, text=string, font="Arial 14 bold", justify="center")
        if(self.timer >= 125):
            canvas.create_image(self.cx, self.cy+75, image=self.programScreenShot3)
        else:
            canvas.create_image(self.cx, self.cy+75, image=self.programScreenShot2)
        self.demoIfStatment2.draw(canvas)
        if(self.timer > 65 and self.timer <125):
            self.demoElifStatment.draw(canvas)
        if(self.timer < 60):
            self.demoIfStatment2.move(self.demoIfStatment2.x-8, self.demoIfStatment2.y+3)
        elif(self.timer < 120):
            self.demoElifStatment.move(self.demoElifStatment.x-8, self.demoElifStatment.y)
    elif(self.helpScreenPos == 5):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 6)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "In the menu, you can create new, open, and save functions under file.\n"
        string += "In the meny, you can access this tutorial under help.\n"
        string += "Creating new and opening functions will be displayed in new tab."
        canvas.create_text(self.cx, self.cy-250, text=string, font="Arial 14 bold", justify="center")
        canvas.create_image(self.cx, self.cy+150, image=self.programScreenShot4)
        canvas.create_text(230, 220, text="Here are the tabs,\nand you can close them.", font="Arial 10 bold", justify="center")
        canvas.create_text(400, 220, text="Here you can \nrename the function.", font="Arial 10 bold", justify="center")
        canvas.create_text(610, 220, text="Here you set comma \ndeliminated parameters.", font="Arial 10 bold", justify="center")
        canvas.create_text(900, 190, text="Click here to convert current\nfunction to Python Code.\nIt will also set \nall the values, \nsuch as function name.", font="Arial 10 bold", justify="center")
        canvas.create_text(1100, 220, text="Click here to convert \nall open functions", font="Arial 10 bold", justify="center")
        canvas.create_text(1250, 260, text="Click here to run \nthe function/functions\n that are converted.", font="Arial 10 bold", justify="center")
    elif(self.helpScreenPos == 6):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 7)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "This is the window that opens when you click run the functions."
        canvas.create_text(self.cx, self.cy-250, text=string, font="Arial 14 bold", justify="center")
        canvas.create_image(self.cx, self.cy+150, image=self.programScreenShot5)
        canvas.create_text(550, 220, text="Click here to run the function you want.", font="Arial 10 bold", justify="center")
        canvas.create_text(850, 220, text="Enter the function \nname you want to run.", font="Arial 10 bold", justify="center")
        canvas.create_text(970, 280, text="Enter the comma \ndelimited parameters \nfor that function.", font="Arial 10 bold", justify="center")
        canvas.create_text(970, 450, text="Here will be all the \nresults that are printed", font="Arial 10 bold", justify="center")
        canvas.create_text(970, 650, text="Here will be all the \nresults that are returned", font="Arial 10 bold", justify="center")
    elif(self.helpScreenPos == 7):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 8)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        canvas.create_image(self.width, self.cy, anchor="e", image=self.forwardArrow)
        string = "These are all the shortcuts:"
        canvas.create_text(self.cx, self.cy-200, text=string, font="Arial 16 bold", justify="center")
        string = "Ctrl+n\tCreates new tab and function\n"
        string += "Ctrl+s\tSaves the current function\n"
        string += "Ctrl+o\tOpens a saved function\n"
        string += "Ctrl+z\tUndo\n"
        string += "Ctrl+y\tRedo\n"
        canvas.create_text(self.cx, self.cy, text=string, font="Arial 14 bold")
    elif(self.helpScreenPos == 8):
        canvas.create_text(self.cx, self.cy-300, text="Help (pg. 9)", font="Arial 30 bold", fill="blue")
        canvas.create_image(0, self.cy, anchor="w", image=self.backArrow)
        string = "You are ready to program now!!!"
        canvas.create_text(self.cx, self.cy, text=string, font="Arial 25 bold", justify="center")
        buttonW, buttonH = 100, 30
        canvas.create_rectangle(self.cx-buttonW, self.cy-buttonH+100, self.cx+buttonW, self.cy+buttonH+100, fill="green")
        canvas.create_text(self.cx, self.cy+100, text="Start Programming!", font="Arial 15 bold")