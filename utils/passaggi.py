import pygame
from utils.draw import renderline, renderpoint, drawfunction

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 18)


def drawguesspoint(screen, f=None, g=None, newg=None, gridsize=None, deltax=0, deltay=0, step=0):
    renderpoint(screen, (g, f(g)), gridsize, deltax, deltay, color=(255, 255, 0), radius=5)
    testo = font.render(f"giallo: ({g:.6f}, {f(g):.6f})", True, (255, 255, 0))
    if step == 0: screen.blit(testo, (5, 75))


def drawtangentline(screen, f=None, g=None, newg=None, gridsize=None, deltax=0, deltay=0, step=0):
    drawguesspoint(
        screen,
        f,
        g,
        newg,
        gridsize,
        deltax,
        deltay,
        step
    )

    def dydx(f):
        dx = 0.0005
        return (f(g + dx) - f(g)) / dx

    m = dydx(f)

    def y(x):
        # y = m(x-x0) + y0
        return m * (x - g) + f(g)

    drawfunction(screen, y, gridsize, deltax, deltay)
    testo = font.render(f"giallo: ({g:.6f}, {f(g):.6f})", True, (255, 255, 0))
    if step == 1: screen.blit(testo, (5, 75))


def drawzeroofy(screen, f=None, g=None, newg=None, gridsize=None, deltax=0, deltay=0, step=0):
    drawtangentline(
        screen,
        f,
        g,
        newg,
        gridsize,
        deltax,
        deltay,
        step
    )

    def dydx(f):
        dx = 0.0005
        return (f(g + dx) - f(g)) / dx

    if g != newg:
        m = dydx(f)
        x = -(f(g) / m) + g
        renderpoint(screen, (x, 0), gridsize, deltax, deltay, color=(0, 255, 255), radius=5)
        testo = font.render(f"giallo: ({g:.6f}, {f(g):.6f})", True, (255, 255, 0))
        screen.blit(testo, (5, 75))
        testo = font.render(f"blu: ({x:.6f}, {f(x):.6f})", True, (0, 255, 255))
        screen.blit(testo, (5, 100))
        return x
    else:
        renderpoint(screen, (g, 0), gridsize, deltax, deltay, color=(0, 255, 255), radius=5)
        testo = font.render(f"giallo: ({g:.6f}, {f(g):.6f})", True, (255, 255, 0))
        if step == 2: screen.blit(testo, (5, 75))
        testo = font.render(f"blu: ({newg:.6f}, {f(newg):.6f})", True, (0, 255, 255))
        screen.blit(testo, (5, 100))


class passaggi:
    def __init__(self, screen, f, g, gridsize, deltax, deltay):
        self.screen = screen
        self.f = f
        self.g = g
        self.gridsize = gridsize
        self.deltax = deltax
        self.deltay = deltay
        self.step = 0
        self.steps = [
            drawguesspoint,
            drawtangentline,
            drawzeroofy
        ]
        self.current = drawguesspoint
        self.done = True
        self.newg = g
        # steps
        # 1. draw the guess point
        # 2. draw the tangent line
        # 3. draw the zero of the tangent line
        # repeat

    def update(self, gridsize, deltax, deltay):
        self.gridsize = gridsize
        self.deltax = deltax
        self.deltay = deltay

    def draw(self):
        if self.step == 0:
            self.g = self.newg
        if self.step == 2 and self.done:
            self.done = False
            self.newg = self.current(
                screen=self.screen,
                f=self.f,
                g=self.g,
                gridsize=self.gridsize,
                deltax=self.deltax,
                deltay=self.deltay,
                step=self.step
            )
        else:
            self.current(
                screen=self.screen,
                f=self.f,
                g=self.g,
                newg=self.newg,
                gridsize=self.gridsize,
                deltax=self.deltax,
                deltay=self.deltay,
                step=self.step
            )

    def refresh(self, newg):
        self.g = self.newg = newg
        self.step = 0
        self.current = self.steps[self.step]
        self.draw()

    def next(self):
        self.done = True
        self.step += 1

        self.step %= 3
        self.current = self.steps[self.step]
        self.draw()