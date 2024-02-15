import pygame
from dice import Dice
from player import Player

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 1020

class Main:    
    def __init__(self):          
        self.FONT = pygame.font.SysFont("None", 50)
        self.TILE_SIZE = 85
        self.dice = Dice()
        self.current_player_index = 0

    def main(self):        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()
        background = pygame.image.load("demo.png")
        icon = pygame.image.load("ikona.png")

        pygame.display.set_icon(icon) 
        pygame.display.set_caption("Snakes and Ladders")

        # Tekst, który wyświetla się na górze
        text_surface = self.FONT.render("Snakes and Ladders", False, 'Dark Green')   

        num_players = int(input("Podaj liczbę graczy (od 2 do 6): "))
        players_list = Player.create_players(num_players)
        current_player = players_list[0]
        current_player_index = 1

        running = True

        while running:                         
            screen.fill((255, 255, 255))
            
            key = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                if key[pygame.K_ESCAPE]:
                    running = False

            # Ustawienie tła i tekstu
            screen.blit(background, (0, 0))
            screen.blit(text_surface, (300, 50))

            # Obsługa tury aktualnego gracza
            current_player = players_list[self.current_player_index]
            current_player.turn_ended = current_player.player_input(screen, self.dice)
            

            # Rysowanie graczy
            for player in players_list:
                screen.blit(player.player_surf, (player.player_rect.x, player.player_rect.y))
            pygame.display.update()

            # Sprawdzenie warunków zmiany tury
            if current_player.turn_ended:
                self.current_player_index = (self.current_player_index + 1) % len(players_list)
                players_list[self.current_player_index].turn_ended = False
            
            pygame.display.update(current_player.player_rect)
            clock.tick(60)  # 60 fps
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    main = Main()
    main.main()