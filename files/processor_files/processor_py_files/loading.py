from Engine import *
from main import loadingImg, load
from files.processor_files.processor_py_files.Processor import *


def beforeOne(processor):

    f = open("files/processor_files/processor_txt_files/processors.txt", "r")
    processorSettings = int(f.read())
    f.close()

    texts_in_processors = {"серия": "Выпустить серию процессоров",
                           "один": "Выпустить процессор"
                           }

    processorNums = ["Первый", "Второй", "Третий", "Четвертый", "Пятый",
                     "Шестой", "Седьмой", "Восьмой", "Девятый", "Десятый"]

    processor = Processor(WIDTH - 350, halfHeight - 500, 100,
                          processorSettings)

    allow_left_arrow = loadingImg("files/allow_left_arrow.png", 1, 1)
    allow_right_arrow = loadingImg("files/allow_right_arrow.png", 1, 1)
    cancel_left_arrow = loadingImg("files/cancel_left_arrow.png", 1, 1)
    cancel_right_arrow = loadingImg("files/cancel_right_arrow.png", 1, 1)

    return "Процессор выбор", (allow_left_arrow, allow_right_arrow, cancel_left_arrow, cancel_right_arrow, texts_in_processors,
                    processorNums), processor


def beforeSeria2(processors):

    f = open("files/processor_files/processor_txt_files/processors.txt", "r")
    processorSettings = int(f.read())
    f.close()

    for i in range(len(processors)):
        processors[i] = Processor(WIDTH - 350, halfHeight - 500, 100, processorSettings)

    return processors


def beforeSeeProc(processors, processorsClasses):

    count = int(load("files/processor_files/processor_txt_files/processors.txt")[0])
    if count > 0:
        for i in range(count):
            processors.append(load(f"files/processor_files/processor_txt_files/created/createdProcessors/processor{i + 1}"))

    for i in range(len(processors)):
        processorsClasses.append(Processor(WIDTH - 350, halfHeight - 500, int(processors[i][5]), count,
                                           float(processors[i][1]), int(processors[i][2]), int(processors[i][3]),
                                           str(processors[i][0]), str(processors[i][4])))
    allow_left_arrow = loadingImg("files/allow_left_arrow.png", 1, 1)
    allow_right_arrow = loadingImg("files/allow_right_arrow.png", 1, 1)
    cancel_left_arrow = loadingImg("files/cancel_left_arrow.png", 1, 1)
    cancel_right_arrow = loadingImg("files/cancel_right_arrow.png", 1, 1)

    if len(processors) > 0:
        return "Просмотр процессоров", allow_left_arrow, allow_right_arrow, cancel_left_arrow, cancel_right_arrow
    else:
        return "Игра", allow_left_arrow, allow_right_arrow, cancel_left_arrow, cancel_right_arrow

