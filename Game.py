import pygame

import Config
from Controls import Controls
from Player import Player
from World import World

class Game:
    SIZE = (640, 480)
    FRAME_RATE = Config.FPS

    def __init__(self):
        self.setup_pygame()
        self.setup_sprites()
        self.setup_world()


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
            self.handle_inputs()

            self.update()

            self.draw_world()
            self.sprite_list.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(self.FRAME_RATE)
    
        pygame.quit()


    def update(self):
        self.sprite_list.update()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.do_loop = False
    

    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            is_running = True
        else:
            is_running = False
            
        if keys[pygame.K_w]:
            self.player.run(Controls.UP) if is_running else self.player.walk(Controls.UP)
        elif keys[pygame.K_s]:
            self.player.run(Controls.DOWN) if is_running else self.player.walk(Controls.DOWN)
        elif keys[pygame.K_a]:
            self.player.run(Controls.LEFT) if is_running else self.player.walk(Controls.LEFT)
        elif keys[pygame.K_d]:
            self.player.run(Controls.RIGHT) if is_running else self.player.walk(Controls.RIGHT)

    


    def setup_world(self):
        self.world = World()

    def draw_world(self):
        self.world.draw(self.screen)