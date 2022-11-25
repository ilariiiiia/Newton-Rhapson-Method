import pygame


def drawgrid(screen: pygame.display, gridsize: int = 10, deltax: int = 0, deltay: int = 0) -> None:
    size = screen.get_size()

    hx = int(size[0] / 2)
    hy = int(size[1] / 2)

    load = 2  # how many more lines to load

    passed = False

    # linee verticali
    for x in range(hx + deltax, size[0] * load, int((size[0] - hx) / gridsize)):

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
    for x in range(hx + deltax, -size[0] * load, int((hx - size[0]) / gridsize)):
        pygame.draw.line(
            screen,
            (125, 125, 125),
            (x, 0),
            (x, size[1]),
            width=1
        )

    passed = False

    # linee orizzontali
    for y in range(hy + deltay, size[1] * load, int((size[1] - hy) / gridsize)):

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


def renderpoint(screen: pygame.display,
                point: (int, int),
                gridsize: int,
                deltax=0,
                deltay=0,
                color=(0, 0, 255),
                radius=1):
    """
    Args:
    screen - lo schermo
    point - tuple di due int, x e y geometrici
    gridsize
    deltax - spostamento sulla x
    deltay - spostamento sulla y
    """

    size = screen.get_size()
    px = point[0] * size[0] / (gridsize * 2)
    px += size[0] / 2
    px += deltax
    px = int(px)
    py = -1 * point[1] * size[1] / (gridsize * 2)
    py += size[1] / 2
    py += deltay
    py = int(py)

    if px > size[0] or px < 0 or py > size[1] or py < 0:
        return
    pygame.draw.circle(
        screen,
        color,
        (px, py),
        radius
    )


def renderline(
        screen: pygame.display,
        point1: (int, int),
        point2: (int, int),
        gridsize: int,
        deltax=0,
        deltay=0,
        color=(255, 255, 255)):
    size = screen.get_size()
    p = []
    for point in (point1, point2):
        px = point[0] * size[0] / (gridsize * 2)
        px += size[0] / 2
        px += deltax
        px = int(px)
        py = -1 * point[1] * size[1] / (gridsize * 2)
        py += size[1] / 2
        py += deltay
        py = int(py)
        p.append((px, py))
    pygame.draw.line(
        screen,
        (255, 255, 255),
        p[0],
        p[1]
    )


def drawfunction(screen: pygame.display, f: object, gridsize: int, deltax=0, deltay=0) -> None:
    size = screen.get_size()
    dx = deltax / size[0] * gridsize
    resolution = 0.1
    n = 10
    for x in range(int(-1 * (gridsize + dx) * n), int((gridsize + dx) * n), int(resolution * n)):
        x /= n
        renderline(
            screen,
            (x, f(x)),
            (x + resolution, f(x + resolution)),
            gridsize,
            deltax,
            deltay
        )