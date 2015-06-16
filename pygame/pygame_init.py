import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Lalka")

pygame.display.update()
# my code over here

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

pygame.quit()
quit()
