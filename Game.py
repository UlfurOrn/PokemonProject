import pygame

class Game:
    SIZE = (640, 480)
    FRAME_RATE = 60

    def __init__(self):
        self.setup()


    def setup(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Pokemon Project")

        self.clock = pygame.time.Clock()
    

    def start(self):
        self.do_loop = True

        while self.do_loop:

            self.handle_events()
            pygame.display.flip()

            self.clock.tick(self.FRAME_RATE)
    


    def handle_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.do_loop = False
