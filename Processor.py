import pygame
from Engine import display
from Engine import button
from Engine import print_text

pygame.init()


class Processor:
    def __init__(self, width, x, y, price, processorSettings, processorModels):
        self.__width = width
        self.__height = width
        self.__x = x
        self.__y = y
        self.__price = price
        self.__processorSettings = processorSettings
        self.__model = None
        self.__modelList = processorModels
        self.__miniwidth = self.__width // 2
        self.__miniheight = self.__height // 2
        self.__image = None
        self.__text = None
        self.__font_type = None
        self.__text_width = None
        self.__text_half_width = None
        self.__text_color = (0, 0, 0)
        self.__text_size = 14
        self.__loadSettings()
        self.__loadImg()

    def __printModel(self, message, x, y, font_color=(0, 0, 0), font_size=20):
        self.__font_type = pygame.font.SysFont("Courier New", font_size)
        self.__text = self.__font_type.render(message, True, font_color)
        self.__text_width = self.__text.get_width()
        self.__text_half_width = self.__text_width // 2
        display.blit(self.__text, (x - self.__text_half_width, y))

    def set(self):
        display.blit(self.__image, (self.__x, self.__y))
        self.__printModel(self.__model, self.__x + 100, self.__y + 75, self.__text_color, self.__text_size)

    def __loadImg(self):
        self.__image = pygame.image.load("img/processor.png")
        self.__image = pygame.transform.scale(self.__image,
                                              (self.__image.get_width() * 2, self.__image.get_height() * 2))

    def __loadSettings(self):
        if self.__modelList[0] != "0":
            self.__model = self.__modelList[0]
        else:
            self.__model = "My Processor"

    def change_model(self, arr):
        self.__model = self.__modelList[arr]

    def get(self, whatget):
        if whatget == "width":
            return self.__width
        elif whatget == "height":
            return self.__height
        elif whatget == "price":
            return self.__price
        elif whatget == "model":
            return self.__model
        elif whatget == "model list":
            return self.__modelList
        elif whatget == "miniwidth":
            return self.__miniwidth
        elif whatget == "miniheight":
            return self.__miniheight
