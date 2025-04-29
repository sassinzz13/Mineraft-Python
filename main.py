import pygame
from player import Player
from block import SquareBlock

# ------------------ Constants ------------------ #
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
FPS = 60

# ------------------ Initialization ------------------ #
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minecraft in Python')
clock = pygame.time.Clock()
running = True
dt = 0

# ------------------ Game Objects ------------------ #
# Create player instance
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Create block instances
squares = pygame.sprite.Group()
squares.add(SquareBlock(500, 500))
squares.add(SquareBlock(900, 500))

# ------------------ Game Loop ------------------ #
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    player.handle_input(keys, dt)

    # Update game objects
    squares.update()

    # Draw everything
    screen.fill("blue")
    player.draw(screen)
    squares.draw(screen)

    # Update the display
    pygame.display.flip()

    # Delta time (frame-independent movement)
    dt = clock.tick(FPS) / 1000

pygame.quit()

# To do for now
# Make a movable player 
# Add sprite images to the block
# Add collision
# Add camera movement
# Make the block 3D
