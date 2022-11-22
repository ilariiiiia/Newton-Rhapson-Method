import pygame


def drawgrid(screen: pygame.display, gridsize:int = 10) -> None:

    size = screen.get_size()

    hx = int(size[0]/2)
    hy = int(size[1]/2)

    passed = False

    # linee verticali
    for x in range(hx, size[0], int((size[0]-hx)/gridsize)):

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
    for x in range(hx, 0, int((hx-size[0])/gridsize)):
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (x, 0),
            (x, size[1]),
            width=1
        )

    passed = False

    # linee orizzontali
    for y in range(hy, size[1], int((size[1]-hy)/gridsize)):

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

    for y in range(hy, 0, int((hy-size[1])/gridsize)):
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (0, y),
            (size[0], y),
            width=1
        )
