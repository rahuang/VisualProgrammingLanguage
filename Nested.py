import string
from Print import Print
from Variable import Variable
from Return import Return
from Expression import Expression



class Nested(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.width = 100
        self.height = 25
        self.condition = ""
        self.do = []
        self.depth = 0
        self.selected = False

    def move(self, x, y):
        dx, dy = x - self.x, y - self.y
        self.x, self.y = x, y
        for i in xrange(len(self.do)):
            x = self.do[i].x + dx
            y = self.do[i].y + dy
            self.do[i].move(x, y)

    def inRange(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<y<self.y+self.height):
            for i in xrange(len(self.do)):
                tmp = self.do[i].inRange(x, y)
                if(tmp != None):
                    if(self.do[i] is tmp and isinstance(self.do[i], Nested)):
                        self.do.pop(i)
                    elif(isinstance(self.do[i], Print) or isinstance(self.do[i], Variable) or isinstance(self.do[i], Return) or isinstance(self.do[i], Expression)):
                        self.do.pop(i)
                    return tmp
            return self
        return None


    def inRangeWithoutPop(self, x, y):
        if(self.x-self.width<=x<=self.x+self.width and self.y-self.height<y<self.y+self.height):
            for i in xrange(len(self.do)):
                tmp = self.do[i].inRangeWithoutPop(x, y)
                if(tmp != None):
                    self.processObj()
                    return tmp
            return self
        return None
    
    def snapDoList(self):
        xpos = self.x-self.width+20
        ypos = self.y-self.height+40
        for i in xrange(len(self.do)):
            self.do[i].move(xpos+self.do[i].width, ypos+self.do[i].height)
            ypos += 10 + 2*self.do[i].height

    def processObj(self):
        height = 25
        width = 100
        for i in xrange(len(self.do)):
            if(isinstance(self.do[i], Nested)):
                self.do[i].processObj()
            height += 5 + self.do[i].height
            if(self.do[i].width > width):
                width = self.do[i].width
        self.height = height
        self.width = width + 20
        self.snapDoList()

    def addDo(self, obj):
        self.do.append(obj)
        self.do.sort(key=lambda obj: obj.y)
        self.processObj()
        