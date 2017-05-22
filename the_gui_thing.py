import pygame,time,os,sys
from pygame.locals import *
import threading
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1200,800))
pygame.display.set_caption("the_gui")
spr=pygame.sprite.Sprite()
bg=pygame.image.load("whatever.jpg").convert()
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(1)
clk=pygame.time.Clock()
fonty=pygame.font.Font(None,40)
screen.blit(bg,(-400,-100))
pygame.display.flip()
def textdisp(msg,pos):
    text=fonty.render(msg,True,(0,0,0))
    rect=pygame.draw.rect(screen,(0,0,0),((screen.get_width()/2)-150,(screen.get_height()/2)-200,200,20),0)
    screen.blit(bg, (-400, -100))
    screen.blit(text,rect)
    pygame.display.update(rect)
    pygame.display.flip()
    pass
def widgets(msg,pos,name,size):
    #text=fonty.render((msg,True,(0,0,0)))
    pass
def app():
    run=True
    type_str=""
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    if len(type_str)==0:
                        pass
                    else:
                        b.computation(type_str)
                type_str=type_str+chr(event.key)
                textdisp(type_str,(100,770))



    pygame.quit()
    quit()
