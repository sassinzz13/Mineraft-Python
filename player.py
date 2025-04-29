import pygame

SPEED = 300
WIDTH = 200
HEIGHT = 150
class Player:
    def __init__(self, x, y):
        # initialize the sprite
        pygame.sprite.Sprite.__init__(self)
        DirtBlockImage = pygame.image.load('assets/1.21.4/blocks/dirt.png').convert_alpha()
        size = (WIDTH, HEIGHT)
        self.image = pygame.transform.scale(DirtBlockImage, size)
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)
        self.speed = SPEED
        
       

    def handle_input(self, keys, dt, obstacles):
        movement = pygame.Vector2(0, 0)
        if keys[pygame.K_w]:
            movement.y -= self.speed * dt
        if keys[pygame.K_s]:
            movement.y += self.speed * dt
        if keys[pygame.K_a]:
            movement.x -= self.speed * dt
        if keys[pygame.K_d]:
            movement.x += self.speed * dt
        
        # collision detector
        self.position.x += movement.x
        self.rect.centerx = self.position.x
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                if movement.x > 0:
                    self.rect.right = obstacle.left
                elif movement.x < 0:
                    self.rect.left = obstacle.right
                self.position.x = self.rect.centerx

        self.position.y += movement.y
        self.rect.centery = self.position.y
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                if movement.y > 0:  
                    self.rect.bottom = obstacle.top
                elif movement.y < 0:  
                    self.rect.top = obstacle.bottom
                self.position.y = self.rect.centery
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
