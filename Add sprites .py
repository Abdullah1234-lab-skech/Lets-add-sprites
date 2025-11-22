import pygame
pygame.init() 
screen = pygame.display.set_mode((400, 300))
done = False
rect = pygame.Rect(50, 50, 100, 50)
class sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width , height])
        self.image.fill(color)
        self.rect = self.image.get_rect() 
my_sprite = sprite((255, 0, 0), 50, 50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(my_sprite)
pygame.sprite.Rect ; width = 50  
pygame.sprite.Rect; height = 50
my_sprite.rect.x = 50
my_sprite.rect.y = 50
pygame.draw.rect(screen, (0 , 255 , 0), rect) 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((1, 1, 1))
    all_sprites_list.draw(screen)
    pygame.display.flip()