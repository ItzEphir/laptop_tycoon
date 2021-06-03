from Engine import display
from Engine import button
from Engine import print_text


class Processor:
    def __init__(self, width, price, model, type):
        self.__width = width
        self.__height = width
        self.__price = price
        self.__model = model
        self.__type = type
        self.__miniwidth = self.__width // 2
        self.__miniheight = self.__height // 2

    def set(self):

        button(x=1230 - self.__width, y=self.__height + 25, width=self.__width, height=self.__height, massage="", color=(197, 201, 199), activeColor=0,
               colorTitle=0, activeColorTitle=0, hitBoxX=0, hitBoxY=0, fontSize=0)
        button(x=1230 - self.__width + self.__miniwidth * 0.75, y=self.__height + 25 + self.__miniheight // 2, width=self.__miniwidth, height=self.__miniheight,
               massage=self.__type, color=(177, 181, 179), activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=(0, 0, 0),
               hitBoxX=0, hitBoxY=0, fontSize=10)

    def get(self, whatget):
        if whatget == "width":
            return self.__width
        elif whatget == "height":
            return self.__height
        elif whatget == "price":
            return self.__price
        elif whatget == "model":
            return self.__model
        elif whatget == "type":
            return self.__type
        elif whatget == "miniwidth":
            return self.__miniwidth
        elif whatget == "miniheight":
            return self.__miniheight
