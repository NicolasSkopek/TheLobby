import pygame
from scripts.obj import Obj

class Scene:

    def __init__(self):

        self.window = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.active = False

    def draw(self):
        self.all_sprites.draw(self.window)

    def update(self):
        self.all_sprites.update()