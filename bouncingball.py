# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pygame;
pygame.init();
screen=pygame.display.set_mode((400,400));
clock=pygame.time.Clock();
velY=1;
x=200;
y=200;
black=(255,255,255);
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit();
    y=y+velY;
    if y==385:
        velY=-1;
    if y==15:
        velY=1;
    screen.fill(black);
    pygame.draw.circle(screen,(255,0,0),(x,y),15); 
    pygame.display.update(); 
    clock.tick(200);               