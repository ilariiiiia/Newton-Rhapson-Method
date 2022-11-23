# libreria per la GUI
import math
import pygame
from NRMethod import NRMethod
from utils.draw import drawgrid, drawfunction
from utils.inputBox import InputBox

# costanti matematiche
e = math.e
ln = lambda x: math.log(x, e)
log = lambda b, x: math.log(x, b)
sqrt = math.sqrt

# definisco la funzione
testof = "x^5-3x-2"
f = lambda x: x ** 3 - 1.3 * x - 2 * sqrt(abs(x))
zero = NRMethod(f, 3)

# GUI

# schermo
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 18)
inputbox = InputBox(5, 75, 200, 35, text="f(x)=")

gridsize = 4
deltax = 0
deltay = 0

while True:

    # raccogli eventi. Non serve a molto per ora
    for event in pygame.event.get():
        inputbox.handle_event(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if not inputbox.active:
                if event.key == pygame.key.key_code("E"): # rimpicciolisci
                    gridsize = gridsize-1 if gridsize > 1 else gridsize
                elif event.key == pygame.key.key_code("Q"): # ingrandisci
                    gridsize += 1
                if event.key == pygame.key.key_code("A"): # destra
                    deltax += gridsize * 4
                elif event.key == pygame.key.key_code("D"): # sinistra
                    deltax -= gridsize * 4
                if event.key == pygame.key.key_code("W"): # su
                    deltay += gridsize * 4
                elif event.key == pygame.key.key_code("S"):# giu'
                    deltay -= gridsize * 4

    inputbox.update()

    # colore di sottofondo
    screen.fill((0, 0, 0))

    inputbox.draw(screen)

    # disegna la griglia
    drawgrid(screen, gridsize, deltax, deltay)
    size = screen.get_size()
    dx = int(size[0] / gridsize)
    dy = dx

    # metti i punti nel grafico
    drawfunction(screen, f, gridsize, deltax, deltay)

    # disegno lo 0 della funzione
    x = zero * size[0] / gridsize + size[0] / 2
    x += deltax
    y = f(zero) * dy
    y += size[1]/2
    y += deltay
    pygame.draw.circle(
        screen,
        (0, 0, 255),
        (x, y),
        radius=3
    )

    # testo dello 0 della funzione
    testo = font.render(f"zero in {zero:3f}", True, (120, 120, 255))
    screen.blit(testo, (5, 0))

    # testo della funzione
    testo = font.render(f"f(x)={testof}", True, (120, 120, 255))
    screen.blit(testo, (5, 25))

    # altri testi
    testo = font.render(f"dimensioni griglia={gridsize}", True, (120, 120, 255))
    screen.blit(testo, (5, 50))

    pygame.display.flip()

    clock.tick(60)
