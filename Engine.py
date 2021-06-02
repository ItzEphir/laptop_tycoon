import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720
halfWidth = WIDTH // 2
halfHeight = WIDTH // 2

f = open("files/Настройки.txt", "r")
sohra_zagruzil = f.read()
newsohra_zagruzil = sohra_zagruzil.split("/")
fullScreen = newsohra_zagruzil[0]
f.close()

if fullScreen == "1":
    display = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
elif fullScreen == "0":
    display = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Гонка")

clock = pygame.time.Clock()


def button(x=100, y=100, width=150, height=50, massage="Кнопка", color=0, activeColor=0, colorTitle=(0, 0, 0), activeColorTitle=0, hitBoxX=50, hitBoxY=10, fontSize=20):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if color != 0:
        pygame.draw.rect(display, color, (x, y, width, height))
    print_text(massage, x + width / 2 - hitBoxX, y + (height // 2 - hitBoxY), colorTitle, fontSize)
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        if activeColor != 0:
            pygame.draw.rect(display, activeColor, (x, y, width, height))
        if activeColorTitle != 0:
            print_text(massage, x + width / 2 - hitBoxX, y + (height // 2 - hitBoxY), activeColorTitle, fontSize)
        if click[0] == 1:
            pygame.time.delay(120)
            return 1


def print_text(message, x, y, font_color=(0, 0, 0), font_size=20):
    font_type = pygame.font.SysFont("Courier New", font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))
