import pygame

# square class to show the block image
class DirtBlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        DirtBlockImage = pygame.image.load('assets/1.21.4/blocks/dirt.png').convert_alpha()
        size = (200, 150)
        self.image = pygame.transform.scale(DirtBlockImage, size)
        self.rect = self.image.get_rect(center=(x, y))
        # detects collision for block to stop player from going no clipping
        self.collision_detector = pygame.Rect(self.rect.topleft, self.rect.size)
class BlockImage():
    pass
    
        
        