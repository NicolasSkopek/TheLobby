import pygame

from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

TILE_MAPPING = {
    "x": "assets/map/tile.png",
    "w0": "assets/map/wall_side0.png",
    "w1": "assets/map/wall_side1.png",
    "w2": "assets/map/wall_side2.png"
}


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.window.fill((0,0,255))

        self.all_sprites = pygame.sprite.Group()  # Certifica que o grupo de sprites foi inicializado
        self.music = pygame.mixer.Sound("assets/sounds/buzz.mp3")
        self.music.play(-1)

        self.generate_map()

    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                if col in TILE_MAPPING:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    Obj(TILE_MAPPING[col], [x, y], self.all_sprites)

    def events(self, event):
        pass

    def draw(self):
        self.window.fill((14,14,14))
        self.all_sprites.draw(self.window)

    def update(self):
        self.all_sprites.update()