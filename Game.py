import pygame

import Config
from Controls import Controls
from Player import Player

class Game:
    SIZE = (640, 480)
    FRAME_RATE = 8

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

        self.player = Player()
        self.sprite_list.add(self.player)
    

    def start(self):
        self.do_loop = True

        while self.do_loop:

            self.handle_events()
            self.do_stuff()

            self.update()

            self.screen.fill((255,255,255))
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
            
            elif event.type == pygame.KEYDOWN:
                #self.handle_inputs(event.key)
                pass


    def handle_inputs(self, key):
        if key == pygame.K_w:
            self.player.walk(Controls.UP)
        elif key == pygame.K_s:
            self.player.walk(Controls.DOWN)
        elif key == pygame.K_a:
            self.player.walk(Controls.LEFT)
        elif key == pygame.K_d:
            self.player.walk(Controls.RIGHT)
    

    def do_stuff(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.walk(Controls.UP)
        elif keys[pygame.K_s]:
            self.player.walk(Controls.DOWN)
        elif keys[pygame.K_a]:
            self.player.walk(Controls.LEFT)
        elif keys[pygame.K_d]:
            self.player.walk(Controls.RIGHT)