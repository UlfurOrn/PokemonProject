import pygame
import Config

class World:

    def __init__(self):
        self.load_tileset()
        self.world = []
        self.load_world()
    


    def load_world(self):
        file_object = open("world.txt", "r")
        for row in file_object:
            tiles = []

            for tile in row.split():
                tiles.append(tile)
            
            self.world.append(tiles)


    def draw(self, screen):
        for y, row in enumerate(self.world):
            for x, tile in enumerate(row):
                image = self.tile_dict[tile]
                rect = pygame.Rect(x * Config.SCALE, y * Config.SCALE, Config.SCALE, Config.SCALE)
                
                screen.blit(image, rect)
                


    def load_tileset(self):
        self.tile_dict = {}

        self.tile_dict["G"] = pygame.transform.scale(pygame.image.load("Sprite_Sheet/Tiles/grass.png"), (Config.SCALE,Config.SCALE))
        self.tile_dict["W"] = pygame.transform.scale(pygame.image.load("Sprite_Sheet/Tiles/water.png"), (Config.SCALE,Config.SCALE))