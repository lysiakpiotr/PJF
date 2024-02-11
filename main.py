import pygame

pygame.init()

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
player1 = pygame.Rect((50, 50, 50, 50))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)

background = pygame.image.load("plansza_plus_liczby_demo.png")
text_surface = game_font.render("Snakes and Ladders", False, 'Dark Green')   #false - antialiasing
player_surface = pygame.image.load("temp/pionek_szary_test.png")
player_x_pos = 100
player_y_pos = 870


run = True

pygame.display.set_caption("Snakes and Ladders")

while run:

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), player1)


    #obsluga klawiszy
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        #rzuć kostką
        pass
    elif key[pygame.K_t]:
        #przyjmij wyzwanie
        pass
    elif key[pygame.K_t]:
        #odrzuć wyzwanie
        pass
    elif key[pygame.K_ESCAPE]:
        run = False
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0, 0))
    screen.blit(text_surface, (300, 50))


    #player_x_pos += 1
    #player_y_pos += 1


    screen.blit(player_surface, (player_x_pos, player_y_pos))

    pygame.display.update()
    clock.tick(60)

#pygame.quit()




'''
class Main:
    def __init__(self) -> None:
        self.main()
        pass

    def main(self) -> None:
        pass
'''

