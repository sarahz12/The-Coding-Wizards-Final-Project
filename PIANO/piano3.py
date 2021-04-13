import pygame
from playsound import playsound

black = (0,0,0)
white = (255,255,255)
grey = (175,175,175)
pygame.init()

background = pygame.image.load('background.jpg')

A = 'Music_Notes\A.wav'
B = 'Music_Notes\B.wav'
C = 'Music_Notes\C.wav'
C1 = 'Music_Notes\C1.wav'
D = 'Music_Notes\D.wav'
E = 'Music_Notes\E.wav'
F = 'Music_Notes\F.wav'
G = 'Music_Notes\G.wav'


C_s = 'Music_Notes\C_s.wav'
D_s = 'Music_Notes\D_s.wav'
F_s = 'Music_Notes\F_s.wav'
G_s = 'Music_Notes\G_s.wav'
A_s = 'Music_Notes\A_s.wav'


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Piano")

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def black_btn(x,note):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_coord = 55*x+175
    y_coord = 200

    if x_coord+35 > mouse[0] > x_coord and y_coord+100>mouse[1]>y_coord:
        pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
        if click[0] == 1:
            playsound(note,False)
    
    else:
        pygame.draw.rect(screen,black,(x_coord,y_coord,35,100))


def white_btn(x,note):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    x_coord = 55*x+140
    y_coord = 200
    x_coord1 = 55*x + 175 # Where the black key starts
    y_coord1 = 275 # where the black keys start and are 100 long.

    if (y_coord+100< mouse[1] < y_coord+175) and (x_coord+50 > mouse[0] > x_coord):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 > mouse[0] > x_coord) and (x in (1,4)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (1,4)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 15) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord < mouse[0] < x_coord + 35) and (x in (2,5,6)):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
            playsound(note,False)

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+35 < mouse[0] < x_coord+50) and (x in (2,5,6)):
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))

    elif (y_coord+100 > mouse[1] > y_coord) and (x_coord+15 < mouse[0] < x_coord+50) and (x in (3,7)):
        pygame.draw.rect(screen,grey,(x_coord +15,y_coord,35,100))
        pygame.draw.rect(screen,grey,(x_coord,y_coord +100,50,75))
        if click[0] == 1:
            playsound(note,False)

    elif (x == 8) and (y_coord < mouse[1] < y_coord+175) and (x_coord < mouse[0] < x_coord + 50):
        pygame.draw.rect(screen,grey,(x_coord,y_coord,50,175))
        if click[0] == 1:
           playsound(note,False)

    else:
        pygame.draw.rect(screen,white,(x_coord,y_coord,50,175))


running = True
while running:
    for events in pygame.event.get():

        if events.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0,100,130))
    screen.blit(background, (0, 0))
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Piano", largeText)
    TextRect.center = (400,100)
    screen.blit(TextSurf, TextRect)


    white_btn(1,C)
    white_btn(2,D)
    white_btn(3,E)
    white_btn(4,F)
    white_btn(5,G)
    white_btn(6,A)
    white_btn(7,B)
    white_btn(8,C1)

    black_btn(1,C_s)
    black_btn(2,D_s)
    black_btn(4,F_s)
    black_btn(5,G_s)
    black_btn(6,A_s)

    pygame.display.update()
