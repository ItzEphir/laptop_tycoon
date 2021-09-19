import pygame
from Levels import *
if __name__ == '__main__':
    from random import randint
    from Peremen import *
    from Engine import *
    from Laptop import *
    from PhotoEtit import *
    from files.processor_files.processor_py_files.Processor import *
    from key_text import *
    from files.processor_files.processor_py_files.deleteProcessorFile import *
    import files.processor_files.processor_py_files.processor_seria_draw as processor_seria_draw
    import files.processor_files.processor_py_files.processor_one_draw as processor_one_draw
    import files.processor_files.processor_py_files.ProcessorDone as ProcessorDone
    import files.processor_files.processor_py_files.loading as loadingProcessors
    import files.processor_files.processor_py_files.processor_see as processor_see
    from files.processor_files.processor_py_files.deleteProcessorFile import *

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
def processorSpecChoose(arrows):
    global screen

    display.fill((0, 0, 194))

    if button(x=halfWidth - 400, y=HEIGHT - halfHeight, width=350, height=50, massage=arrows[4]["серия"],
              color=(255, 255, 255), activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0,
              hitBoxX=0, hitBoxY=10, fontSize=20, font="Courier New", delay=120, center=True):
        screen = "Серия процессоров хар"
    elif button(x=halfWidth + 100, y=HEIGHT - halfHeight, width=300, height=50, massage=arrows[4]["один"],
                color=(255, 255, 255), activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0,
                hitBoxX=0, hitBoxY=10, fontSize=20, font="Courier New", delay=120, center=True):
        screen = "Процессор хар"

    checkEscape("Меню")


def processorSeriaSpec(arrows):
    global screen, processors, processorsCounter

    got = processor_seria_draw.spec1(arrows, processorsCounter, processors)

    screen = got[0]
    processors = got[1]
    processorsCounter = got[2]

    checkEscape("Загрузка Процессора")


def processorSeriaSpec2(arrows):
    global screen, processorsCounter

    got = processor_seria_draw.spec2(arrows, processorsCounter)

    print(got[0])

    screen = got[1]
    return got[0]


def processorSeriaSpec3(index):
    global screen, processors, processorsCounter, buttonPressed

    got = processor_seria_draw.spec3(processors, index, processorsCounter, buttonPressed, keys)

    screen = got[0]
    processors = got[1]
    processorsCounter = got[2]
    buttonPressed = got[3]
    index = got[4]

    checkEscape("Игра")
    return index


def processorSeriaSpec4(index, arrows):
    global screen

    screen = processor_seria_draw.spec4(arrows, index, processors)


def processorSpec():
    global screen

    screen = processor_one_draw.spec1(processor, keys)

    checkEscape("Игра")


def processorSpec2(arrows):
    global screen

    screen = processor_one_draw.spec2(arrows, processor)

    checkEscape("Процессор хар")


def processorDone():
    global screen, processor, per

    got = ProcessorDone.one(processor, per, processorsCounter, processors)

    screen = got[0]
    processor = [1]
    per = got[2]


def processorSeriaDone():
    global screen, processors, processorsCounter, per

    got = ProcessorDone.seria(processors, processorsCounter, per)

    screen = got[0]
    processors = got[1]
    processorsCounter = got[2]
    per = got[3]


def loadingBeforeProcessor():
    global screen, processor

    got = loadingProcessors.beforeOne(processor)

    screen = got[0]
    arrows = got[1]
    processor = got[2]

    return arrows


def loadingBeforeSeria2():
    global screen, processors

    processors = loadingProcessors.beforeSeria2(processors)

    screen = "Серия процессоров хар2"


def loadingBeforeSeeProc():
    global screen, processors, processorsClasses

    got = loadingProcessors.beforeSeeProc(processors, processorsClasses)

    screen = got[0]

    return got[1], got[2], got[3], got[4]


def seeProcessors(arrows):
    global screen, currentProcessor

    got = processor_see.see(currentProcessor, processorsClasses, arrows)

    screen = got[0]
    currentProcessor = got[1]

    checkEscape("Процессоры просмотрены")


def processorsSeen():
    global screen, processors, processorsClasses, currentProcessor
    processors = []
    processorsClasses = []
    currentProcessor = 1

    screen = "Игра"


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


# Илья, используй эту функцию для удаления файлов процессоров!
def deleteProcessors():
    global processor, processors, processorsClasses, currentProcessor
    deleteProcessorsFiles(int(load("files/processor_files/processor_txt_files/created/createdProcessors/processors.txt")[0]),
                          int(load("files/processor_files/processor_txt_files/created/createdSeriesProcessors/processorSeries.txt")[0]))
    currentProcessor = 1
    processors = []
    processorsClasses = []
    processor = None


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
           massage=f"Разрешение: {thisLaptop.resolutionX} X {thisLaptop.resolutionY}", color=0, activeColor=0,
           colorTitle=(10, 10, 10),
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
    index = None
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
        elif screen == "Серия процессоров хар":
            processorSeriaSpec(arrows)
        elif screen == "Загрузка серия процессоров хар2":
            loadingBeforeSeria2()
        elif screen == "Серия процессоров хар2":
            index = processorSeriaSpec2(arrows)
        elif screen == "Серия процессоров хар3":
            index = processorSeriaSpec3(index)
        elif screen == "Серия процессоров хар4":
            processorSeriaSpec4(index, arrows)
        elif screen == "Процессор хар":
            processorSpec()
        elif screen == "Процессор хар2":
            processorSpec2(arrows)
        elif screen == "Загрузка Процессора":
            arrows = loadingBeforeProcessor()
        elif screen == "Процессор выбор":
            processorSpecChoose(arrows)
        elif screen == "Процессор сделан":
            processorDone()
        elif screen == "Завершить серию процессоров":
            processorSeriaDone()
        elif screen == "Загрузка просмотра процессоров":
            arrows = loadingBeforeSeeProc()
        elif screen == "Просмотр процессоров":
            seeProcessors(arrows)
        elif screen == "Процессоры просмотрены":
            processorsSeen()
        elif screen == "Просмотр ноутбуков":
            seeLaptops()
        elif screen == "Технологии":
            technologiesGeneral()

        print_text(str(int(clock.get_fps())), 10, 10, (120, 120, 120), 20)

        pygame.display.update()


if __name__ == '__main__':
    game()
