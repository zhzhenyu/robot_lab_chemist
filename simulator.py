import os, random, pygame, math, sys, time
from Station import Station
from Agent import Agent
from Chemical import Chemical
from Task_node import Task_node
from Parent_node import Parent_node, Hierarchy
from Prompt import Prompt, Merge, Instruction

step = 10


def draw_hold_chemicals():
    for i, chemical in enumerate(agent.chemicals):
        pygame.draw.rect(screen, chemical.color, pygame.Rect(10 + i * 15, 450, chemical.width, chemical.height))


def clear():
    screen.fill((255, 255, 255))
    for station in all_stations:
        station.draw()
    for chemical in all_chemicals:
        if chemical.being_hold:
            draw_hold_chemicals()
        else:
            chemical.draw()


def pick_up_chemical(agent, all_chemicals, tasks, learning):
    for chemical in all_chemicals:
        if agent.rect.collidepoint(chemical.get_pos()):
            agent.pick_up(chemical)
            if learning:
                node = Task_node(chemical.get_pos(), 'pick_up')
                tasks.append(node)
                stage_nodes.append(node)


def drop_off_chemical(agent, tasks, learning):
    if agent.chemicals:
        chemical = agent.chemicals[0]
        drop_x = agent.x
        drop_y = agent.y
        print(agent.chemicals)
        for index in range(len(agent.chemicals)):
            chemical = agent.chemicals[0]
            agent.chemicals.remove(agent.chemicals[0])
            chemical.update_pos(drop_x, drop_y)
            chemical.being_hold = False
            drop_y = drop_y - 30
            drop_x = drop_x
        if learning:
            node = Task_node(chemical.get_pos(), 'drop_down')
            tasks.append(node)
            stage_nodes.append(node)


def react(agent, all_chemicals, learning):
    if agent.chemicals:
        r, g, b = 0, 0, 0
        components = []
        for chemical in agent.chemicals:
            r += chemical.color[0]
            g += chemical.color[1]
            b += chemical.color[2]
            chemical.being_hold = False
            all_chemicals.remove(chemical)
            components.append(chemical.color)
        r, g, b = min(240, r), min(240, g), min(240, b)
        color = (r, g, b)
        mix_chemical = Chemical(agent.x, agent.y, screen, chemical_width, chemical_height, color, components)
        agent.chemicals = []
        all_chemicals.append(mix_chemical)
        if learning:
            node = Task_node(mix_chemical.get_pos(), 'react')
            tasks.append(node)
            stage_nodes.append(node)


