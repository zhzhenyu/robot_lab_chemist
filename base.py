import os
import random
import pygame
import math
import sys
from Station import Station
from collections import defaultdict

task_nodes = []
step = 10
def clear():
    screen.fill((255, 255, 255))
<<<<<<< HEAD
    station1.draw()
    station2.draw()
    station3.draw()
    
=======
    pygame.draw.rect(screen, (0, 0, 0), storage_bench.rect)
    pygame.draw.rect(screen, (0, 0, 0), reaction_bench.rect)
    pygame.draw.rect(screen, (0, 0, 0), separation_bench.rect)
>>>>>>> 552b0170a094b456561ccefa72183d539bdfb848

class Agent(object):
    def __init__(self):
        self.x = 250
        self.y = 250
        self.rect = pygame.rect.Rect((self.x, self.y, 16, 16))
<<<<<<< HEAD
        self.learned_tasks = defaultdict(dict)
        self.prev_level = None
        self.current_level = self.learned_tasks
        self.state = None
=======
        self.chemicals = []
>>>>>>> 552b0170a094b456561ccefa72183d539bdfb848

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
<<<<<<< HEAD
            task_nodes.append(task_node(self.x,self.y,'dummy_task'))
            print(self.x,self.y)
    
    def learn_task(self,task):
        if task not in self.current_level:
            self.current_level[task] = {}
        self.prev_level = self.current_level
        self.current_level = self.current_level[task]
        
=======
            task_nodes.append(task_node(self.x, self.y, 'dummy_task'))
            print(self.x, self.y)
>>>>>>> 552b0170a094b456561ccefa72183d539bdfb848

    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), pygame.rect.Rect((self.x, self.y, 16, 16)))

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

class task_node:
    def __init__(self, x, y, task):
        self.x = x
        self.y = y
        self.task = task

class bench:
    def __init__(self, left, top, width, height, chemicals=None):
        if chemicals is None:
            chemicals = []
        self.rect = pygame.rect.Rect(left, top, width, height)
        self.chemicals = chemicals


pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
station_width = 40
station_height = 200
<<<<<<< HEAD
station1 = Station(0,80,screen,station_width,station_height,['pick up items','prepare for reaction'])
station2 = Station(screen_width-station_width,80,screen,station_width,station_height,['C','D'])
station3 = Station((screen_width-station_height)/2,0,screen,station_height,station_width,['E','F'])
agent = Agent()
i = 0
=======
station1 = [0, 80]
station2 = [screen_width - station_width, 80]
station3 = [(screen_width - station_height) / 2, 0]
storage_bench = bench(station1[0], station1[1], station_width, station_height, ["A", "B"])
reaction_bench = bench(station2[0], station2[1], station_width, station_height, [])
separation_bench = bench(station3[0], station3[1], station_height, station_width, [])
agent = agent()
>>>>>>> 552b0170a094b456561ccefa72183d539bdfb848

while not done:
    pygame.key.set_repeat(1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_d]:
        clear()
        agent.current_level = agent.learned_tasks
        agent.x = 250
        agent.y = 250
        agent.draw(screen)
        for task_node in task_nodes:
<<<<<<< HEAD
            agent.goto(task_node.x,task_node.y)
    if pygame.key.get_pressed()[pygame.K_l]:
        agent.learn_task('dummy_task'+str(i))
        i+=1
    station1.get_actions()
    station2.get_actions()
    station3.get_actions()

    agent.display()
=======
            agent.goto(task_node.x, task_node.y)
    # Pick up
    if pygame.key.get_pressed()[pygame.K_p]:
        # calculate distance to bench
        # if robot is next to a bench
        #   ask for chemicals to pickup
        #   if chemical is available
        #       pick up the chemical
        # else
        #   do nothings
        current_bench = None
        if storage_bench.rect.contains(agent.rect):
            print("in the storage bench")
            current_bench = storage_bench
        elif reaction_bench.rect.contains(agent.rect):
            print("in the reaction bench")
            current_bench = reaction_bench
        elif separation_bench.rect.contains(agent.rect):
            print("in the separation bench")
            current_bench = separation_bench
        else:
            print("not next to bench")

        if current_bench:
            chemical = input("chemical to pick up\n")
            if chemical in current_bench.chemicals:
                current_bench.chemicals.remove(chemical)
                agent.chemicals.append(chemical)
                print("agent has chemical " + "".join(agent.chemicals))
            else:
                print("chemical not in current bench")

>>>>>>> 552b0170a094b456561ccefa72183d539bdfb848
    clear()
    agent.draw(screen)
    agent.handle_keys()
    pygame.display.update()
    clock.tick(10)
