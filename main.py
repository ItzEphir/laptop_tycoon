import pygame
from random import randint
from Peremen import *
from Engine import *
from Laptop import *
from Levels import *

pygame.init()
levels = Levels()


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


def loadingLaptopSpec():
    global thisLaptop, screen, screenLaptop, landscapeImg
    landscapeImg = loadingImg("img/Пейзаж.jpg", 1, 1)
    laptops.append(Laptop(len(laptops)))
    thisLaptop = laptops[len(laptops) - 1]
    screenLaptop = 1


def laptopSpec1():
    button(x=20, y=20, width=250, height=50,
           massage=f"Ширина: {((thisLaptop.width - thisLaptop.originalWidth) // 10) + 1}", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    if button(x=160, y=60, width=30, height=40, massage=f">", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.width - thisLaptop.originalWidth) // 10) < levels.maxWidth:
            thisLaptop.price += 2
            thisLaptop.width += 10
    if button(x=20, y=60, width=30, height=40, massage=f"<", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.width - thisLaptop.originalWidth) // 10) + 1 > 1:
            thisLaptop.price -= 2
            thisLaptop.width -= 10
    button(x=20, y=120, width=250, height=50,
           massage=f"Высота: {((thisLaptop.height - thisLaptop.originalHeight) // 10) + 1}", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    if button(x=160, y=160, width=30, height=40, massage=f">", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.height - thisLaptop.originalHeight) // 10) < levels.maxHeight:
            thisLaptop.price += 2
            thisLaptop.height += 10
    if button(x=20, y=160, width=30, height=40, massage=f"<", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.height - thisLaptop.originalHeight) // 10) + 1 > 1:
            thisLaptop.price -= 2
            thisLaptop.height -= 10

    button(x=20, y=220, width=250, height=50,
           massage=f"Ширина экрана: {((thisLaptop.widthScreen - thisLaptop.originalWidthScreen) // 10) + 1}", color=0,
           activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    if button(x=160, y=260, width=30, height=40, massage=f">", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.widthScreen - thisLaptop.originalWidthScreen) // 10) < levels.maxWidthScreen:
            thisLaptop.price += 2
            thisLaptop.widthScreen += 10
    if button(x=20, y=260, width=30, height=40, massage=f"<", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.widthScreen - thisLaptop.originalWidthScreen) // 10) + 1 > 1:
            thisLaptop.price -= 2
            thisLaptop.widthScreen -= 10
    button(x=20, y=320, width=250, height=50,
           massage=f"Высота экрана: {((thisLaptop.heightScreen - thisLaptop.originalHeightScreen) // 10) + 1}", color=0,
           activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    if button(x=160, y=360, width=30, height=40, massage=f">", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.heightScreen - thisLaptop.originalHeightScreen) // 10) < levels.maxHeightScreen:
            thisLaptop.price += 2
            thisLaptop.heightScreen += 10
    if button(x=20, y=360, width=30, height=40, massage=f"<", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=10, hitBoxY=15, fontSize=30):
        if ((thisLaptop.heightScreen - thisLaptop.originalHeightScreen) // 10) + 1 > 1:
            thisLaptop.price -= 2
            thisLaptop.heightScreen -= 10


def laptopSpec2():
    button(x=20, y=50, width=250, height=50,
           massage=f"Цвет: ", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    if button(x=20, y=120, width=30, height=30,
              massage="", color=(200, 0, 0), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (200, 0, 0)
        thisLaptop.colorNumber = 1
    if button(x=70, y=120, width=30, height=30,
              massage="", color=(250, 160, 0), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (250, 80, 0)
        thisLaptop.colorNumber = 2
    if button(x=120, y=120, width=30, height=30,
              massage="", color=(220, 220, 0), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (220, 220, 0)
        thisLaptop.colorNumber = 3
    if button(x=170, y=120, width=30, height=30,
              massage="", color=(0, 200, 0), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (0, 200, 0)
        thisLaptop.colorNumber = 4
    if button(x=220, y=120, width=30, height=30,
              massage="", color=(60, 160, 240), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (60, 160, 240)
        thisLaptop.colorNumber = 5
    if button(x=270, y=120, width=30, height=30,
              massage="", color=(0, 0, 200), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (0, 0, 200)
        thisLaptop.colorNumber = 6
    if button(x=320, y=120, width=30, height=30,
              massage="", color=(0, 0, 0), activeColor=0,
              colorTitle=0, activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30):
        thisLaptop.color = (40, 40, 40)
        thisLaptop.colorNumber = 7
    button(x=20 + (thisLaptop.colorNumber - 1) * 50, y=150, width=250, height=50,
           massage=f"^", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)


def laptopSpec3():
    display.blit(landscapeImg, (750 - thisLaptop.widthScreen / 2, 300 - thisLaptop.heightScreen / 2))


def laptopSpecGeneral():
    global screenLaptop, landscapeImg
    display.fill((200, 200, 200))
    button(x=1000, y=20, width=250, height=50, massage=f"Стоимость: {thisLaptop.price}", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=30)
    pygame.draw.rect(display, thisLaptop.color,
                     (750 - thisLaptop.width / 2, 300 - thisLaptop.height / 2, thisLaptop.width, thisLaptop.height))
    pygame.draw.rect(display, (20, 20, 20),
                     (750 - thisLaptop.widthScreen / 2, 300 - thisLaptop.heightScreen / 2, thisLaptop.widthScreen,
                      thisLaptop.heightScreen))
    pygame.draw.rect(display, (60, 60, 60),
                     (750 - thisLaptop.width / 2 * 1.1, 300 + thisLaptop.height / 2, thisLaptop.width * 1.1,
                      thisLaptop.depth))
    if button(x=1050, y=650, width=150, height=50, massage=f"Вперед", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
        screenLaptop += 1
        if screenLaptop == 3:
            landscapeImg = pygame.transform.scale(landscapeImg,
                                                  (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
    if button(x=100, y=650, width=150, height=50, massage=f"Назад", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
        if screenLaptop > 1:
            screenLaptop -= 1
    if screenLaptop == 1:
        laptopSpec1()
    elif screenLaptop == 2:
        laptopSpec2()
    elif screenLaptop == 3:
        laptopSpec3()


# Дима здесь
def processorSpec():
    pass


def play():
    global screen
    display.fill((200, 200, 200))
    button(x=20, y=10, width=250, height=50, massage=f"Денег: {gold}", color=0, activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=29)
    if button(x=130, y=130, width=270, height=50, massage="Новый ноутбук", color=(180, 180, 180), activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=110, hitBoxY=15, fontSize=29):
        loadingLaptopSpec()
        screen = "Ноутбук хар"
    if button(x=130, y=230, width=270, height=50, massage="Новый процессор", color=(180, 180, 180), activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=125, hitBoxY=15, fontSize=29):
        screen = "Процессор хар"


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
            laptopSpecGeneral()
        elif screen == "Процессор хар":
            processorSpec()

        print_text(str(int(clock.get_fps())), 10, 10, (120, 120, 120), 20)

        pygame.display.update()


game()
