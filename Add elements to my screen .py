import pygame
pygame.init()
screen = pygame.display.set_mode((600,300)) 
rect = pygame.Rect(50,50,100,50) 
draw_rect = True
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((1,1,1)) 
    if draw_rect:
        pygame.draw.rect(screen,(0,255,0),rect) 
    pygame.display.flip()