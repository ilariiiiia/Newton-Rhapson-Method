import pygame


def drawgrid(screen: pygame.display, gridsize: int = 10, deltax:int=0, deltay:int=0) -> None:
    size = screen.get_size()

    hx = int(size[0] / 2)
    hy = int(size[1] / 2)

    load = 2 # how many more lines to load

    passed = False

    # linee verticali
    for x in range(hx + deltax, size[0]*load, int((size[0] - hx) / gridsize)):

        if not passed:
            w = 3
            passed = True
        else:
            w = 1

        pygame.draw.line(
            screen,
            (125, 125, 125),
            (x, 0),
            (x, size[1]),
            width=w
        )
    for x in range(hx + deltax, -size[0]*load, int((hx - size[0]) / gridsize)):
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (x, 0),
            (x, size[1]),
            width=1
        )

    passed = False

    # linee orizzontali
    for y in range(hy + deltay, size[1]*load, int((size[1] - hy) / gridsize)):

        if not passed:
            w = 3
            passed = True
        else:
            w = 1

        pygame.draw.line(
            screen,
            (125, 125, 125),
            (0, y),
            (size[0], y),
            width=w
        )

    for y in range(hy + deltay, -size[1] * load, int((hy - size[1]) / gridsize)):
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (0, y),
            (size[0], y),
            width=1
        )


def drawfunction(screen: pygame.display, f: object, gridsize:int, deltax=0, deltay=0) -> None:
    load = 2  # how many more lines to load
    size = screen.get_size()
    for px in range(-size[0]*load, size[0]*load):
        # costanti
        # metà dimensioni y
        hy = size[1] / 2
        # x è il numero delle ordinate. px è la rappresentazione di quel numero sullo schermo
        x = px / size[0]
        x *= gridsize
        x -= gridsize / 2
        y = f(x) * size[1]/gridsize
        y += hy
        y += deltay
        x2 = (px + 1) / size[0]
        x2 *= gridsize
        x2 -= gridsize / 2
        y2 = f(x2) * size[1] / gridsize
        y2 += hy
        y2 += deltay

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (px+deltax, y),
            (px+deltax+1, y2)
        )
