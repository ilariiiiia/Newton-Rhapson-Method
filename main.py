# libreria per la GUI
import time
import pygame

f = lambda x: x ** 3 - 3 ** x + 1


def NRMethod(f: object, g: float = 0.0) -> float:
    """
    :param f: la funzione. Passa una funzione anonima lambda
    :param g: un qualsiasi punto da provare
    :return: float: il punto in cui la funzione fa 0
    """

    def zerodi(f, x0):
        """
        :param f: la funzione. Passa una funzione anonima lambda
        :return: float: il punto in cui la funzione fa 0
        """

        # data un equazione lineare, rida' il valore x in cui quella equazione e' uguale a 0

        # funzione per trovare la derivata di una funzione in un punto di essa
        def dydx(f):
            dx = 0.0005
            return (f(g + dx) - f(g)) / dx

        m = dydx(f)
        # equazione: y = m(x-x0) + y0
        # rigiro un po' di cose quando y = 0...
        # -y0 = m(x-x0)
        # -y0/m = x-x0
        # x = -y0/m + x0
        y0 = f(x0)
        return -(y0 / m) + x0

    n = 15  # numero di iterazioni
    for _ in range(n):
        g = zerodi(f, g)
    return g

zero = NRMethod(f, 0)

# GUI

# schermo
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

while True:

    # raccogli eventi. Non serve a molto per ora
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # colore di sottofondo
    screen.fill((0, 0, 0))

    # griglia
    size = screen.get_size()

    # dx e' la differenza sulla x delle linee verticali (in px).
    # dy e' uguale ma per le linee orizzontali.
    gridsize = 10  # grandezza della griglia sullo schermo
    dx = int(size[0] / gridsize)
    dy = dx

    passed = False

    # linee verticali
    for x in range(int(dx / 2), int(size[0] + dx / 2), dx):

        if x/size[0] > 0.40 and x/size[0] < 0.60 and not passed:
            w = 5
            passed = True
        else:
            w = 2

        pygame.draw.line(
            screen,
            (125, 125, 125),
            (x, 0),
            (x, size[1]),
            width=w
        )

    passed = False

    # linee orizzontali
    for y in range(int(dy / 2), int(size[1] + dy / 2), dy):

        if y/size[1] > 0.40 and y/size[1] < 0.60 and not passed:
            w = 5
            passed = True
        else:
            w = 2

        pygame.draw.line(
            screen,
            (125, 125, 125),
            (0, y),
            (size[0], y),
            width=w
        )

    # draw the points of the graph
    for px in range(1, size[0]):
        # constants
        # half screen size
        hx = size[0] / 2
        hy = size[1] / 2
        # x is real x value. px is the pixel position
        x = px / size[0]
        x *= gridsize
        x -= gridsize/2
        y = f(x) * dy
        y += hy + 10

        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (px, y),
            radius=1
        )

    x = zero * size[0] / gridsize + size[0]/2
    y = f(zero) * dy
    y += size[1]/2 + 10

    pygame.draw.circle(
        screen,
        (0, 0, 255),
        (x, y),
        radius=3
    )

    pygame.display.flip()

    clock.tick(60)
