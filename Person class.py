# # class person:
# #     def __init__(self):
# #         print("this class is called person class")
# #         self.__name = None
# #         self.__age = None
# #
# #     def set_name(self,name):
# #         self.__name=name
# #
# #     def get_name(self):
# #         return self.__name
# #
# #     def set_age(self,age):
# #         self.__age=age
# #
# #     def get_age(self):
# #         return self.__age
# # p = person()
# # p.set_name("vikas")
# # p.set_age(20)
# #
# # print("name=",p.get_name())
# # print("age=",p.get_age())
#
# class student:
#     def __init__(self,name,age,dob):
#         self.name = name
#         self.age = age
#         self.dob = dob
#
#     def getname(self):
#         return self.name
#     def getage(self):
#         return self.age
#     def getdob(self):
#         return self.dob
#
# s = student("vikas",20,"10,11,2005")
# print("name=",s.getname())
# print("age=",s.getage())
# print("dob=",s.getdob())

class Shape:

    def __init__(self, color, borderWidth):
        self.color = color
        self.borderWidth = borderWidth
    #
    # def setColor(self, c):
    #     self.color = c

    def getColor(self):
        return self.color

    # def setBorderWidth(self, bw):
    #     self.borderWidth = bw

    def getBorderWidth(self):
        return self.borderWidth


class Rectangle(Shape):

    def __init__(self, length, width=0, color="", borderWidth=0):
        self.length = length
        self.width = width
        super().__init__(color,borderWidth)

    # def setLength(self, l):
    #     self.length = l

    def getLength(self):
        return self.length
    #
    # def setWidth(self, w):
    #     self.width = w

    def getWidth(self):
        return self.width


# Creating a Rectangle object
r = Rectangle(10, 20, 'red', 100)
print("Rectangle:")
print("Length:", r.getLength())
print("Width:", r.getWidth())
print("Color:", r.getColor())
print("Border Width:", r.getBorderWidth())