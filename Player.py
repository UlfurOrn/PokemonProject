import pygame

class Player(pygame.sprite.Sprite):
    IMAGE_SIZE = [128, 128]

    def __init__(self):
        super().__init__()

        # Load and resize image to IMAGE_SIZE
        self.image = pygame.image.load("Sprite_Sheet/Stand/Stand_S.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, self.IMAGE_SIZE)

        # Create rect variable for draw call in Game loop
        self.rect = self.image.get_rect()


    def