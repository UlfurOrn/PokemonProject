import pygame

from Player import Player

class Game:
    SIZE = (640, 480)
    FRAME_RATE = 60

    def __init__(self):
        self.setup_pygame()
        self.setup_sprites()


    def setup_pygame(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Pokemon Project")

        self.clock = pygame.time.Clock()
    

    def setup_sprites(self):
        self.sprite_list = pygame.sprite.Group()

        self.sprite_list.add(Player())
    

    def start(self):
        self.do_loop = True

        while self.do_loop:

            self.handle_events()
            self.update()

            self.sprite_list.draw(self.screen)

            pygame.display.flip()

            # Set framerate to 60
            self.clock.tick(self.FRAME_RATE)
    

    def update(self):
        self.sprite_list.update()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.do_loop = False
