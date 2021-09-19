from Engine import *


def see(currentProcessor, processorsClasses, arrows):

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

    print_text("Частота: " + str(processorsClasses[currentProcessor - 1].get("frequency")),
               halfWidth - 510, halfHeight - 400, (255, 255, 255), 20)
    print_text("Кол-во ядер: " + str(processorsClasses[currentProcessor - 1].get("cores")),
               halfWidth - 510, halfHeight - 350, (255, 255, 255), 20)
    print_text("Кол-во потоков" + " (" + processorsClasses[currentProcessor - 1].get("flow technology") + "): " +
               str(processorsClasses[currentProcessor - 1].get("flows")), halfWidth - 510, halfHeight - 300,
               (255, 255, 255), 20)

    if button(x=1200, y=10, width=50, height=50,
              massage=f"X", color=0, activeColor=0, colorTitle=(10, 10, 10),
              activeColorTitle=0, hitBoxX=10, hitBoxY=20, fontSize=40, font="Courier New", delay=120):
        return "Процессоры просмотрены", currentProcessor
    return "Просмотр процессоров", currentProcessor
