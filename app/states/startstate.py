from game import Game
from states.state import State
from constants import *
import pygame
from algo.pieces import Piece
from states.playstate import PlayState
from pygame.locals import *

class StartState(State):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.white_button_rect = pygame.Rect(200, 280, 80, 80)
        self.black_button_rect = pygame.Rect(360, 280, 80, 80)
        self.font = pygame.font.SysFont(FONT, 80, bold=True)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)

            elif event.type == MOUSEBUTTONDOWN:
                if self.white_button_rect.collidepoint(event.pos):
                    self.game.playerColor = Piece.WHITE
                elif self.black_button_rect.collidepoint(event.pos):
                    self.game.playerColor = Piece.BLACK 

                if self.game.playerColor is not None:
                    self.game.pushState(PlayState(self.game))


    def draw(self) -> None:
        self.drawBoardGame()
        
        # Vẽ nền của nút trắng
        pygame.draw.rect(self.game.window, (255, 255, 255), self.white_button_rect)
        
        # Vẽ viền cho nút trắng (màu đen) với độ dày 2 pixel
        pygame.draw.rect(self.game.window, (0, 0, 0), self.white_button_rect, 2)
        
        # Vẽ nền của nút đen
        pygame.draw.rect(self.game.window, GRAY, self.black_button_rect)
        
        # Vẽ viền cho nút đen (màu trắng) với độ dày 2 pixel
        pygame.draw.rect(self.game.window, (0, 0, 0), self.black_button_rect, 2)

        self.game.window.blit(self.game.images["wK"], (self.white_button_rect.centerx - 35, self.white_button_rect.centery - 35))
        self.game.window.blit(self.game.images["bK"], (self.black_button_rect.centerx - 35, self.black_button_rect.centery - 35))


        # Vẽ dòng chữ "Choose player" giữa hai nút
        choose_player_text = self.font.render("Choose player", True, (0, 0, 0))
        choose_player_rect = choose_player_text.get_rect(centerx=(self.white_button_rect.centerx + self.black_button_rect.centerx) // 2, centery=200)
        
        # Vẽ dòng chữ "Choose player"
        self.game.window.blit(choose_player_text, choose_player_rect)

    def drawBoardGame(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(self.game.window, WHITE, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
                else:
                    pygame.draw.rect(self.game.window, GRAY, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))