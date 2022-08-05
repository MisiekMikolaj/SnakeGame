import pygame
import random
import sys
import time

pygame.init()
screen = pygame.display.set_mode([1220, 720])
liczba_czesci = 1
box = [pygame.Rect(-90, 10, 100, 100)]
X = [[]]
Y = [[]]

a = 0.2
sterowanie = 0
jedz = pygame.Rect(210, 210, 100, 100)
x = [10, 110, 210, 310, 410, 510, 610, 710, 810, 910, 1010, 1110, 1210]
y = [10, 110, 210, 310, 410, 510, 610, 710]
while True:

    i = -1
    for czesc in range(0, liczba_czesci):
        X[czesc].append(box[czesc].x)
        Y[czesc].append(box[czesc].y)

    for czesc in range(liczba_czesci - 1, 0, -1):
        box[czesc].x = X[i-1][-1]
        box[czesc].y = Y[i-1][-1]
        i = i-1

    if sterowanie == 0:
        time.sleep(a)
        box[0].x += 100
    elif sterowanie == 1:
        time.sleep(a)
        box[0].y += 100
    elif sterowanie == 2:
        time.sleep(a)
        box[0].y -= 100
    elif sterowanie == 3:
        time.sleep(a)
        box[0].x -= 100

    c = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and (sterowanie == 0 or sterowanie == 3) and c == 0:
            sterowanie = 1
            c = 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and (sterowanie == 0 or sterowanie == 3) and c == 0:
            sterowanie = 2
            c = 1
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_d) and (sterowanie == 1 or sterowanie == 2) and c == 0:
            sterowanie = 0
            c = 1
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_a) and (sterowanie == 1 or sterowanie == 2) and c == 0:
            sterowanie = 3
            c = 1

    if box[0] == jedz:
        box.append(pygame.Rect(2000, 2000, 100, 100))
        jedz.x = x[random.randrange(0, 12)]
        jedz.y = y[random.randrange(0, 7)]
        liczba_czesci += 1
        X.append([])
        Y.append([])

    W = liczba_czesci-1
    while W > 0:
        W = liczba_czesci - 1
        for czesc in range(liczba_czesci):

            if jedz.x == box[czesc].x and jedz.y == box[czesc].y:

                jedz.x = x[random.randrange(0, 12)]
                jedz.y = y[random.randrange(0, 7)]

            else:
                W -= 1

        #Drawing
    screen.fill((0, 0,  0))
    pygame.draw.rect(screen, (0, 255, 255), jedz)
    for czesc in range(0, liczba_czesci):
        pygame.draw.rect(screen, (0, 255, 0), box[czesc])

    for czesc in range(1, liczba_czesci):
        if box[0].x == box[czesc].x and box[0].y == box[czesc].y:
            sterowanie = 4
            for czesc in range(0, liczba_czesci):
                pygame.draw.rect(screen, (255, 0, 0), box[czesc])
            print(liczba_czesci)

    if box[0].x == 1210 or box[0].x == -90 or box[0].y == -90 or box[0].y == 710:
        sterowanie = 4
        for czesc in range(0, liczba_czesci):
            pygame.draw.rect(screen, (255, 0, 0), box[czesc])
        print(liczba_czesci)

    pygame.display.flip()

    if sterowanie == 4:
        time.sleep(5)
        break
