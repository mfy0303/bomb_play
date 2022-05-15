import pygame

class Square(pygame.sprite.Sprite):
	def __init__(self,bg_size,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("bomb_bg.png").convert_alpha()
		self.mouse_image=pygame.image.load("bomb_bg2.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.width,self.height = bg_size[0],bg_size[1]
		self.rect.left,self.rect.bottom = self.width-x,self.height-y
		self.active=True
		self.mask=pygame.mask.from_surface(self.image)
	
