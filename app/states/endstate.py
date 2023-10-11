from game import Game
from states.state import State
from constants import *
import pygame
from algo.pieces import Piece
from pygame.locals import *

class EndState(State):
    def __init__(self, game: Game, winner) -> None:
        super().__init__(game)
        self.restart_button_rect = pygame.Rect(280, 280, 80, 80)
        self.button_image = None
        self.loadImage()
        self.font = pygame.font.SysFont(FONT, 80, bold=True)
        self.winner = winner

    def loadImage(self) -> None:
        image = pygame.image.load("assets/PA.png")
        self.button_image = pygame.transform.scale(image, (80, 80))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == MOUSEBUTTONDOWN:
                if self.restart_button_rect.collidepoint(event.pos):
                    self.game.newGame()
                    


    def draw(self) -> None:
        pygame.draw.rect(self.game.window, (255, 255, 255), self.restart_button_rect)

        self.game.window.blit(self.button_image, self.restart_button_rect.topleft)
        
        # Vẽ viền cho nút trắng (màu đen) với độ dày 2 pixel
        pygame.draw.rect(self.game.window, 'black', self.restart_button_rect, 2)

        end_text = None
        if self.winner == 'h':
            endtext = self.font.render("You Win", True, 'red')
        elif self.winner == 'a':
            endtext = self.font.render("You Lose", True, 'red')
        endrect = endtext.get_rect(centerx=WINDOW_HEIGHT // 2, centery=200)
        
        # Vẽ dòng chữ "Choose player"
        self.game.window.blit(endtext, endrect)