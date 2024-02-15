import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.board = pygame.image.load("demo.png")
        self.rect = self.board.get_rect()
        self.rect.topleft = (0, 0)
        
    def update(self):
        pass