def separate(agent, all_chemicals, learning):
    if agent.chemicals:
        for i, chemical in enumerate(agent.chemicals):
            if chemical.components:
                r, g, b = 0, 0, 0
                for j, color in enumerate(chemical.components):
                    component_chemical = Chemical(agent.x + 10, agent.y + j * 20, screen, chemical_width,
                                                  chemical_height, color, [])
                    r += chemical.color[0]
                    g += chemical.color[1]
                    b += chemical.color[2]
                    all_chemicals.append(component_chemical)
                n = len(chemical.components)
                all_chemicals.remove(chemical)
                agent.chemicals.remove(chemical)
                avg_color = (r // n, g // n, b // n)
                new_chemical = Chemical(agent.x + 10, agent.y + n * 20, screen, chemical_width, chemical_height,
                                        avg_color, [])
                all_chemicals.append(new_chemical)
                break
        if learning:
            node = Task_node(agent.get_pos(), 'separate')
            tasks.append(node)
            stage_nodes.append(node)


def merge_nodes(annotation):
    global stage_nodes
    parent_node = Parent_node()
    actions = ''
    for node in stage_nodes:
        parent_node.children.append(node)
        actions += node.action + ' '
    parent_node.annotation.append(annotation)
    parent_nodes.append(parent_node)
    print(annotation + ' sub-task: ' + actions)
    stage_nodes = []


def add_demonstration():
    global tasks, demonstrations
    demonstrations.append(tasks)
    tasks = []


def reset():
    global chemical1, chemical2, chemical3, all_chemicals, agent
    chemical1 = Chemical(20, 120, screen, chemical_width, chemical_height, (0, 100, 100), [])
    chemical2 = Chemical(20, 180, screen, chemical_width, chemical_height, (100, 100, 0), [])
    chemical3 = Chemical(20, 240, screen, chemical_width, chemical_height, (100, 0, 100), [])
    all_chemicals = [chemical1, chemical2, chemical3]
    agent = Agent(screen, step)
    clear()


pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
station_width, station_height = 40, 200
chemical_width, chemical_height = 12, 12
demonstrations = []
tasks = []
stage_nodes = []
parent_nodes = []
parent_index = 0

station1 = Station(0, 80, screen, station_width, station_height, ['pick up chemicals', 'prepare for reaction'])
station2 = Station(screen_width - station_width, 80, screen, station_width, station_height, ['reaction bench'])
station3 = Station((screen_width - station_height) / 2, 0, screen, station_height, station_width,
                   ['separating chemical mixtures'])
all_stations = [station1, station2, station3]
chemical1 = Chemical(20, 120, screen, chemical_width, chemical_height, (0, 100, 100), [])
chemical2 = Chemical(20, 180, screen, chemical_width, chemical_height, (100, 100, 0), [])
chemical3 = Chemical(20, 240, screen, chemical_width, chemical_height, (100, 0, 100), [])
key_to_chemical = {'1': chemical1, '2': chemical2, '3': chemical3}
all_chemicals = [chemical1, chemical2, chemical3]
agent = Agent(screen, step)
hierarchy = Hierarchy()

while not done:
    pygame.key.set_repeat(1000, 1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.key.get_pressed()[pygame.K_p]:
        pick_up_chemical(agent, all_chemicals, tasks, True)
    if pygame.key.get_pressed()[pygame.K_d]:
        drop_off_chemical(agent, tasks, True)
    if pygame.key.get_pressed()[pygame.K_g]:
        node = Task_node(agent.get_pos(), 'go_to')
        tasks.append(node)
        stage_nodes.append(node)
    if pygame.key.get_pressed()[pygame.K_r]:
        react(agent, all_chemicals, True)
    if pygame.key.get_pressed()[pygame.K_s]:
        separate(agent, all_chemicals, True)
    if pygame.key.get_pressed()[pygame.K_a]:
        reset()
        add_demonstration()
    if pygame.key.get_pressed()[pygame.K_m]:
        bucket = Merge()
        annote = bucket.name.get()
        merge_nodes(annote)
    if pygame.key.get_pressed()[pygame.K_f]:
        if tasks:
            demonstrations.append(tasks)
        for tasks in demonstrations:
            reset()
            for task_node in tasks:
                # print(task_node.pos,task_node.action)
                agent.goto(task_node.pos, clear)
                action = task_node.action
                if action == 'pick_up':
                    pick_up_chemical(agent, all_chemicals, tasks, False)
                elif action == 'drop_down':
                    drop_off_chemical(agent, tasks, False)
                elif action == 'react':
                    react(agent, all_chemicals, False)
                elif action == 'separate':
                    separate(agent, all_chemicals, False)
    if pygame.key.get_pressed()[pygame.K_z]:
        reset()
        # print(parent_nodes)
        for parent_node in parent_nodes:
            # print(parent_node.children)
            for task_node in parent_node.children:
                agent.goto(task_node.pos, clear)
                action = task_node.action
                if action == 'pick_up':
                    pick_up_chemical(agent, all_chemicals, tasks, False)
                elif action == 'drop_down':
                    drop_off_chemical(agent, tasks, False)
                elif action == 'react':
                    react(agent, all_chemicals, False)
                elif action == 'separate':
                    separate(agent, all_chemicals, False)
    if pygame.key.get_pressed()[pygame.K_n]:
        if parent_nodes:
            if parent_index == 0:
                reset()
            parent_node = []
            for pn in parent_nodes:
                if pn.annotation[0] == hierarchy.order[parent_index]:
                    parent_node = pn
            for task_node in parent_node.children:
                if 'react' in task_node.action:
                    prompt = Prompt()
                    s = prompt.name.get().split(',')
                    for i, c_name in enumerate(s):
                        chemical = all_chemicals[int(c_name)]
                        # chemical = key_to_chemical[c_name]
                        parent_node.children[i].pos = chemical.get_pos()
                    # print(chemical.get_pos())
            for task_node in parent_node.children:
                agent.goto(task_node.pos, clear)
                action = task_node.action
                if action == 'pick_up':
                    pick_up_chemical(agent, all_chemicals, tasks, False)
                elif action == 'drop_down':
                    drop_off_chemical(agent, tasks, False)
                elif action == 'react':
                    react(agent, all_chemicals, False)
                elif action == 'separate':
                    separate(agent, all_chemicals, False)
            parent_index += 1
    if pygame.key.get_pressed()[pygame.K_i]:
        reset()
        instruction = Instruction()
        hierarchy.order = instruction.name.get().split(',')

    for station in all_stations:
        station.get_actions()

    agent.display()
    agent.draw(screen)
    agent.handle_keys()
    pygame.display.update()
    clear()
    clock.tick(10)
