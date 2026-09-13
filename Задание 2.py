from pygame import *
from pygame.math import Vector2
import random

init()
screen = display.set_mode((800, 600))
clock = time.Clock()
new_circle = lambda: Vector2(random.randint(50, 750), random.randint(50, 300))
circle, vel, bullet, running = new_circle(), None, None, True

def draw_screen(circle, bullet):
    screen.fill((255, 255, 255))
    draw.circle(screen, (200, 0, 0), circle, 20, 3)
    if bullet is not None:
        draw.circle(screen, (0, 0, 0), bullet, 5)
    display.flip()

def bek(circle, vel, bullet, running):
    for i in event.get():
        if i.type == QUIT:
            running = False
        elif i.type == MOUSEBUTTONDOWN and bullet is None:
            bullet = [400, 630]
            vel = (circle - [400, 630]).normalize() * 500

    if bullet is not None:
        bullet += vel * dt
        if bullet.distance_to(circle) < 20:
            bullet, circle = None, new_circle()
    return running, bullet, circle, vel

while running:
    dt = clock.tick(60) / 1000
    running, bullet, circle, vel = bek(circle, vel, bullet, running)
    draw_screen(circle, bullet)

quit()
