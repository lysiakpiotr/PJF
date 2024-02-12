import pygame

pygame.init()

SCREEN_WIDTH = 1020
SCREEN_HEIGHT = 1020

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
player1 = pygame.Rect((50, 50, 50, 50))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)

background = pygame.image.load("demo.png")
icon = pygame.image.load("ikona.png")
text_surface = game_font.render("Snakes and Ladders", False, 'Dark Green')   #false - antialiasing
player_surface = pygame.image.load("pionki/pionek_6.png")
player_x_pos = 87
player_y_pos = 848

pygame.display.set_icon(icon) 
running = True

pygame.display.set_caption("Snakes and Ladders")

while running:

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
        running = False
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

