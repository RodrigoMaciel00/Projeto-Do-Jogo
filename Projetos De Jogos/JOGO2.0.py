import pygame
from pygame import mixer
from random import randint
#Base
pygame.init()
mixer.init()
# X direita 550
# X esquerda 250
# Y do chão 515
# Y do Teto 1
p_x = 300
p_y = 100
P_speed = 20

I_x = 100

I_y1 = 700
I_y2 = 1000
I_y3 = 600

I_speed = randint(10, 15)

timer = 0
timer2 = 0

FDP = pygame.image.load('Space.png')
PP = pygame.image.load('SS.png')
I1 = pygame.image.load('asteroid.png')
I2 = pygame.image.load('ISS.png')
I3 = pygame.image.load('ISS3.png')
mixer.music.load('EpicMusic.mpeg')

tf = pygame.font.SysFont('Bauhaus 93', 25)
txt = tf.render('T= ', True, (255, 255, 255))
pos_t = txt.get_rect()
pos_t.center = 65, 50

mixer.music.play()
pg = pygame.display.set_mode((700, 600))
pygame.display.set_caption('Projeto Do Jogo2')

pga = True
while pga:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pga = False

    cmnd = pygame.key.get_pressed()
    if cmnd[pygame.K_RIGHT]:
        p_x += P_speed
    if cmnd[pygame.K_LEFT]:
        p_x -= P_speed

#COLISAO
    if I_x < 80 + p_x and I_y1 < 90 + p_y:
        p_y = 2000

    if timer < 10:
        timer += 1
    else:
        timer2 += 1
        txt = tf.render('T= ' + str(timer2), True, (255, 255, 255))
        timer = 0

    if I_y1 <= -80:
        I_y1 = randint(900, 1400)

    if I_y2 <= -80:
        I_y2 = randint(900, 1400)

    if I_y3 <= -80:
        I_y3 = randint(900, 1400)

    I_y1 -= I_speed
    I_y2 -= I_speed
    I_y3 -= I_speed

    pg.blit(FDP, (0, 0))
    pg.blit(PP, (p_x, p_y))
    pg.blit(I1, (I_x + 100, I_y1))
    pg.blit(I2, (I_x + 250, I_y2))
    pg.blit(I3, (I_x + 400, I_y3))
    pg.blit(txt, pos_t)

    pygame.display.update()

pygame.quit()
