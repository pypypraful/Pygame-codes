import pygame
import time
import random

display_width = 800
display_height = 650

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
car_width=44 #picture width pixel
car_height=90 #picture height pixel

pygame.init()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carImg = pygame.image.load('mycar.png')
treeImg = pygame.image.load('mytree.png')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy):
    gameDisplay.blit(treeImg,(thingx,thingy))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message_display("You Crashed")


def game_loop():
    x = (display_width*0.5)
    y = (display_height)-car_height

    x_change = 0

    thing_startx = random.randrange(0,display_width-64)
    thing_starty = -600
    thing_speed = 4
    thing_width = 64
    thing_height = 113
    dodged=0


    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change=0
        x+= x_change

        gameDisplay.fill(white)
        things(thing_startx,thing_starty)
        thing_starty+=thing_speed

        car(x,y)
        things_dodged(dodged)

        if x>display_width-car_width or x<0:
            crash()
        if thing_starty>display_height:
            thing_starty=-113
            thing_startx=random.randrange(0,display_width-64)
            dodged+=1
            thing_speed+=1

        if y<thing_starty+thing_height:
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                crash()

        pygame.display.update()
        clock.tick(100)
game_loop()
pygame.quit()
quit()