import pygame

import time
import Config
from Controls import Controls

class Player(pygame.sprite.Sprite):
    SIZE = Config.SCALE
    IMAGE_SIZE = (Config.SCALE, Config.SCALE)
    WALK_ANIMATION_LENGTH = 16
    RUN_ANIMATION_LENGTH = 8

    def __init__(self):
        super(Player, self).__init__()

        # Load Animations and Images
        self.load_images()

        # Set starting image and rect
        self.direction = Controls.DOWN
        self.image = self.stand_south
        self.rect = self.image.get_rect()

        self.walking = False
        self.running = False



    def update(self):
        if self.running:
            self.do_run()

        elif self.walking:
            self.do_walk()
        
        else:
            self.do_stand()



    
    def walk(self, direction):
        if not self.walking and not self.running:
            self.walking = True
            self.direction = direction
            self.image_index = 0

    def run(self, direction):
        if not self.running:
            self.running = True
            self.direction = direction

            if self.walking:
                self.image_index = self.image_index // int(self.WALK_ANIMATION_LENGTH / self.RUN_ANIMATION_LENGTH)
            else:
                self.image_index = 0
    

    def do_walk(self):
        direction_dict = {Controls.UP:self.walk_north, Controls.DOWN:self.walk_south, Controls.LEFT:self.walk_west, Controls.RIGHT:self.walk_east}
        self.do_movement(direction_dict, self.WALK_ANIMATION_LENGTH)
    

    def do_run(self):
        direction_dict = {Controls.UP:self.run_north, Controls.DOWN:self.run_south, Controls.LEFT:self.run_west, Controls.RIGHT:self.run_east}
        self.do_movement(direction_dict, self.RUN_ANIMATION_LENGTH)


    def do_movement(self, direction_dict, animation_length):
        movement_dict = {Controls.UP:(0,-1), Controls.DOWN:(0,1), Controls.LEFT:(-1,0), Controls.RIGHT:(1,0)}

        image_list = direction_dict[self.direction]
        delta_x, delta_y = movement_dict[self.direction]
    
        self.image = image_list[self.image_index // int(animation_length / 4)]
        self.image_index += 1
        self.rect.x += delta_x * self.SIZE / animation_length
        self.rect.y += delta_y * self.SIZE / animation_length

        if self.image_index == animation_length:
            self.walking = False
            self.running = False
    

    def do_stand(self):
        direction_dict = {Controls.UP:self.stand_north, Controls.DOWN:self.stand_south, Controls.LEFT:self.stand_west, Controls.RIGHT:self.stand_east}
        self.image = direction_dict[self.direction]



    def rescale_image(self, image):
        return pygame.transform.scale(image, self.IMAGE_SIZE)


    def load_images(self):
        self.stand_north = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_N.png").convert_alpha())
        self.stand_south = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_S.png").convert_alpha())
        self.stand_east = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_E.png").convert_alpha())
        self.stand_west = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_W.png").convert_alpha())

        self.walk_north = [self.stand_north,
                           self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_N_1.png").convert_alpha()),
                           self.stand_north,
                           self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_N_2.png").convert_alpha())]
        self.walk_south = [self.stand_south,
                           self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_S_1.png").convert_alpha()),
                           self.stand_south,
                           self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_S_2.png").convert_alpha())]
        self.walk_east = [self.stand_east,
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_E_1.png").convert_alpha()),
                          self.stand_east,
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_E_2.png").convert_alpha())]
        self.walk_west = [self.stand_west,
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_W_1.png").convert_alpha()),
                          self.stand_west,
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Walk/Walk_W_2.png").convert_alpha())]
        
        self.run_north = [self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_N_1.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_N_2.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_N_3.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_N_4.png").convert_alpha())]
        self.run_south = [self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_S_1.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_S_2.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_S_3.png").convert_alpha()),
                          self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_S_4.png").convert_alpha())]
        self.run_east = [self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_E_1.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_E_2.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_E_3.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_E_4.png").convert_alpha())]
        self.run_west = [self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_W_1.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_W_2.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_W_3.png").convert_alpha()),
                         self.rescale_image(pygame.image.load("Sprite_Sheet/Run/Run_W_4.png").convert_alpha())]