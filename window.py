import pygame



class Window:
    def __init__(self, type):
        self.type = type
        pass

    def draw(self):
        if self.type == "intro":
            #wyswietl okno z wyborem liczby graczy od 2 do 6 i przyciskami


            
            pass

        elif self.type == "quest":
            #wyswietl okno z decyją o akceptacji lub odrzuceniu wyzwania
            pass

        elif self.type == "scoreboard":
            #wyswietl okno z wynikami
            pass

        pass

    def display(self):
        pass

    def update(self):
        pass

    def handle_events(self):
        pass