import pygame
from collections import defaultdict
class Agent(object):
    def __init__(self,screen,step):
        self.x = 250
        self.y = 250
        self.rect = pygame.rect.Rect((self.x, self.y, 16,16))
        self.learned_tasks = defaultdict(dict)
        self.prev_level = None
        self.current_level = self.learned_tasks
        self.state = None
        self.chemicals = []
        self.screen = screen
        self.step = step


    def get_pos(self):
        return [self.x,self.y]

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
            self.rect.move_ip(-self.step, 0)
            self.x -= self.step
        elif key[pygame.K_RIGHT]:
            self.rect.move_ip(self.step, 0)
            self.x += self.step
        elif key[pygame.K_UP]:
            self.rect.move_ip(0, -self.step)
            self.y -= self.step
        elif key[pygame.K_DOWN]:
            self.rect.move_ip(0, self.step)
            self.y += self.step
        if key[pygame.K_SPACE]:
            pass
    
    def learn_task(self,task):
        if task not in self.current_level:
            self.current_level[task] = {}
        self.prev_level = self.current_level
        self.current_level = self.current_level[task]

    def draw(self, surface):
        pygame.draw.rect(self.screen, (0, 0, 128), pygame.rect.Rect((self.x, self.y, 16,16)))

    def goto(self, pos, clear):
        x,y = pos
        clock = pygame.time.Clock()
        while abs(self.x - x) > 1:
            clear()
            if self.x > x:
                self.draw(self.screen)
                self.rect.move_ip(-self.step, 0)
                self.x -= self.step
                pygame.display.update()
            else:
                self.draw(self.screen)
                self.rect.move_ip(self.step, 0)
                self.x += self.step
                pygame.display.update()
            clock.tick(10)
        while abs(self.y - y) > 1:
            clear()
            if self.y > y:
                self.draw(self.screen)
                self.rect.move_ip(0, -self.step)
                self.y -= self.step
                pygame.display.update()
            else:
                self.draw(self.screen)
                self.rect.move_ip(0, self.step)
                self.y += self.step
                pygame.display.update()
            clock.tick(10)

    def pick_up(self,chemical):
        if chemical not in self.chemicals:
            self.chemicals.append(chemical)
            chemical.being_hold = True

    def display(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            print('get agent states: ', self.prev_level)