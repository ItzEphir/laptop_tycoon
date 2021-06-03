from Engine import display


class Processor:
    def __init__(self, width, price, model, type):
        self.__width = width
        self.__height = width
        self.__price = price
        self.__model = model
        self.__type = type
        self.__miniwidth = self.__width // 2
        self.__miiniheight = self.__height // 2

    def set(self):
        pass

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
            return self.__miiniheight
