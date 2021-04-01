import os,random,pygame,math,sys,time
from Station import Station
from Agent import Agent
from Chemical import Chemical
from Task_node import Task_node
import numpy as np
from functools import partial

task_nodes = []
step = 10

def draw_hold_chemicals():
    for i,chemical in enumerate(agent.chemicals):
        pygame.draw.rect(screen, chemical.color, pygame.Rect(10+i*15, 450, chemical.width, chemical.height))

def clear():
    screen.fill((255, 255, 255))
    station1.draw()
    station2.draw()
    station3.draw()
    for chemical in all_chemicals:
        if chemical.being_hold: 
            draw_hold_chemicals()
        else:
            chemical.draw()

def pick_up_chemical(agent,all_chemicals,tasks,learning):
    for chemical in all_chemicals:
            if agent.rect.collidepoint(chemical.get_pos()):
                agent.pick_up(chemical)
                if learning:
                    tasks.append(Task_node(chemical.get_pos(),'pick_up'))

def drop_off_chemical(agent,tasks,learning):
    if agent.chemicals:
        chemical = agent.chemicals[0]
        agent.chemicals.pop(0)
        chemical.update_pos(agent.x,agent.y)
        chemical.being_hold = False
        if learning:
            tasks.append(Task_node(chemical.get_pos(),'drop_down'))

def react(agent,all_chemicals,learning):
    if agent.chemicals:
        r,g,b = 0,0,0
        for chemical in agent.chemicals:
            r+=chemical.color[0]
            g+=chemical.color[1]
            b+=chemical.color[2]
        color = (r/3,g/3,b/3)
        new_chemical = Chemical(agent.x,agent.y, screen,chemical_width,chemical_height,color)
        agent.chemicals = []
        all_chemicals.append(new_chemical)
        if learning:
            tasks.append(Task_node(new_chemical.get_pos(),'react'))

def reset():
    global chemical1,chemical2,all_chemicals,agent
    pygame.init()
    chemical1 = Chemical(20,150, screen,chemical_width,chemical_height,(0,100,100))
    chemical2 = Chemical(20,200, screen,chemical_width,chemical_height,(100,100,0))
    agent = Agent(screen,step)
    all_chemicals = [chemical1,chemical2]
    clear()

pygame.init()
screen_width,screen_height = 500,500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
station_width,station_height = 40,200
chemical_width,chemical_height = 10,10
tasks = []

station1 = Station(0,80,screen,station_width,station_height,['pick up items','prepare for reaction'])
station2 = Station(screen_width-station_width,80,screen,station_width,station_height,['C','D'])
station3 = Station((screen_width-station_height)/2,0,screen,station_height,station_width,['E','F'])

chemical1 = Chemical(20,150, screen,chemical_width,chemical_height,(0,100,100))
chemical2 = Chemical(20,200, screen,chemical_width,chemical_height,(100,100,0))
all_chemicals = [chemical1,chemical2]

agent = Agent(screen,step)

while not done:
    pygame.key.set_repeat(1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_p]:
        pick_up_chemical(agent,all_chemicals,tasks,True)
    if pygame.key.get_pressed()[pygame.K_d]:
        drop_off_chemical(agent,tasks,True)
    if pygame.key.get_pressed()[pygame.K_g]:
        tasks.append(Task_node(agent.get_pos(),'go_to'))
    if pygame.key.get_pressed()[pygame.K_r]:
        react(agent,all_chemicals,True)
    if pygame.key.get_pressed()[pygame.K_s]:
        reset()
        for task_node in tasks:
            agent.goto(task_node.pos,clear)
            action = task_node.action
            if action == 'pick_up':
                pick_up_chemical(agent,all_chemicals,tasks,False)
            elif action == 'drop_down':
                drop_off_chemical(agent,tasks,False)
            elif action == 'react':
                react(agent,all_chemicals,False)

    
    station1.get_actions()
    station2.get_actions()
    station3.get_actions()
    agent.display()
    agent.draw(screen)
    agent.handle_keys()
    pygame.display.update()
    clear()
    clock.tick(10)
