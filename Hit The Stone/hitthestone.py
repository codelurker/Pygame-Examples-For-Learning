#! /usr/bin/env python

############################################################################
# File name : hitthestone.py
# Purpose : A demo game that destroys the falling stones on shooting
# Start date : 16/01/2012
# End date : In Progress (Stand By Due To Time Limitation)
# Author : Ankur Aggarwal
# License : GNU GPL v3 http://www.gnu.org/licenses/gpl.html
############################################################################

#Important : This game is incomplete. It just shoots the bullets when the spacebar is pressed.
#            Due to time limitation I am unable to finish this game.I thought this as a demo game
#            tutorial for pygame newbies like my other game 'Hungry Snake'
#            My intentions was to shoot  randomly falling stones with the bullets (something game like that).
#            I have already created the stone class but struggled with the sprite group management.
#            Leaving this game in between because going somewhere for about 4 months
#            where laptops are not allowed.
#            I would be greatful to the person who completes this for learning purpose.
#            Contact me at ankur.aggarwal2390@gmail.com


import pygame
from pygame.locals import *
import random
import time

pygame.init()
screen=pygame.display.set_mode((640,480),0,24)
pygame.display.set_caption("Hit The Stone")
background=pygame.Surface(screen.get_size())
background=background.convert()
screen.blit(background,(0,0))

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('plane.gif').convert()
        self.timer=15
        self.rect=self.image.get_rect()
        self.rect.centerx=random.randint(0,screen.get_width())
        self.distancefromcenter=30
        self.rect.centery=screen.get_height()-self.distancefromcenter
        self.dx=2
        self.dy=2

    def update(self):
        self.pressed=pygame.key.get_pressed()
        if self.pressed[K_DOWN]:
            self.rect.centery+=self.dy
        elif self.pressed[K_UP]:
            self.rect.centery-=self.dy
        elif self.pressed[K_LEFT]:
            self.rect.centerx-=self.dx
        elif self.pressed[K_RIGHT]:
            self.rect.centerx+=self.dx
            

        if self.rect.bottom>=screen.get_height():
            self.rect.bottom=screen.get_height()
        elif self.rect.top<=0:
            self.rect.top=0

        if self.rect.centerx>=screen.get_width()-self.distancefromcenter:
            self.rect.centerx=screen.get_width()-self.distancefromcenter
        elif self.rect.centerx<=self.distancefromcenter:
            self.rect.centerx=self.distancefromcenter


class Stone(pygame.sprite.Sprite):
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.centerx=random.randint(5,630)
        self.rect.centery=0
        self.dy=5

    def update(self):
        self.rect.centery+=self.dy
        if self.rect.bottom>=screen.get_height():
            self.rect.centerx=random.randint(5,630)
            self.rect.centery=0


class Bullet(pygame.sprite.Sprite):
    def __init__(self,posx,posy,image):
        pygame.sprite.Sprite.__init__(self)

        self.image=image
        self.rect=self.image.get_rect()        
        self.rect.center=(posx,posy-30)
        self.dy=5
        


    def update(self):
        self.rect.centery-=self.dy
        self.rect.center=(self.rect.centerx,self.rect.centery)
        if self.rect.top<=0:
            self.kill()

       

def main():
    image=pygame.image.load('geometrybullet.png')
    image=image.convert()
    stoneImage=pygame.image.load('stone.png')
    stoneImage=stoneImage.convert_alpha()
    bullet=None
    plane=Plane()
    allSprites=pygame.sprite.Group(plane)
    clock=pygame.time.Clock()

    while 1:
        pressed=pygame.key.get_pressed()
        for i in pygame.event.get():
            if i.type==QUIT or pressed[K_q]:
                exit()
        if  pressed[K_SPACE]:
            plane.timer-=1
            if plane.timer==0:
                bullet=Bullet(plane.rect.centerx,plane.rect.centery,image)
                plane.timer=15
                allSprites.add(bullet)
       # if bullet is not None:
        #    if bullet.rect.colliderect(stone):
         #      print 'a'
#                    bullet.kill()
                   # stone.kill()
        #stone=Stone(stoneImage)
        #allSprites.add(stone)
#        clock.tick(20) */
       
        allSprites.clear(screen,background)
        allSprites.update()
        allSprites.draw(screen)

#         clock.tick(60)
        pygame.display.flip()


if __name__=='__main__':
    main()
        
        

