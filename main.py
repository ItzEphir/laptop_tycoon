import pygame
from random import randint
from Peremen import *
from Engine import *
from Laptop import *
from Levels import *
from PhotoEtit import *
from Processor import *
from key_text import *

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


def create(way):
    f = open(way, "w")
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
def processorSpec():
    global screen, escapePressed, processor, buttonPressed

    display.fill((0, 0, 194))

    print_text("Название:", halfWidth - 80, halfHeight - 500, (255, 255, 255))

    if button(halfWidth - 200, halfHeight - 400, 300, 50, "____________", 0, 0, (255, 255, 255)):
        buttonPressed = True
    elif button(0, 0, WIDTH, halfHeight - 400, "") or button(0, 0, halfWidth - 200, HEIGHT, "") or \
            button(0, halfHeight - 350, WIDTH, HEIGHT - (halfHeight - 350), "") or \
            button(halfWidth + 100, 0, WIDTH - (halfHeight + 100), HEIGHT, ""):
        buttonPressed = False

    if buttonPressed:
        get = keyboard_to_text(keys, processor)
        processor.change_name(get[1])
        processor.change_name(get[0])
        exition = processor.get("name") + "|"
    else:
        exition = processor.get("name")

    print_text(exition, halfWidth - 100, halfHeight - 400, (255, 255, 255))

    if processor.get("name") != "":
        if button(halfWidth - 77, halfHeight - 300, 100, 50, "Далее", (255, 255, 255), (150, 150, 150),
                  (0, 0, 0), (255, 255, 255), 40, 10, 25, "Courier New"):
            screen = "Процессор хар2"
    else:
        button(halfWidth - 77, halfHeight - 300, 100, 50, "Далее", (150, 150, 150), 0,
               (255, 255, 255), 0, 40, 10, 25, "Courier New")

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Игра"

    checkEscape("Игра")


