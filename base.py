import os
import random
import pygame
import math
import sys

task_nodes = []
step = 10
def clear():
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(station1[0], station1[1], station_width,station_height))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(station2[0], station2[1], station_width,station_height))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(station3[0], station3[1], station_height,station_width))
    

class agent(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.rect = pygame.rect.Rect((self.x, self.y, 16, 16))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-step, 0)
            self.x-=step
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(step, 0)
            self.x+=step
        elif key[pygame.K_UP]:
            self.rect.move_ip(0, -step)
            self.y-=step
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0, step)
            self.y+=step
        if key[pygame.K_SPACE]:
            task_nodes.append(task_node(self.x,self.y,'dummy_task'))
            print(self.x,self.y)
        

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), pygame.rect.Rect((self.x, self.y, 16, 16)))

    def goto(self,x,y):
        while abs(self.x-x)>1:
            clear()
            if self.x>x:
                self.draw(screen)
                self.rect.move_ip(-1, 0)
                self.x-=1
                pygame.display.update()
            else:
                self.draw(screen)
                self.rect.move_ip(1, 0)
                self.x+=1
                pygame.display.update()
        while abs(self.y-y)>1:
            clear()
            if self.y>y:
                self.draw(screen)
                self.rect.move_ip(0, -1)
                self.y-=1
                pygame.display.update()
            else:
                self.draw(screen)
                self.rect.move_ip(0, 1)
                self.y+=1
                pygame.display.update()


class task_node:
    def __init__(self,x,y,task):
        self.x = x
        self.y = y
        self.task = task



pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
station_width = 40
station_height = 200
station1 = [0,80]
station2 = [screen_width-station_width,80]
station3 = [(screen_width-station_height)/2,0]
agent = agent()

while not done:
    pygame.key.set_repeat(1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_d]:
        clear()
        agent.x = 250
        agent.y = 250
        agent.draw(screen)
        for task_node in task_nodes:
            agent.goto(task_node.x,task_node.y)
    clear()
    agent.draw(screen)
    agent.handle_keys()
    pygame.display.update()
    clock.tick(10)
