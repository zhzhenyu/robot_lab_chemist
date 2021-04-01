import pygame

class Station(object):
	def __init__(self,x,y,screen,width,height,actions):
		self.actions = set(actions)
		self.screen = screen
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rect = pygame.Rect(x, y, width, height)
		pygame.draw.rect(screen, (120,120,120), self.rect)

	def add_action(self,action):
		self.actions.add(action)

	def draw(self):
		pygame.draw.rect(self.screen, (120,120,120), self.rect)

	def get_actions(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.key.get_pressed()[pygame.K_g]:
			print(self.actions)
			
