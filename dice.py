import pygame
import time
from random import randint

class Dice(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.dices = {
            1: "kostka/kostka_1.png",
            2: "kostka/kostka_2.png",
            3: "kostka/kostka_3.png",
            4: "kostka/kostka_4.png",
            5: "kostka/kostka_5.png",
            6: "kostka/kostka_6.png"
        }
        self.dice = self.dices[1]       
        self.dice_x_pos = 0
        self.dice_y_pos = 200
        self.dice_surf = pygame.image.load(self.dice)
        self.rect = self.dice_surf.get_rect()
        self.is_rolling = False


    def roll(self, surface, position):
        number = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d and not self.is_rolling:
                    self.is_rolling = True
                    for _ in range(30):
                        number = randint(1, 6)
                        self.dice = self.dices[number]
                        #wyświetl kostkę
                        self.dice_surf = pygame.image.load(self.dice)
                        self.draw(surface, position)
                        pygame.display.update()
                        time.sleep(0.05)
                        #przesuń pionek o wylosowaną liczbę
                    self.is_rolling = False
                    time.sleep(0.5)
                return number
        self.is_rolling = False
        return 0           


    def draw(self, surface, position):
        surface.blit(self.dice_surf, position)
        pass