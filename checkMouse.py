import win32api
import win32con


def countMouse():
    if win32api.GetSystemMetrics(win32con.SM_CMOUSEBUTTONS) == 0:
        return False
    else:
        return True
