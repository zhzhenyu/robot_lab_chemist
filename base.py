import os
import random
import pygame
import math
import sys
from Station import Station
from collections import defaultdict
import numpy as np

task_nodes = []
step = 10
def clear():
    screen.fill((255, 255, 255))
    station1.draw()
    station2.draw()
    station3.draw()

def pairwise_dist(pos1, pos2):
    dist = np.sqrt(np.sum((pos1.reshape(2, 1) - pos2) ** 2, axis=0))
    return dist


class Agent(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.pos = np.array([self.x, self.y])
        self.rect = pygame.rect.Rect((self.x, self.y, agentSize, agentSize))
        self.learned_tasks = defaultdict(dict)
        self.prev_level = None
        self.current_level = self.learned_tasks
        self.state = None
        self.chemicals = []


    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-step, 0)
            self.x -= step
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(step, 0)
            self.x += step
        elif key[pygame.K_UP]:
            self.rect.move_ip(0, -step)
            self.y -= step
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0, step)
            self.y += step
        if key[pygame.K_SPACE]:
            task_nodes.append(task_node(self.x,self.y,'dummy_task'))
            print(self.x,self.y)
        self.pos = np.array([self.x, self.y])
    
    def learn_task(self,task):
        if task not in self.current_level:
            self.current_level[task] = {}
        self.prev_level = self.current_level
        self.current_level = self.current_level[task]
        

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), pygame.rect.Rect((self.x, self.y, agentSize, agentSize)))

    def goto(self, x, y):
        while abs(self.x - x) > 1:
            clear()
            if self.x > x:
                self.draw(screen)
                self.rect.move_ip(-1, 0)
                self.x -= 1
                pygame.display.update()
            else:
                self.draw(screen)
                self.rect.move_ip(1, 0)
                self.x += 1
                pygame.display.update()
        while abs(self.y - y) > 1:
            clear()
            if self.y > y:
                self.draw(screen)
                self.rect.move_ip(0, -1)
                self.y -= 1
                pygame.display.update()
            else:
                self.draw(screen)
                self.rect.move_ip(0, 1)
                self.y += 1
                pygame.display.update()

    def display(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            print('get agent states: ', self.prev_level)


class reagent(object):
    def __init__(self):
        self.pos = np.array([[20, 100], [20, 180], [20, 260]]).transpose()
        self.x = self.pos[0]
        self.y = self.pos[1]

    def possess(self, agx, agy, ind):
        self.x[ind] = agx+agentSize/2
        self.y[ind] = agy+agentSize/2
        self.pos = np.array([self.x, self.y])

    def draw(self, surface):
        pygame.draw.circle(screen, color=reagent0_color, center=[self.x[0], self.y[0]], radius=agentSize / 2)
        pygame.draw.circle(screen, color=reagent1_color, center=[self.x[1], self.y[1]], radius=agentSize / 2)
        pygame.draw.circle(screen, color=reagent2_color, center=[self.x[2], self.y[2]], radius=agentSize / 2)


class task_node:
    def __init__(self, x, y, task):
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
agentSize = 32
reagent0_color = [255, 0, 0]
reagent1_color = [0, 255, 0]
reagent2_color = [0, 0, 255]
station1 = Station(0,80,screen,station_width,station_height,['pick up items','prepare for reaction'])
station2 = Station(screen_width-station_width,80,screen,station_width,station_height,['C','D'])
station3 = Station((screen_width-station_height)/2,0,screen,station_height,station_width,['E','F'])
agent = Agent()
reag = reagent()
possess = False
index = 10

while not done:
    pygame.key.set_repeat(1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_p]:
        if not possess:
            dist = pairwise_dist(agent.pos+np.array([agentSize/2, agentSize/2]), reag.pos)
            if np.any(dist < agentSize):
                possess = True
                index = np.argmin(dist)
        print(possess)
    if pygame.key.get_pressed()[pygame.K_o]:
        possess = False
        print(possess)
    if possess:
        reag.possess(agent.x, agent.y, index)
    if pygame.key.get_pressed()[pygame.K_d]:
        clear()
        agent.current_level = agent.learned_tasks
        agent.x = 250
        agent.y = 250
        agent.draw(screen)
        for task_node in task_nodes:
            agent.goto(task_node.x,task_node.y)
    # if pygame.key.get_pressed()[pygame.K_l]:
    #     agent.learn_task('dummy_task'+str(i))
    #     i+=1
    station1.get_actions()
    station2.get_actions()
    station3.get_actions()

    agent.display()



    clear()
    agent.draw(screen)
    reag.draw(screen)
    agent.handle_keys()
    pygame.display.update()
    clock.tick(10)
