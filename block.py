import pygame

# square class to show the block image
class SquareBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet_image = pygame.image.load('assets/1.21.4/blocks/dirt.png').convert_alpha()
        self.image = sprite_sheet_image
        self.rect = self.image.get_rect()  
        self.size = pygame.Vector2(200, 150)
        self.rect.center = (x, y)
        # initialize the self.image to transform the scale of the sprite image
        self.image = pygame.transform.scale(sprite_sheet_image, (int(self.size.x), int(self.size.y)))
class BlockImage():
    pass
    
        
        