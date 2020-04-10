import pygame

import Config
from Controls import Controls

class Player(pygame.sprite.Sprite):
    SIZE = Config.SCALE
    IMAGE_SIZE = (Config.SCALE, Config.SCALE)

    def __init__(self):
        super(Player, self).__init__()

        self.load_images()

        # Load and resize image to IMAGE_SIZE
        self.image = self.stand_south

        # Create rect variable for draw call in Game loop
        self.rect = self.image.get_rect()

    

    def load_images(self):
        self.stand_south = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_S.png").convert_alpha())
        self.stand_north = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_N.png").convert_alpha())
        self.stand_west = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_W.png").convert_alpha())
        self.stand_east = self.rescale_image(pygame.image.load("Sprite_Sheet/Stand/Stand_E.png").convert_alpha())
    

    def rescale_image(self, image):
        return pygame.transform.scale(image, self.IMAGE_SIZE)



    def walk(self, direction):
        if direction == Controls.UP:
            self.rect.y -= self.SIZE
            self.image = self.stand_north
        elif direction == Controls.DOWN:
            self.rect.y += self.SIZE
            self.image = self.stand_south
        elif direction == Controls.LEFT:
            self.rect.x -= self.SIZE
            self.image = self.stand_west
        elif direction == Controls.RIGHT:
            self.rect.x += self.SIZE
            self.image = self.stand_east