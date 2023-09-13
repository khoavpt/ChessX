"""
ui.py: Handle the user interface
abc123
"""
import pygame
from board import Board
from pieces import Piece

board = Board()

pygame.init()
# screen = pygame.display.set_mode((1080, 720))
WINDOWWIDTH = 1080
WINDOWHEIGHT = 720
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('ChessX')
clock = pygame.time.Clock()
running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen, (0, 0, 255),
                 [100, 100, 400, 100])

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()