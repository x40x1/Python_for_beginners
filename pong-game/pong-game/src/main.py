import pygame
from game import Game

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Create a new game instance
game = Game(screen_width, screen_height, screen)

# Start the game loop
while True:
    # Handle events
    game.handle_events()

    # Update game state
    game.update()

    # Draw game on screen
    game.draw()

    # Check if game is over
    if game.game_over:
        game.reset()

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()