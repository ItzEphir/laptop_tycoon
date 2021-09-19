from Peremen import *
from Engine import *
from files.processor_files.processor_py_files.CreateFolder import *
from main import create, save, write


def one(processor, per, processorsCounter, processors):

    display.fill((0, 0, 194))

    processor.set()

    print_text("Загрузка", halfWidth - 100, halfHeight - 100, (255, 255, 255))
    create(f"files/processor_files/processor_txt_files/created/createdProcessors/processor{processor.get('count') + 1}")
    processor.count_plus(1)

    write(str(f'{processor.get("name")}/{str(processor.get("frequency"))}/\
    {str(processor.get("cores"))}/{str(processor.get("flows"))}/\
    {processor.get("flow technology")}/{str(processor.get("price"))}'),
          f'files/processor_files/processor_txt_files/created/createdProcessors/processor{processor.get("count")}')

    save("files/processor_files/processor_txt_files/processors.txt", [str(processor.get("count"))])

    return "Игра", None, ""


def seria(processors, processorsCounter, per):

    display.fill((0, 0, 194))

    f = open("files/processor_txt_files/created/processorSeries.txt")
    counts = int(f.read())
    f.close()

    createFolder(f"seria{counts + 1}")
    for i in range(processorsCounter):
        create(f"files/createdSeriesProcessors/seria{counts + 1}/processor{i + 1}.txt")
    create(f"files/createdSeriesProcessors/seria{counts + 1}/processors.txt")

    write(str(processorsCounter), f"files/createdSeriesProcessors/seria{counts + 1}/processors.txt")

    for i in range(len(processors)):
        write(str(f'{processors[i].get("name")}/{str(processors[i].get("frequency"))}/\
    {str(processors[i].get("cores"))}/{str(processors[i].get("flows"))}/\
    {processors[i].get("flow technology")}/{str(processors[i].get("price"))}'),
              f'files/createdSeriesProcessors/seria{counts + 1}/processor{i + 1}.txt')

    write(str(counts + 1), "files/processorSeries.txt")

    return "Игра", [], 0, ""

