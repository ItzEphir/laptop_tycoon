import os


def deleteProcessorsFiles(count):
    for i in range(count):
        os.remove(f"files/createdProcessors/processor{count}")
