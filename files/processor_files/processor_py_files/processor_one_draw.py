from Peremen import *
from Engine import *
from key_text import *


def spec1(processor, keys):
    global buttonPressed

    display.fill((0, 0, 194))

    print_text("Название:", halfWidth - 80, halfHeight - 500, (255, 255, 255))

    if button(halfWidth - 200, halfHeight - 400, 300, 50, "____________", 0, 0, (255, 255, 255)):
        buttonPressed = True
    elif button(0, 0, WIDTH, halfHeight - 400, "") or button(0, 0, halfWidth - 200, HEIGHT, "") or \
            button(0, halfHeight - 350, WIDTH, HEIGHT - (halfHeight - 350), "") or \
            button(halfWidth + 100, 0, WIDTH - (halfHeight + 100), HEIGHT, ""):
        buttonPressed = False

    if buttonPressed:
        get = keyboard_to_text(keys)
        processor.change_name(get)
        exition = processor.get("name") + "|"
    else:
        exition = processor.get("name")

    print_text(exition, halfWidth - 100, halfHeight - 400, (255, 255, 255))

    if processor.get("name") != "":
        if button(halfWidth - 77, halfHeight - 300, 100, 50, "Далее", (255, 255, 255), (150, 150, 150),
                  (0, 0, 0), (255, 255, 255), 40, 10, 25, "Courier New"):
            return "Процессор хар2"
    else:
        button(halfWidth - 77, halfHeight - 300, 100, 50, "Далее", (150, 150, 150), 0,
               (255, 255, 255), 0, 40, 10, 25, "Courier New")

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        return "Игра"
    return "Процессор хар"


def spec2(arrows, processor):

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

    print_text("Кол-во потоков" + " (" + processor.get("flow technology") + ")", halfWidth - 580, halfHeight - 450,
               (255, 255, 255), 14)
    print_text(str(processor.get("flows")), halfWidth - 485, halfHeight - 385, (255, 255, 255))
    if processor.get("flows") != 48 and processor.get("flow technology") == "Hyper Threading" or \
            processor.get("flows") == 1:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 400))
        if button(halfWidth - 450, halfHeight - 400, 50, 50, ""):
            processor.flows_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 400))
    if (processor.get("flows") != 2 and processor.get("flow technology") == "Multi Threading") or \
            processor.get("cores") == 1 and processor.get("flows") != 1:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 400))
        if button(halfWidth - 560, halfHeight - 400, 50, 50, ""):
            processor.flows_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 400))

    if button(x=1150, y=600, width=100, height=50,
              massage="=>", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        return "Процессор сделан"

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        return "Игра"
    return "Процессор хар2"
