import inspect
import os
import sys


def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def createFolder(name):
    currentFolder = str(get_script_dir())

    currentFolder += "/files/"
    os.chdir(currentFolder)
    try:
        os.mkdir("createdSeriesProcessors")
        currentFolder += "createdSeriesProcessors"
        os.chdir(currentFolder)
    except FileExistsError:
        currentFolder += "createdSeriesProcessors"
        os.chdir(currentFolder)

    os.mkdir(name)

    os.chdir(get_script_dir())