def processorSpec2(arrows):
    global screen, escapePressed, processor

    # Фон
    display.fill((0, 0, 194))

    processor.set()

    print_text("Частота", halfWidth - 510, halfHeight - 150, (255, 255, 255), 14)
    print_text(str(processor.get("frequency")), halfWidth - 500, halfHeight - 85, (255, 255, 255))
    if processor.get("frequency") != 5.0:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 100))
        if button(halfWidth - 450, halfHeight - 100, 50, 50, ""):
            processor.frequency_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 100))
    if processor.get("frequency") != 1.0:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 100))
        if button(halfWidth - 560, halfHeight - 100, 50, 50, ""):
            processor.frequency_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 100))

    print_text("Кол-во ядер", halfWidth - 510, halfHeight - 300, (255, 255, 255), 14)
    print_text(str(processor.get("cores")), halfWidth - 485, halfHeight - 235, (255, 255, 255))
    if processor.get("cores") != 16:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 250))
        if button(halfWidth - 450, halfHeight - 250, 50, 50, ""):
            processor.cores_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 250))
    if processor.get("cores") != 1:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 250))
        if button(halfWidth - 560, halfHeight - 250, 50, 50, ""):
            processor.cores_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 250))

    print_text("Кол-во потоков" + " (" + processor.get("flow technology") + ")", halfWidth - 580, halfHeight - 450, (255, 255, 255), 14)
    print_text(str(processor.get("flows")), halfWidth - 485, halfHeight - 385, (255, 255, 255))
    if processor.get("flows") != 48 and processor.get("flow technology") == "Hyper Threading" or\
            processor.get("flows") == 1:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 400))
        if button(halfWidth - 450, halfHeight - 400, 50, 50, ""):
            processor.flows_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 400))
    if (processor.get("flows") != 2 and processor.get("flow technology") == "Multi Threading") or\
            processor.get("cores") == 1 and processor.get("flows") != 1:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 400))
        if button(halfWidth - 560, halfHeight - 400, 50, 50, ""):
            processor.flows_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 400))

    if button(x=1150, y=600, width=100, height=50,
              massage="=>", color=0, activeColor=0, colorTitle=(10, 10 ,10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Процессор сделан"

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Игра"

    checkEscape("Процессор хар")


def processorDone():
    global screen, point, processor

    display.fill((0, 0, 194))

    processor.set()

    print_text("Загрузка", halfWidth - 100, halfHeight - 100, (255, 255, 255))
    create(f"files/createdProcessors/processor{processor.get('count') + 1}")
    processor.count_plus(1)

    write(str(f'{processor.get("name")}/{str(processor.get("frequency"))}/\
{str(processor.get("cores"))}/{str(processor.get("flows"))}/\
{processor.get("flow technology")}/{str(processor.get("price"))}'), f'files/createdProcessors/processor{processor.get("count")}')

    save("files/processors.txt", [str(processor.get("count"))])

    processor = None
    screen = "Игра"
    return


def loadingBeforeProcessor():
    global screen, processor

    f = open("files/processors.txt", "r")
    processorSettings = int(f.read())
    f.close()

    processor = Processor(WIDTH - 350, halfHeight - 500, 100,
                          processorSettings)

    allow_left_arrow = loadingImg("img/allow_left_arrow.png", 1, 1)
    allow_right_arrow = loadingImg("img/allow_right_arrow.png", 1, 1)
    cancel_left_arrow = loadingImg("img/cancel_left_arrow.png", 1, 1)
    cancel_right_arrow = loadingImg("img/cancel_right_arrow.png", 1, 1)

    screen = "Процессор хар"
    return allow_left_arrow, allow_right_arrow, cancel_left_arrow, cancel_right_arrow


def loadingBeforeSeeProc():
    global screen, processors, processorsClasses
    count = int(load("files/processors.txt")[0])
    if count > 0:
        for i in range(count):
            processors.append(load(f"files/createdProcessors/processor{i + 1}"))

    for i in range(len(processors)):
        processorsClasses.append(Processor(WIDTH - 350, halfHeight - 500, int(processors[i][5]), count,
                                 float(processors[i][1]), int(processors[i][2]), int(processors[i][3]),
                                 str(processors[i][0]), str(processors[i][4])))
    allow_left_arrow = loadingImg("img/allow_left_arrow.png", 1, 1)
    allow_right_arrow = loadingImg("img/allow_right_arrow.png", 1, 1)
    cancel_left_arrow = loadingImg("img/cancel_left_arrow.png", 1, 1)
    cancel_right_arrow = loadingImg("img/cancel_right_arrow.png", 1, 1)

    if len(processors) > 0:
        screen = "Просмотр процессоров"
    else:
        screen = "Игра"
    return allow_left_arrow, allow_right_arrow, cancel_left_arrow, cancel_right_arrow


def seeProcessors(arrows):
    global screen, currentProcessor
    display.fill((0, 0, 194))

    if currentProcessor != len(processorsClasses):
        display.blit(arrows[1], (1150, halfHeight - 50))
        if button(1150, halfHeight - 50, 100, 100, ""):
            currentProcessor += 1
    else:
        display.blit(arrows[3], (1150, halfHeight - 50))

    if currentProcessor != 1:
        display.blit(arrows[0], (18, halfHeight - 50))
        if button(18, halfHeight - 50, 100, 100, ""):
            currentProcessor -= 1
    else:
        display.blit(arrows[2], (18, halfHeight - 50))

    processorsClasses[currentProcessor - 1].set()

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        screen = "Игра"

    checkEscape("Игра")


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
        screen = "Загрузка Процессора"
    elif button(x=130, y=330, width=270, height=50, massage="Процессоры", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=90, hitBoxY=15, fontSize=29):
        screen = "Загрузка просмотра процессоров"
    elif button(x=130, y=430, width=270, height=50, massage="Ноутбуки", color=(180, 180, 180), activeColor=0,
                colorTitle=(10, 10, 10), activeColorTitle=0, hitBoxX=90, hitBoxY=15, fontSize=29):
        if len(laptops) > 0:

            screen = "Просмотр ноутбуков"
    elif button(x=130, y=530, width=270, height=50, massage="Технологии", color=(180, 180, 180), activeColor=0,
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
    arrows = None
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
        elif screen == "Процессор хар2":
            processorSpec2(arrows)
        elif screen == "Загрузка Процессора":
            arrows = loadingBeforeProcessor()
        elif screen == "Процессор сделан":
            processorDone()
        elif screen == "Загрузка просмотра процессоров":
            arrows = loadingBeforeSeeProc()
        elif screen == "Просмотр процессоров":
            seeProcessors(arrows)
        elif screen == "Просмотр ноутбуков":
            seeLaptops()
        elif screen == "Технологии":
            technologiesGeneral()

        print_text(str(int(clock.get_fps())), 10, 10, (120, 120, 120), 20)

        pygame.display.update()


game()
