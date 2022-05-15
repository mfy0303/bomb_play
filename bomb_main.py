import pygame
import sys 
import find_bomb
from pygame.locals import*

pygame.init
size = width, height = 535,535
w=525
h=465
clock=pygame.time.Clock()
bg_color = (230,230,230)
square_index_x=0
square_index_y=0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ATTENTION!THERE ARE MANY BOMBS!")
square_flag=True
def squares(group):
	global w
	global h
	for p in range(8):
		for i in range(8):
			square=find_bomb.Square(size,w,h)
			group.add(square)
			w=w-65
		h=h-65
		w=525
def mouse_pos_square(a,b):
	r=(a-10) // 65
	u=(b-10) // 65
	if r*65==a:
		if u*65==b:
			return r,u
	elif r*65 < a:
		if u*65 < b:
			return r+1,u+1
add_square=pygame.sprite.Group()
squares(add_square)
running=True
while running:
	screen.fill(bg_color)
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = False
	elif event.type == pygame.MOUSEMOTION:
		x,y = event.pos
		square_index_x,square_index_y = mouse_pos_square(x,y)
	elif event.type == pygame.MOUSEBUTTONDOWN:
		square_flag=False
	# print(square_index_x,square_index_y)
	for each in add_square:
		screen.blit(each.image,each.rect)
		x3,y3=mouse_pos_square(each.rect.left+5,each.rect.top+5)
		# if x3==square_index_x:
			# if y3==square_index_y:
				# screen.blit(each.mouse_image,each.rect)
		if square_flag == False:
			if x3==square_index_x:
				if y3==square_index_y:
					each.image=pygame.image.load("no_bomb.png").convert_alpha()
					square_flag=True	
	pygame.display.flip()
	clock.tick(120)	
	
