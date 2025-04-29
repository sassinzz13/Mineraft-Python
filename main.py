import pygame
from player import Player
from block import DirtBlock

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
player = Player(200,200)

# Create block instances
squares = pygame.sprite.Group()
squares.add(DirtBlock(500, 500))
squares.add(DirtBlock(1000, 500))
# Collision detection
obstacles = [block.rect for block in squares]

# ------------------ Game Loop ------------------ #
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle input
    keys = pygame.key.get_pressed()
    # detects collision
    player.handle_input(keys, dt, obstacles)

    # Update game objects
    squares.update()

    # Draw everything
    screen.fill("blue")
    player.draw(screen) # Spawn player
    squares.draw(screen) # Spawn blocks
    
    # Update the display
    pygame.display.flip()

    # Delta time (frame-independent movement)
    dt = clock.tick(FPS) / 1000

pygame.quit()

# To do for now
# Make a movable player ✅
# Add sprite images to the block ✅
# Add collision
# Add camera movement
# Make the block 3D
