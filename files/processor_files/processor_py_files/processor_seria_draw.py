from Engine import *
from key_text import *


def spec1(arrows, counter, processors):

    display.fill((0, 0, 194))

    print_text("Введите необходимое количество процессоров в серии:", WIDTH // 2 + 30, HEIGHT - halfHeight,
               (255, 255, 255),
               20, "Courier New", True)

    print_text(str(counter), WIDTH // 2, HEIGHT - halfHeight + 110, (255, 255, 255), 20, "Courier New", True)

    if counter != 0:
        display.blit(arrows[0], (WIDTH // 2 - 100, HEIGHT - halfHeight + 100))
        if button(WIDTH // 2 - 100, HEIGHT - halfHeight + 100, 100, 100, ""):
            counter -= 1
    else:
        display.blit(arrows[2], (WIDTH // 2 - 100, HEIGHT - halfHeight + 100))

    if counter != 10:
        display.blit(arrows[1], (WIDTH // 2 + 45, HEIGHT - halfHeight + 100))
        if button(WIDTH // 2 + 45, HEIGHT - halfHeight + 100, 100, 100, ""):
            counter += 1
    else:
        display.blit(arrows[3], (WIDTH // 2 + 45, HEIGHT - halfHeight + 100))

    if counter > 1:
        if button(WIDTH // 2 - 50, HEIGHT // 2, 100, 50, "Далее", (255, 255, 255), 0, (0, 0, 0),
                  0, 30, 10, 20, "Courier New", True):
            for i in range(counter):
                processors.append("lol")
            pygame.time.delay(120)
            return "Загрузка серия процессоров хар2", processors, counter
    return "Серия процессоров хар", processors, counter


def spec2(arrows, counter):

    display.fill((0, 0, 194))

    for i in range(counter):
        if i < 4:
            if button(WIDTH // 2 - 100, 100 + i * 150, 100, 50, arrows[5][i]):
                return i, "Серия процессоров хар3"
        elif i < 8:
            if button(WIDTH // 2 + 100, 100 + (i - 4) * 150, 100, 50, arrows[5][i]):
                return i, "Серия процессоров хар3"
        else:
            if button(WIDTH // 2 + 300, 100 + (i - 8) * 150, 100, 50, arrows[5][i]):
                return i, "Серия процессоров хар3"

    if button(halfWidth - 500, halfHeight - 300, 200, 50, "Завершить", (255, 255, 255), (150, 150, 150),
              (0, 0, 0), (255, 255, 255), 62, 10, 25, "Courier New", True):
        return 0, "Завершить серию процессоров"

    return 0, "Серия процессоров хар2"


def spec3(processorsList, index, counter, buttonPressed, keys):

    print(index)
    print(processorsList)
    print(processorsList[index].get("name"))

    display.fill((0, 0, 194))

    print_text("Название:", halfWidth - 80, halfHeight - 500, (255, 255, 255))

    if button(halfWidth - 200, halfHeight - 400, 300, 50, "____________", 0, 0, (255, 255, 255), check=False):
        buttonPressed = True
    elif button(0, 0, WIDTH, halfHeight - 400, "") or button(0, 0, halfWidth - 200, HEIGHT, "") or \
            button(0, halfHeight - 350, WIDTH, HEIGHT - (halfHeight - 350), "") or \
            button(halfWidth + 100, 0, WIDTH - (halfHeight + 100), HEIGHT, ""):
        buttonPressed = False

    if buttonPressed:
        get = keyboard_to_text(keys)
        processorsList[index].change_name(get)
        exition = processorsList[index].get("name") + "|"
    else:
        exition = processorsList[index].get("name")

    print_text(exition, halfWidth - 100, halfHeight - 400, (255, 255, 255))

    if processorsList[index].get("name") != "":
        if button(x=halfWidth - 77, y=halfHeight - 300, width=100, height=50, massage="Далее",
                  color=(255, 255, 255), activeColor=(150, 150, 150),
                  colorTitle=(0, 0, 0), activeColorTitle=(255, 255, 255),
                  hitBoxX=40, hitBoxY=10, fontSize=25, font="Courier New", check=False):
            print("lol")
            return "Серия процессоров хар4", processorsList, counter, buttonPressed, index
    else:
        button(halfWidth - 77, halfHeight - 300, 100, 50, "Далее", (150, 150, 150), 0,
               (255, 255, 255), 0, 40, 10, 25, "Courier New")

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):

        return "Игра", [], 0, buttonPressed, index

    return "Серия процессоров хар3", processorsList, counter, buttonPressed, index


def spec4(arrows, index, processors):

    display.fill((0, 0, 194))

    processors[index].set()

    print_text("Частота", halfWidth - 510, halfHeight - 150, (255, 255, 255), 14)
    print_text(str(processors[index].get("frequency")), halfWidth - 500, halfHeight - 85, (255, 255, 255))
    if processors[index].get("frequency") != 5.0:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 100))
        if button(halfWidth - 450, halfHeight - 100, 50, 50, "", check=False):
            processors[index].frequency_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 100))
    if processors[index].get("frequency") != 1.0:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 100))
        if button(halfWidth - 560, halfHeight - 100, 50, 50, "", check=False):
            processors[index].frequency_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 100))

    print_text("Кол-во ядер", halfWidth - 510, halfHeight - 300, (255, 255, 255), 14)
    print_text(str(processors[index].get("cores")), halfWidth - 485, halfHeight - 235, (255, 255, 255))
    if processors[index].get("cores") != 16:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 250))
        if button(halfWidth - 450, halfHeight - 250, 50, 50, "", check=False):
            processors[index].cores_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 250))
    if processors[index].get("cores") != 1:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 250))
        if button(halfWidth - 560, halfHeight - 250, 50, 50, "", check=False):
            processors[index].cores_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 250))

    print_text("Кол-во потоков" + " (" + processors[index].get("flow technology") + ")", halfWidth - 580,
               halfHeight - 450,
               (255, 255, 255), 14)
    print_text(str(processors[index].get("flows")), halfWidth - 485, halfHeight - 385, (255, 255, 255))
    if processors[index].get("flows") != 48 and processors[index].get("flow technology") == "Hyper Threading" or \
            processors[index].get("flows") == 1:
        display.blit(arrows[1], (halfWidth - 450, halfHeight - 400))
        if button(halfWidth - 450, halfHeight - 400, 50, 50, "", check=False):
            processors[index].flows_plus()
    else:
        display.blit(arrows[3], (halfWidth - 450, halfHeight - 400))
    if (processors[index].get("flows") != 2 and processors[index].get("flow technology") == "Multi Threading") or \
            processors[index].get("cores") == 1 and processors[index].get("flows") != 1:
        display.blit(arrows[0], (halfWidth - 560, halfHeight - 400))
        if button(halfWidth - 560, halfHeight - 400, 50, 50, "", check=False ):
            processors[index].flows_minus()
    else:
        display.blit(arrows[2], (halfWidth - 560, halfHeight - 400))

    if button(x=1150, y=600, width=100, height=50,
              massage="=>", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        return "Серия процессоров хар2"
    return "Серия процессоров хар4"

