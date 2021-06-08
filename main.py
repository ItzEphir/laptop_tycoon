import pygame
from random import randint
from Peremen import *
from Engine import *
from Laptop import *
from Levels import *
from PhotoEtit import *
from Processor import *

pygame.init()
levels = Levels()
levels.refresh()

# Шаблон
# button(x=100, y=650, width=150, height=50,
#        massage=f"Назад", color=0, activeColor=0, colorTitle=(10, 10, 10),
#        activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30, font="Courier New", delay=120)


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
    global thisLaptop, screen, screenLaptop, landscapeImg, landscapeImgEdit, newLandscapeImg
    landscapeImg = loadingImg("img/Пейзаж.jpg", 1, 1)
    thisLaptop = Laptop(len(laptops))
    screenLaptop = 1
    landscapeImg = pygame.transform.scale(landscapeImg,
                                          (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
    landscapeImgEdit = Photo("img/Пейзаж.jpg")
    for i in range(landscapeImgEdit.width):
        for j in range(landscapeImgEdit.height):
            r = landscapeImgEdit.pix[i, j][0]
            g = landscapeImgEdit.pix[i, j][1]
            b = landscapeImgEdit.pix[i, j][2]
            r = r // 1.2
            g = g // 1.2
            b = b // 1.2
            landscapeImgEdit.draw.point((i, j), (int(r), int(g), int(b)))
    landscapeImgEdit.image.save("Новый пейзаж.jpg", "JPEG")
    newLandscapeImg = loadingImg("Новый пейзаж.jpg", 1, 1)
    newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                             (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()


def loadingSeeLaptops():
    global screenSeeLaptop, thisLaptop
    screenSeeLaptop = 1
    thisLaptop = laptops[0]


def loadingTech():
    global screenTech
    levels.refresh()
    screenTech = 1


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
    global newLandscapeImg, landscapeImgEdit
    display.blit(newLandscapeImg, (750 - thisLaptop.widthScreen / 2, 300 - thisLaptop.heightScreen / 2))
    button(x=40, y=30, width=250, height=50,
           massage=f"Матрица:", color=(180, 180, 180), activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=70, hitBoxY=15, fontSize=30)
    if button(x=40, y=100, width=250, height=50, massage=f"TN", color=(180, 180, 180), activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=15, hitBoxY=15, fontSize=30):
        landscapeImgEdit = Photo("img/Пейзаж.jpg")
        for i in range(landscapeImgEdit.width):
            for j in range(landscapeImgEdit.height):
                r = landscapeImgEdit.pix[i, j][0]
                g = landscapeImgEdit.pix[i, j][1]
                b = landscapeImgEdit.pix[i, j][2]
                r = r // 1.2
                g = g // 1.2
                b = b // 1.2
                landscapeImgEdit.draw.point((i, j), (int(r), int(g), int(b)))
        landscapeImgEdit.image.save("Новый пейзаж.jpg", "JPEG")
        newLandscapeImg = loadingImg("Новый пейзаж.jpg", 1, 1)
        newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                                 (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
        if thisLaptop.screenTech == "VA":
            thisLaptop.price -= 10
        elif thisLaptop.screenTech == "IPS":
            thisLaptop.price -= 20
        elif thisLaptop.screenTech == "OLED":
            thisLaptop.price -= 30
        thisLaptop.screenTech = "TN"
    elif button(x=40, y=160, width=250, height=50, massage=f"VA", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=15, hitBoxY=15, fontSize=30):
        landscapeImgEdit = Photo("img/Пейзаж.jpg")
        for i in range(landscapeImgEdit.width):
            for j in range(landscapeImgEdit.height):
                r = landscapeImgEdit.pix[i, j][0]
                g = landscapeImgEdit.pix[i, j][1]
                b = landscapeImgEdit.pix[i, j][2]
                r /= 1.15
                g /= 1.15
                b /= 1.15
                landscapeImgEdit.draw.point((i, j), (int(r), int(g), int(b)))
        landscapeImgEdit.image.save("Новый пейзаж.jpg", "JPEG")
        newLandscapeImg = loadingImg("Новый пейзаж.jpg", 1, 1)
        newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                                 (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
        if thisLaptop.screenTech == "TN":
            thisLaptop.price += 10
        elif thisLaptop.screenTech == "IPS":
            thisLaptop.price -= 10
        elif thisLaptop.screenTech == "OLED":
            thisLaptop.price -= 20
        thisLaptop.screenTech = "VA"
    elif button(x=40, y=220, width=250, height=50,
                massage=f"IPS", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=15, hitBoxY=15, fontSize=30):
        landscapeImgEdit = Photo("img/Пейзаж.jpg")
        for i in range(landscapeImgEdit.width):
            for j in range(landscapeImgEdit.height):
                r = landscapeImgEdit.pix[i, j][0]
                g = landscapeImgEdit.pix[i, j][1]
                b = landscapeImgEdit.pix[i, j][2]
                r /= 1.1
                g /= 1.1
                b /= 1.1
                landscapeImgEdit.draw.point((i, j), (int(r), int(g), int(b)))
        landscapeImgEdit.image.save("Новый пейзаж.jpg", "JPEG")
        newLandscapeImg = loadingImg("Новый пейзаж.jpg", 1, 1)
        newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                                 (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
        if thisLaptop.screenTech == "TN":
            thisLaptop.price += 20
        elif thisLaptop.screenTech == "VA":
            thisLaptop.price += 10
        elif thisLaptop.screenTech == "OLED":
            thisLaptop.price -= 10
        thisLaptop.screenTech = "IPS"
    elif button(x=40, y=280, width=250, height=50,
                massage=f"OLED", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=20, hitBoxY=15, fontSize=30):
        landscapeImgEdit = Photo("img/Пейзаж.jpg")
        for i in range(landscapeImgEdit.width):
            for j in range(landscapeImgEdit.height):
                r = landscapeImgEdit.pix[i, j][0]
                g = landscapeImgEdit.pix[i, j][1]
                b = landscapeImgEdit.pix[i, j][2]
                r *= 1
                g *= 1
                b *= 1
                landscapeImgEdit.draw.point((i, j), (int(r), int(g), int(b)))
        landscapeImgEdit.image.save("Новый пейзаж.jpg", "JPEG")
        newLandscapeImg = loadingImg("Новый пейзаж.jpg", 1, 1)
        newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                                 (thisLaptop.widthScreen, thisLaptop.heightScreen)).convert_alpha()
        if thisLaptop.screenTech == "TN":
            thisLaptop.price += 30
        elif thisLaptop.screenTech == "VA":
            thisLaptop.price += 20
        elif thisLaptop.screenTech == "IPS":
            thisLaptop.price += 10
        thisLaptop.screenTech = "OLED"


def laptopSpecPrice():
    button(x=40, y=30, width=250, height=50,
           massage=f"Цена:", color=(180, 180, 180), activeColor=0,
           colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=55, hitBoxY=15, fontSize=30)
    button(x=120, y=100, width=100, height=50,
           massage=str(int(thisLaptop.salePrice)), color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=30, hitBoxY=15, fontSize=27)
    if button(x=50, y=100, width=50, height=50,
              massage=f"<", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=13, hitBoxY=15, fontSize=30, font="Courier New", delay=11):
        thisLaptop.salePrice -= 1
    if button(x=240, y=100, width=50, height=50,
              massage=f">", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=13, fontSize=30, font="Courier New", delay=11):
        thisLaptop.salePrice += 1


def laptopSpecGeneral():
    global screenLaptop, landscapeImg, landscapeImgEdit, newLandscapeImg, screen
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
    if screenLaptop != 4:
        if button(x=1050, y=650, width=150, height=50, massage=f"Вперед", color=0, activeColor=0,
                  colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
            if screenLaptop == 3:
                thisLaptop.salePrice = int(thisLaptop.price * 1.3)
            elif screenLaptop == 2:
                newLandscapeImg = pygame.transform.scale(newLandscapeImg,
                                                         (thisLaptop.widthScreen,
                                                          thisLaptop.heightScreen)).convert_alpha()
            screenLaptop += 1
    else:
        if button(x=1050, y=650, width=150, height=50, massage=f"Разработать", color=0, activeColor=0,
                  colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
            thisLaptop.countMark()
            print(thisLaptop.markFirst)
            print(thisLaptop.mark)
            laptops.append(thisLaptop)
            screen = "Игра"
    if button(x=100, y=650, width=150, height=50, massage=f"Назад", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
        if screenLaptop > 1:
            screenLaptop -= 1
        else:
            screen = "Игра"
    if screenLaptop == 1:
        laptopSpec1()
    elif screenLaptop == 2:
        laptopSpec2()
    elif screenLaptop == 3:
        laptopSpec3()
    elif screenLaptop == 4:
        laptopSpecPrice()


def showMark():
    pass


# Дима здесь
def processorSpec(typeproc="Intel", modelproc=1):
    global screen, escapePressed, processors

    # Фон
    display.fill((0, 0, 194))

    if typeproc == "Intel":
        processors = [Processor(100, 100, 1, "Intel"), Processor(100, 105, 2, "Intel"), Processor(100, 110, 3, "Intel")]
    elif typeproc == "AMD":
        processors = [Processor(100, 75, 1, "AMD"), Processor(150, 85, 2, "AMD"), Processor(150, 90, 3, "AMD")]

    if modelproc == 1:
        processor = processors[1]
    elif modelproc == 2:
        processor = processors[2]
    elif modelproc == 3:
        processor = processors[3]

    processor.set()

    checkEscape("Игра")


# И здесь тоже Дима
def checkEscape(where):
    global escapePressed, screen
    # Выход нажатием клавиши escape
    if keys[pygame.K_ESCAPE]:
        # Проверка на долговременное нажатие (если убрать - баги)
        if not escapePressed:
            escapePressed = True
            pygame.time.delay(120)
    else:
        # Продолжение проверки на долговременное нажатие
        if escapePressed:
            screen = where
            escapePressed = False


def seeLaptops():
    global screen, thisLaptop, screenSeeLaptop
    display.fill((200, 200, 200))
    pygame.draw.rect(display, thisLaptop.color,
                     (800 - thisLaptop.width / 2, 300 - thisLaptop.height / 2, thisLaptop.width, thisLaptop.height))
    pygame.draw.rect(display, (20, 20, 20),
                     (800 - thisLaptop.widthScreen / 2, 300 - thisLaptop.heightScreen / 2, thisLaptop.widthScreen,
                      thisLaptop.heightScreen))
    pygame.draw.rect(display, (60, 60, 60),
                     (800 - thisLaptop.width / 2 * 1.1, 300 + thisLaptop.height / 2, thisLaptop.width * 1.1,
                      thisLaptop.depth))
    if button(x=1050, y=650, width=150, height=50, massage=f"Вперед", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
        if screenSeeLaptop < len(laptops):
            screenSeeLaptop += 1
            thisLaptop = laptops[screenSeeLaptop - 1]
    if button(x=100, y=650, width=150, height=50,
              massage=f"Назад", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30, font="Courier New", delay=120):
        if screenSeeLaptop > 1:
            screenSeeLaptop -= 1
            thisLaptop = laptops[screenSeeLaptop - 1]
    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Игра"
    button(x=500, y=30, width=150, height=50,
           massage=f"Название: {thisLaptop.name}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=20, fontSize=35, font="Courier New", delay=120)
    button(x=40, y=30, width=150, height=50,
           massage=f"Цена: {thisLaptop.salePrice}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=15, fontSize=30, font="Courier New", delay=120)
    button(x=40, y=90, width=150, height=50,
           massage=f"Матрица: {thisLaptop.screenTech}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=15, fontSize=30, font="Courier New", delay=120)
    button(x=40, y=150, width=150, height=50,
           massage=f"Разрешение: {thisLaptop.resolutionX} X {thisLaptop.resolutionY}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=15, fontSize=30, font="Courier New", delay=120)
    button(x=40, y=210, width=150, height=50,
           massage=f"Оценка: {thisLaptop.mark}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=15, fontSize=30, font="Courier New", delay=120)


def technologies1():
    button(x=100, y=30, width=150, height=50,
           massage=f"Ширина ноутбука: {levels.maxWidth}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=20, fontSize=30, font="Courier New", delay=120)
    if button(x=50, y=30, width=50, height=50,
              massage=f"<", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=13, hitBoxY=20, fontSize=30, font="Courier New", delay=200):
        if levels.maxWidth > levels.originalMaxWidth:
            levels.maxWidth -= 1
    if button(x=470, y=30, width=50, height=50,
              massage=f">", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=30, font="Courier New", delay=200):
        levels.maxWidth += 1
    button(x=100, y=100, width=150, height=50,
           massage=f"Высота ноутбука: {levels.maxHeight}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=55, hitBoxY=20, fontSize=30, font="Courier New", delay=120)
    if button(x=50, y=100, width=50, height=50,
              massage=f"<", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=13, hitBoxY=20, fontSize=30, font="Courier New", delay=200):
        if levels.maxHeight > levels.originalMaxHeight:
            levels.maxHeight -= 1
    if button(x=470, y=100, width=50, height=50,
              massage=f">", color=(180, 180, 180), activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=30, font="Courier New", delay=200):
        levels.maxHeight += 1


def technologiesGeneral():
    global screenTech, screen
    display.fill((200, 200, 200))
    if button(x=1050, y=650, width=150, height=50, massage=f"Вперед", color=0, activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30):
        if screenTech < len(laptops):
            screenTech += 1
    if button(x=100, y=650, width=150, height=50,
              massage=f"Назад", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=60, hitBoxY=15, fontSize=30, font="Courier New", delay=120):
        if screenTech > 1:
            screenTech -= 1
    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Игра"
    if screenTech == 1:
        technologies1()


def play():
    global screen
    display.fill((200, 200, 200))
    button(x=20, y=10, width=250, height=50,
           massage=f"Денег: {gold}", color=0, activeColor=0, colorTitle=(10, 10, 10),
           activeColorTitle=0, hitBoxX=120, hitBoxY=15, fontSize=29, font="Courier New", delay=120)
    if button(x=130, y=130, width=270, height=50, massage="Новый ноутбук", color=(180, 180, 180), activeColor=0,
              colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=110, hitBoxY=15, fontSize=29):
        loadingLaptopSpec()
        screen = "Ноутбук хар"
    elif button(x=130, y=230, width=270, height=50, massage="Новый процессор", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=125, hitBoxY=15, fontSize=29):
        screen = "Процессор хар"
    elif button(x=130, y=330, width=270, height=50, massage="Ноутбуки", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=90, hitBoxY=15, fontSize=29):
        if len(laptops) > 0:
            loadingSeeLaptops()
            screen = "Просмотр ноутбуков"
    elif button(x=130, y=430, width=270, height=50, massage="Технологии", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=95, hitBoxY=15, fontSize=29):
        loadingTech()
        screen = "Технологии"


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
        elif screen == "Просмотр ноутбуков":
            seeLaptops()
        elif screen == "Технологии":
            technologiesGeneral()

        print_text(str(int(clock.get_fps())), 10, 10, (120, 120, 120), 20)

        pygame.display.update()


game()
