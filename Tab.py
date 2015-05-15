from Tkinter import *

class Tab(object):
    def __init__(self, x, y, name):
        self.width = 35
        self.height = 15
        self.closeSize = 20
        self.x = x
        self.y = y
        self.closeX = x + self.width - 15
        self.closeY = y
        self.name = name
        self.selected = False
        self.selectedTab = PhotoImage(file="pics\selected_tab.gif").subsample(2,2)
        self.deselectedTab = PhotoImage(file="pics\deselected_tab.gif").subsample(2,2)
        self.closeButton = PhotoImage(file="pics\close_button.gif").subsample(4,4)


    def inRange(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width-self.closeSize and self.y-self.height<=y<=self.y+self.height):
            return True
        return False

    def inRangeClose(self, x, y):
        distance = ((x-self.closeX)**2 + (y-self.closeY)**2)**0.5
        if(distance <= self.closeButton.height()):
            return True
        return False

    def setXY(self, x, y):
        self.x = x
        self.y = y
        self.closeX = x + self.width - 15
        self.closeY = y

    def setName(self, name):
        self.name = name

    def draw(self, canvas):
        image = self.deselectedTab
        if(self.selected):
            image = self.selectedTab
        canvas.create_image(self.x, self.y, image=image)
        name = self.name if len(self.name) < 11 else self.name[:7] + "..."
        canvas.create_text(self.x-self.width+10,self.y-self.height+10, text=name, anchor="nw")
        canvas.create_image(self.closeX, self.closeY, image=self.closeButton)

