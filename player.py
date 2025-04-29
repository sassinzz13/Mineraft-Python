# player.py
import pygame

class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(200, 150)
        self.color = "black"
        self.speed = 300

    def handle_input(self, keys, dt):
        if keys[pygame.K_w]:
            self.position.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.position.y += self.speed * dt
        if keys[pygame.K_a]:
            self.position.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.position.x += self.speed * dt

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))
