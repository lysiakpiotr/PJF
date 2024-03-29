import pygame

TILE_SIZE = 85

class Player(pygame.sprite.Sprite):
    def __init__(self, name, number, player_x_pos, player_y_pos):
        super().__init__()          
        self.name = name
        self.number = number
        self.DEFAULT_X = 86
        self.DEFAULT_Y = 848
        
        self.turn_ended = True
        #wyswietl 1 odpowiedni pionek spośród 6
        self.player_surf = pygame.image.load(f"pionki/pionek_{number}.png")
        self.player_rect = self.player_surf.get_rect(topleft = (self.DEFAULT_X, self.DEFAULT_Y))
        self.player_rect.x = player_x_pos
        self.player_rect.y = player_y_pos
        self.current_tile = 1
        
        

    @staticmethod    
    def create_players(number):
        DEFAULT_X = 86
        DEFAULT_Y = 848
        if number not in range(2, 7): 
            print("Podaj poprawną liczbę graczy")
            return

        players = []
        


        for x in range(number):
            name = input(f"Podaj nazwę gracza nr. {x+1}: ")

            player = Player(name, x+1, DEFAULT_X, DEFAULT_Y)
            players.append(player)

        return players 



    def player_input(self, screen, dice, dt):

        key = pygame.key.get_pressed()
        
        if key[pygame.K_d]:
            #przesuń pionek o wylosowaną liczbę
            if dice.is_rolling:
                return
            tiles_to_move = dice.roll(screen, (dice.dice_x_pos, dice.dice_y_pos))
            self.update(tiles_to_move, dt)
            return True
            
        elif key[pygame.K_t]:
            #przyjmij wyzwanie
            good_rolls = {
                12: 2,
                16: 6,
                45: 4,
                73: 5,
                82: 3,
                89: 1
            }

            if good_rolls[self.current_tile] == tiles_to_move:
                #przesuń pionek o wylosowaną liczbę
                
                #self.move(self.current_tile, tiles_to_move)
                self.update(self.current_tile, 2)

                #i dodaj rzut kostką
                tiles_to_move = dice.roll()
                self.update(self.current_tile, tiles_to_move)

            return True

        elif key[pygame.K_t]:
            #odrzuć wyzwanie
            return True
        
    
    def get_tile_position(self, tiles_to_move):
        destinated_tile = self.current_tile + tiles_to_move
        if destinated_tile > 100:
            return 100
        
        if (destinated_tile//self.current_tile)%2 == 0:
            destinated_x = self.player_rect.x + (destinated_tile - 1)%10 * TILE_SIZE
        else:
            destinated_x = self.player_rect.x - (destinated_tile - 1)%10 * TILE_SIZE
        destinated_y = self.player_rect.y - (destinated_tile - 1)//10 * TILE_SIZE
        return (destinated_x, destinated_y)

    def update(self, tiles_to_move, dt):
        if tiles_to_move == 0 or self.current_tile + tiles_to_move > 100:
            return
        

        start_x, start_y = self.player_rect.x, self.player_rect.y
        '''modulo = self.current_tile%10
        div = self.current_tile//10'''
        if (self.current_tile + tiles_to_move)//10 == self.current_tile//10:
            #lewo/prawo
            end_x, end_y = self.get_tile_position(tiles_to_move)
            #góra
            end_x, end_y = self.get_tile_position(tiles_to_move)
            #lewo/prawo
            end_x, end_y = self.get_tile_position(tiles_to_move)
            
        else:
            end_x, end_y = start_x, start_y
        

        '''if not (abs(self.player_rect.x - end_x) < 1 and abs(self.player_rect.y - end_y) < 1):   #jeśli gracz nie jest w miejscu docelowym
            # Odległość do pokonania w każdej klatce
            distance_x = (end_x - start_x) / dt
            distance_y = (end_y - start_y) / dt

            self.player_rect.x += distance_x * dt
            self.player_rect.y += distance_y * dt
            # Zaokrąglenie do najbliższej liczby całkowitej
            self.player_rect.x = round(self.player_rect.x)
            self.player_rect.y = round(self.player_rect.y)
            print(f"gracz {self.number} na polu {self.current_tile} przesuwa się z {start_x, start_y} na {end_x, end_y}")
        else:
            self.current_tile = self.current_tile + tiles_to_move'''

        distance_x = end_x - start_x
        distance_y = end_y - start_y

        self.player_rect.x += distance_x
        self.player_rect.y += distance_y
            
        pygame.display.update(self.player_rect)
        
        return



    '''def update(self, tiles_to_move):
        if tiles_to_move == 0:
            return
        print(f"rusz gracza nr. {self.number} o {tiles_to_move} pól z pola {self.current_tile}")
        if self.current_tile + tiles_to_move > 100:
            return
        
        for _ in range(tiles_to_move):

            if self.current_tile%10 == 0:
                #przesuń w górę
                print("przesuń w górę")
                for _ in range(TILE_SIZE):
                    self.player_rect.y -= 1
                    #pygame.display.flip()
                pygame.time.delay(100)
                self.current_tile += 1

            elif self.current_tile//10 in [0, 2, 4, 6, 8]:
                #przesuń w prawo
                print("przesuń w prawo")
                for _ in range(TILE_SIZE):
                    self.player_rect.x += 1
                    #pygame.display.flip()
                pygame.time.delay(100)
                self.current_tile += 1

            elif self.current_tile//10 in [1, 3, 5, 7, 9]:
                #przesuń w lewo
                print("przesuń w lewo")
                for _ in range(TILE_SIZE):
                    self.player_rect.x -= 1
                    #pygame.display.flip()
                pygame.time.delay(100)
                self.current_tile += 1
            pygame.display.update(self.player_rect)
        pygame.display.update(self.player_rect)
        pygame.time.delay(100)

        #weze
        if self.current_tile == 26:
            self.current_tile = 4
            self.player_rect.x -= 2*TILE_SIZE
            self.player_rect.y += 2*TILE_SIZE
        elif self.current_tile == 62:
            self.current_tile = 21
            self.player_rect.x -= 1*TILE_SIZE
            self.player_rect.y += 4*TILE_SIZE
        elif self.current_tile == 55:
            self.current_tile = 47
            self.player_rect.x += 1*TILE_SIZE
            self.player_rect.y += 1*TILE_SIZE
        elif self.current_tile == 68:
            self.current_tile = 48
            self.player_rect.y += 2*TILE_SIZE
        elif self.current_tile == 85:
            self.current_tile = 65
            self.player_rect.y += 2*TILE_SIZE
        #drabiny
        elif self.current_tile == 13:
            self.current_tile = 46
            self.player_rect.x -= 2*TILE_SIZE
            self.player_rect.y -= 3*TILE_SIZE
        elif self.current_tile == 19:
            self.current_tile = 58
            self.player_rect.x += 1*TILE_SIZE
            self.player_rect.y -= 4*TILE_SIZE
        elif self.current_tile == 53:
            self.current_tile = 72
            self.player_rect.x += 1*TILE_SIZE
            self.player_rect.y -= 2*TILE_SIZE
        elif self.current_tile == 64:
            self.current_tile = 83
            self.player_rect.x -= 2*TILE_SIZE
            self.player_rect.y -= 2*TILE_SIZE
        elif self.current_tile == 66:
            self.current_tile = 75
            self.player_rect.y -= 1*TILE_SIZE


        pygame.display.flip()'''
        



