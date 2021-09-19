import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
halfWidth = WIDTH // 2
halfHeight = WIDTH // 2
buttonPressed2 = False
oldClick = False

f = open("files/Настройки.txt", "r")
save_downloaded = f.read()
new_save_downloaded = save_downloaded.split("/")
fullScreen = new_save_downloaded[0]
f.close()

if fullScreen == "1":
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
elif fullScreen == "0":
    display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Гонка")

clock = pygame.time.Clock()


def button(x=100, y=100, width=150, height=50, massage="Кнопка",
           color=0, activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0,
           hitBoxX=50, hitBoxY=10, fontSize=20, font="Courier New", delay=120,
           center=False, aim=False, check=True):
    global buttonPressed2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(5)
    if color != 0:
        pygame.draw.rect(display, color, (x, y, width, height))
    print_text(massage, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY), colorTitle, fontSize, font, center)
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if not aim:
            if activeColor != 0:
                pygame.draw.rect(display, activeColor, (x, y, width, height))
            if activeColorTitle != 0:
                print_text(massage, x + width // 2 - hitBoxX, y + (height // 2 - hitBoxY),
                           activeColorTitle, fontSize, font, center)
            if check:
                if click[0] == 1:
                    if not buttonPressed2:
                        buttonPressed2 = True
                else:
                    if buttonPressed2:
                        buttonPressed2 = False
                        return 1
            else:
                if click[0] == 1:
                    pygame.time.delay(delay)
                    return 1
        else:
            if check:
                if not buttonPressed2:
                    buttonPressed2 = True
                if buttonPressed2:
                    buttonPressed2 = False
                    pygame.time.delay(delay)
                    return 1


def print_text(message="Надпись", x=100, y=100, font_color=(0, 0, 0), font_size=20, font="Courier New", center=False):
    font_type = pygame.font.SysFont(font, font_size)
    text = font_type.render(message, True, font_color)
    if center:
        text_width = text.get_width() // 2
        display.blit(text, (x - text_width, y))
    else:
        display.blit(text, (x, y))


