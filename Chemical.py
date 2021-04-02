import pygame

class Chemical(object):

	def __init__(self,x,y,screen,width,height,color,components):
		self.x = x
		self.y = y
		self.screen = screen
		self.width = width
		self.height = height
		self.color = color
		self.being_hold = False
		self.components = components
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(screen, self.color, self.rect)

	def update_pos(self,x,y):
		self.x=x
		self.y=y
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def get_pos(self):
		return [self.x,self.y]

	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)