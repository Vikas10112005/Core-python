class shape:
    def __init__(self,colour,borderwidth):
        self.colour = colour
        self.borderwidth = borderwidth

    def getcolour(self):
        return self.colour
    def getborderwidth(self):
        return self.borderwidth

class rectangle(shape):
    def __init__(self,lenth=0,width=0,colour="",borderwidth=0):
        self.lenth = lenth
        self.width = width
        super().__init__(colour,borderwidth)

    def getlenth(self):
        return self.lenth
    def getwidth(self):
        return self.borderwidth

r = rectangle(10,20,"blue",12)
print("lenth=",r.getlenth())
print("width=",r.getwidth())
print("colour=",r.getcolour())
print("borderwidth=",r.getborderwidth())