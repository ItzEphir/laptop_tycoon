from Peremen import per, keyPressed, needKey
import pygame


def keyboard_to_text(keys):
    global per, keyPressed, needKey
    capslock = pygame.key.get_mods() & pygame.KMOD_CAPS
    if keys[pygame.K_LSHIFT] or capslock:
        if keys[pygame.K_q]:
            if not keyPressed:
                keyPressed = True
                needKey = "Q"
        elif keys[pygame.K_w]:
            if not keyPressed:
                keyPressed = True
                needKey = "W"
        elif keys[pygame.K_e]:
            if not keyPressed:
                keyPressed = True
                needKey = "E"
        elif keys[pygame.K_r]:
            if not keyPressed:
                keyPressed = True
                needKey = "R"
        elif keys[pygame.K_t]:
            if not keyPressed:
                keyPressed = True
                needKey = "T"
        elif keys[pygame.K_y]:
            if not keyPressed:
                keyPressed = True
                needKey = "Y"
        elif keys[pygame.K_u]:
            if not keyPressed:
                keyPressed = True
                needKey = "U"
        elif keys[pygame.K_i]:
            if not keyPressed:
                keyPressed = True
                needKey = "I"
        elif keys[pygame.K_o]:
            if not keyPressed:
                keyPressed = True
                needKey = "O"
        elif keys[pygame.K_p]:
            if not keyPressed:
                keyPressed = True
                needKey = "P"
        elif keys[pygame.K_a]:
            if not keyPressed:
                keyPressed = True
                needKey = "A"
        elif keys[pygame.K_s]:
            if not keyPressed:
                keyPressed = True
                needKey = "S"
        elif keys[pygame.K_d]:
            if not keyPressed:
                keyPressed = True
                needKey = "D"
        elif keys[pygame.K_f]:
            if not keyPressed:
                keyPressed = True
                needKey = "F"
        elif keys[pygame.K_g]:
            if not keyPressed:
                keyPressed = True
                needKey = "G"
        elif keys[pygame.K_h]:
            if not keyPressed:
                keyPressed = True
                needKey = "H"
        elif keys[pygame.K_j]:
            if not keyPressed:
                keyPressed = True
                needKey = "J"
        elif keys[pygame.K_k]:
            if not keyPressed:
                keyPressed = True
                needKey = "K"
        elif keys[pygame.K_l]:
            if not keyPressed:
                keyPressed = True
                needKey = "L"
        elif keys[pygame.K_z]:
            if not keyPressed:
                keyPressed = True
                needKey = "Z"
        elif keys[pygame.K_x]:
            if not keyPressed:
                keyPressed = True
                needKey = "X"
        elif keys[pygame.K_c]:
            if not keyPressed:
                keyPressed = True
                needKey = "C"
        elif keys[pygame.K_v]:
            if not keyPressed:
                keyPressed = True
                needKey = "V"
        elif keys[pygame.K_b]:
            if not keyPressed:
                keyPressed = True
                needKey = "B"
        elif keys[pygame.K_n]:
            if not keyPressed:
                keyPressed = True
                needKey = "N"
        elif keys[pygame.K_m]:
            if not keyPressed:
                keyPressed = True
                needKey = "M"
        elif keys[pygame.K_0]:
            if not keyPressed:
                keyPressed = True
                needKey = "0"
        elif keys[pygame.K_1]:
            if not keyPressed:
                keyPressed = True
                needKey = "1"
        elif keys[pygame.K_2]:
            if not keyPressed:
                keyPressed = True
                needKey = "2"
        elif keys[pygame.K_3]:
            if not keyPressed:
                keyPressed = True
                needKey = "3"
        elif keys[pygame.K_4]:
            if not keyPressed:
                keyPressed = True
                needKey = "4"
        elif keys[pygame.K_5]:
            if not keyPressed:
                keyPressed = True
                needKey = "5"
        elif keys[pygame.K_6]:
            if not keyPressed:
                keyPressed = True
                needKey = "6"
        elif keys[pygame.K_7]:
            if not keyPressed:
                keyPressed = True
                needKey = "7"
        elif keys[pygame.K_8]:
            if not keyPressed:
                keyPressed = True
                needKey = "8"
        elif keys[pygame.K_9]:
            if not keyPressed:
                keyPressed = True
                needKey = "9"
        elif keys[pygame.K_SPACE]:
            if not keyPressed:
                keyPressed = True
                needKey = " "
        elif keys[pygame.K_BACKSPACE] and len(per) != 0:
            keyPressed = True
            needKey = "delete"
        else:
            if keyPressed:
                keyPressed = False
                if needKey == "delete":
                    per = list(per)
                    per.pop(len(per) - 1)
                    per = "".join(per)
                else:
                    per += needKey
                return per
    elif keys[pygame.K_q]:
        if not keyPressed:
            keyPressed = True
            needKey = "q"
    elif keys[pygame.K_w]:
        if not keyPressed:
            keyPressed = True
            needKey = "w"
    elif keys[pygame.K_e]:
        if not keyPressed:
            keyPressed = True
            needKey = "e"
    elif keys[pygame.K_r]:
        if not keyPressed:
            keyPressed = True
            needKey = "r"
    elif keys[pygame.K_t]:
        if not keyPressed:
            keyPressed = True
            needKey = "t"
    elif keys[pygame.K_y]:
        if not keyPressed:
            keyPressed = True
            needKey = "y"
    elif keys[pygame.K_u]:
        if not keyPressed:
            keyPressed = True
            needKey = "u"
    elif keys[pygame.K_i]:
        if not keyPressed:
            keyPressed = True
            needKey = "i"
    elif keys[pygame.K_o]:
        if not keyPressed:
            keyPressed = True
            needKey = "o"
    elif keys[pygame.K_p]:
        if not keyPressed:
            keyPressed = True
            needKey = "p"
    elif keys[pygame.K_a]:
        if not keyPressed:
            keyPressed = True
            needKey = "a"
    elif keys[pygame.K_s]:
        if not keyPressed:
            keyPressed = True
            needKey = "s"
    elif keys[pygame.K_d]:
        if not keyPressed:
            keyPressed = True
            needKey = "d"
    elif keys[pygame.K_f]:
        if not keyPressed:
            keyPressed = True
            needKey = "f"
    elif keys[pygame.K_g]:
        if not keyPressed:
            keyPressed = True
            needKey = "g"
    elif keys[pygame.K_h]:
        if not keyPressed:
            keyPressed = True
            needKey = "h"
    elif keys[pygame.K_j]:
        if not keyPressed:
            keyPressed = True
            needKey = "j"
    elif keys[pygame.K_k]:
        if not keyPressed:
            keyPressed = True
            needKey = "k"
    elif keys[pygame.K_l]:
        if not keyPressed:
            keyPressed = True
            needKey = "l"
    elif keys[pygame.K_z]:
        if not keyPressed:
            keyPressed = True
            needKey = "z"
    elif keys[pygame.K_x]:
        if not keyPressed:
            keyPressed = True
            needKey = "x"
    elif keys[pygame.K_c]:
        if not keyPressed:
            keyPressed = True
            needKey = "c"
    elif keys[pygame.K_v]:
        if not keyPressed:
            keyPressed = True
            needKey = "v"
    elif keys[pygame.K_b]:
        if not keyPressed:
            keyPressed = True
            needKey = "b"
    elif keys[pygame.K_n]:
        if not keyPressed:
            keyPressed = True
            needKey = "n"
    elif keys[pygame.K_m]:
        if not keyPressed:
            keyPressed = True
            needKey = "m"
    elif keys[pygame.K_0]:
        if not keyPressed:
            keyPressed = True
            needKey = "0"
    elif keys[pygame.K_1]:
        if not keyPressed:
            keyPressed = True
            needKey = "1"
    elif keys[pygame.K_2]:
        if not keyPressed:
            keyPressed = True
            needKey = "2"
    elif keys[pygame.K_3]:
        if not keyPressed:
            keyPressed = True
            needKey = "3"
    elif keys[pygame.K_4]:
        if not keyPressed:
            keyPressed = True
            needKey = "4"
    elif keys[pygame.K_5]:
        if not keyPressed:
            keyPressed = True
            needKey = "5"
    elif keys[pygame.K_6]:
        if not keyPressed:
            keyPressed = True
            needKey = "6"
    elif keys[pygame.K_7]:
        if not keyPressed:
            keyPressed = True
            needKey = "7"
    elif keys[pygame.K_8]:
        if not keyPressed:
            keyPressed = True
            needKey = "8"
    elif keys[pygame.K_9]:
        if not keyPressed:
            keyPressed = True
            needKey = "9"
    elif keys[pygame.K_SPACE]:
        if not keyPressed:
            keyPressed = True
            needKey = " "
    elif keys[pygame.K_BACKSPACE] and len(per) != 0:
        keyPressed = True
        needKey = "delete"
    else:
        if keyPressed:
            keyPressed = False
            if needKey == "delete":
                per = list(per)
                per.pop(len(per) - 1)
                per = "".join(per)
            else:
                per += needKey
            return per

    return per