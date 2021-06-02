import pygame
from random import randint
from Peremen import *
from Engine import *
from Laptop import *

pygame.init()


def write(what_write, file):
    f = open(file, "w")
    f.write(what_write)
    f.close()


def save(file, whatSave):
    f = open(file, "r")
    sohra = f.read()
    newsohra = sohra.split("/")
    for i in range(len(whatSave)):
        newsohra[i] = whatSave[i]
    sohra = "/".join(newsohra)
    write(sohra, file)
    f.close()


def cleaning(file):
    global availability_save
    f = open(file, "r")
    sohra = f.read()
    newsohra = sohra.split("/")
    for i in range(len(newsohra)):
        newsohra[i] = "0"
    availability_save = newsohra[0]
    sohra = "/".join(newsohra)
    write(sohra, file)
    f.close()


def load(file):
    f = open(file, "r")
    sohra_zagruzil = f.read()
    newsohra_zagruzil = sohra_zagruzil.split("/")
    f.close()
    return newsohra_zagruzil


def loadingImg(imgFile, width, height):
    img = pygame.image.load(imgFile)
    img = pygame.transform.scale(img, (img.get_width() * width, img.get_height() * height)).convert_alpha()
    img.set_colorkey((0, 0, 0))
    return img


def loadingApp():
    global screen
    screen = "Меню"


def laptopSpec():
    display.fill((200, 200, 200))
    button(x=400 - laptops[len(laptops)].width, y=10, width=250, height=50, massage="", color=0, activeColor=0,
           colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=29)


def play():
    global screen
    display.fill((200, 200, 200))
    button(x=20, y=10, width=250, height=50, massage=f"Денег: {gold}", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=29)
    if button(x=130, y=130, width=250, height=50, massage="Новый ноутбук", color=(180, 180, 180), activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=110, hitBoxY=15, fontSize=29):
        laptops.append(Laptop(len(laptops)))
        screen = "Ноутбук хар"


def menu():
    global screen
    if button(x=250, y=400, width=250, height=250, massage="Продолжить", color=(10, 10, 10), activeColor=0,
              colorTitle=(220, 220, 220), activeColorTitle=(220, 220, 220), hitBoxX=95, hitBoxY=110, fontSize=30):
        pass
    if button(x=550, y=400, width=250, height=250, massage="Новая Игра", color=(10, 10, 10), activeColor=0,
              colorTitle=(220, 220, 220), activeColorTitle=(220, 220, 220), hitBoxX=95, hitBoxY=110, fontSize=30):
        screen = "Игра"


def game():
    global game_end, display, keys
    game_end = False
    while not game_end:
        clock.tick(FPS)
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_end = True

        display.fill((0, 0, 0))

        if screen == "Меню":
            menu()
        elif screen == "ЗагрузкаПриложения":
            loadingApp()
        elif screen == "Игра":
            play()
        elif screen == "Ноутбук хар":
            laptopSpec()

        print_text(str(int(clock.get_fps())), 10, 10, (120, 120, 120), 20)

        pygame.display.update()


game()
