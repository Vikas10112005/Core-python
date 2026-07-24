# class person:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.address = None
#     def set_name(self,name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#
# p = person()
#
# p.set_name("vikas")
# print("name=",p.get_name())


class Shape:

    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth

    # def setColor(self, c):
    #     self.color = c

    def getColor(self):
        return self.color
    #
    # def setBorderWidth(self, bw):
    #     self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


s = Shape("Red", 5)

print("Color:", s.getColor())
print("Border Width:", s.getBorderWidth())