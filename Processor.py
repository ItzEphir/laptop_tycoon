import pygame
from Engine import display
from Engine import button
from Engine import print_text

pygame.init()


class Processor:
    def __init__(self, x, y, price, processorSettings, frequency=1.0):
        self.__x = x
        self.__y = y
        self.__price = price
        self.__processorSettings = processorSettings
        self.__name = ""
        self.__frequency = frequency
        self.__cores = 1
        self.__flows = 2
        self.__flow_technology = "Hyper Threading"
        self.__image = None
        self.__text = None
        self.__font_type = None
        self.__text_width = None
        self.__text_half_width = None
        self.__text_color = (0, 0, 0)
        self.__text_size = 14
        self.__count = 0
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
        self.__printModel(self.__name, self.__x + 100, self.__y + 75, self.__text_color, self.__text_size)

    def __loadImg(self):
        self.__image = pygame.image.load("img/processor.png")
        self.__image = pygame.transform.scale(self.__image,
                                              (self.__image.get_width() * 2, self.__image.get_height() * 2))

    def __loadSettings(self):
        self.__count = self.__processorSettings

    def change_name(self, newname):
        self.__name = newname

    def frequency_minus(self):
        if self.__frequency == 4.1 or self.__frequency == 3.3 or self.__frequency == 2.8 or self.__frequency == 2.3 or\
                self.__frequency == 1.7 or self.__frequency == 1.4 or self.__frequency == 1.2:
            self.__frequency -= 0.05
            self.__frequency *= 10
            self.__frequency = int(self.__frequency)
            self.__frequency = float(self.__frequency)
            self.__frequency /= 10
            self.__price -= 2
            return
        self.__frequency -= 0.1
        self.__frequency *= 10
        self.__frequency = int(self.__frequency)
        self.__frequency = float(self.__frequency)
        self.__frequency /= 10
        self.__price -= 2

    def frequency_plus(self):
        if self.__frequency == 4.1 or self.__frequency == 4.3 or self.__frequency == 4.6 or self.__frequency == 4.8:
            self.__frequency += 0.15
            self.__frequency *= 10
            self.__frequency = int(self.__frequency)
            self.__frequency = float(self.__frequency)
            self.__frequency /= 10
            self.__price += 2
            return
        self.__frequency += 0.1
        self.__frequency *= 10
        self.__frequency = int(self.__frequency)
        self.__frequency = float(self.__frequency)
        self.__frequency /= 10
        self.__price += 2

    def cores_plus(self):
        self.__cores *= 2
        self.__flows = self.__cores * 2
        self.__flow_technology = "Hyper Threading"
        self.__price += 10

    def cores_minus(self):
        self.__cores //= 2
        self.__flows = self.__cores * 2
        self.__flow_technology = "Hyper Threading"
        self.__price -= 10

    def flows_plus(self):
        self.__flows += self.__cores
        if self.__cores != 1 or self.__flows == 3:
            self.__flow_technology = "Multi Threading"
        elif self.__cores == 1 and self.__flows == 2:
            self.__flow_technology = "Hyper Threading"
        self.__price += 10

    def flows_minus(self):
        self.__flows -= self.__cores
        if self.__cores != 1 or self.__flows == 2:
            self.__flow_technology = "Hyper Threading"
        elif self.__flows == 1:
            self.__flow_technology = ""
        self.__price -= 10

    def count_plus(self, arr):
        self.__count += arr

    def get(self, whatget):
        if whatget == "price":
            return self.__price
        elif whatget == "name":
            return self.__name
        elif whatget == "frequency":
            return self.__frequency
        elif whatget == "cores":
            return self.__cores
        elif whatget == "flows":
            return self.__flows
        elif whatget == "flow technology":
            return self.__flow_technology
        elif whatget == 'count':
            return self.__count

    def __del__(self):
        self.__x = None
        self.__y = None
        self.__price = None
        self.__processorSettings = None
        self.__name = None
        self.__frequency = None
        self.__cores = None
        self.__flows = None
        self.__flow_technology = None
        self.__image = None
        self.__text = None
        self.__font_type = None
        self.__text_width = None
        self.__text_half_width = None
        self.__text_color = None
        self.__text_size = None
        self.__count = None
