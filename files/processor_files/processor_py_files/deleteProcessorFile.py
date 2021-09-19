import os


def deleteProcessorsFiles(count, countSeries):
    for i in range(count):
        os.remove(f"files/createdProcessors/processor{i}")

    for i in range(countSeries):
        os.rmdir(f"files/createdSeriesProcessors/seria{i}")

    return
