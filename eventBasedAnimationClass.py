# eventBasedAnimationClass.py

from Tkinter import *

class EventBasedAnimationClass(object):
    def onMousePressed(self, event): pass
    def onKeyPressed(self, event): pass
    def onTimerFired(self): pass
    def redrawAll(self): pass
    def initAnimation(self): pass
    def leftMousePressed(self, event): pass
    def leftMouseMoved(self, event): pass
    def leftMouseReleased(self, event): pass

    def __init__(self, width=300, height=300):
        self.width = width
        self.height = height
        self.timerDelay = 10 # in milliseconds (set to None to turn off timer)

    def onMousePressedWrapper(self, event):
        self.onMousePressed(event)
        self.redrawAll()

    def onKeyPressedWrapper(self, event):
        self.onKeyPressed(event)
        self.redrawAll()

    def onTimerFiredWrapper(self):
        if (self.timerDelay == None):
            return # turns off timer
        self.onTimerFired()
        #self.redrawAll()
        #self.canvas.after(self.timerDelay, self.onTimerFiredWrapper) 

    def leftMousePressedWrapper(self, event):
        self.leftMousePressed(event)
        self.redrawAll()

    def leftMouseMovedWrapper(self, event):
        self.leftMouseMoved(event)
        self.redrawAll()

    def leftMouseReleasedWrapper(self, event):
        self.leftMouseReleased(event)
        self.redrawAll()

    def run(self):
        # create the root and the canvas
        self.root = Tk()
        self.root.state('zoomed')
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.initAnimation()
        # set up events
        # DK: You can use a local function with a closure
        # to store the canvas binding, like this:
        def f(event): self.onMousePressedWrapper(event)    
        self.root.bind("<Button-3>", f)
        # DK: Or you can just use an anonymous lamdba function, like this:
        self.root.bind("<Key>", lambda event: self.onKeyPressedWrapper(event))
        self.root.bind("<Button-1>", lambda event: self.leftMousePressedWrapper(event))
        #self.root.bind("<Button-3>", rightMousePressed)
        self.canvas.bind("<B1-Motion>", lambda event: self.leftMouseMovedWrapper(event))
        #self.canvas.bind("<B3-Motion>", rightMouseMoved)
        self.root.bind("<B1-ButtonRelease>", lambda event: self.leftMouseReleasedWrapper(event))
        #self.root.bind("<B3-ButtonRelease>", rightMouseReleased)
        #self.onTimerFiredWrapper()
        self.redrawAll()
        # and launch the app (This call BLOCKS, so your program waits
        # until you close the window!)
        
        self.root.mainloop()

# EventBasedAnimationClass(300,300).run()