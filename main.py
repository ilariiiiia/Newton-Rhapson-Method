# libreria per la GUI
import math
import pygame
from NRMethod import NRMethod
from utils.draw import drawgrid, drawfunction

# costanti matematiche
e = math.e
ln = lambda x: math.log(x, e)
log = lambda b, x: math.log(x, b)

# definisco la funzione
f = lambda x: x ** 5 - 3 * x - 2
zero = NRMethod(f, 0)

# GUI

# schermo
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

while True:

    # raccogli eventi. Non serve a molto per ora
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # colore di sottofondo
    screen.fill((0, 0, 0))

    # disegna la griglia
    gridsize = 15
    drawgrid(screen, gridsize)
    size = screen.get_size()
    dx = int(size[0] / gridsize)
    dy = dx

    # metti i punti nel grafico
    drawfunction(screen, f, gridsize)

    # disegno lo 0 della funzione
    x = zero * size[0] / gridsize + size[0] / 2
    y = f(zero) * dy
    y += size[1]/2

    pygame.draw.circle(
        screen,
        (0, 0, 255),
        (x, y),
        radius=3
    )

    pygame.display.flip()

    clock.tick(60)
