import pygame

from scripts.camera import Camera
from scripts.obj import *
from scripts.player import Player
from scripts.scene import Scene
from scripts.settings import *

TILE_MAPPING = {
    "x": "assets/map/tile.png",
    "w0": "assets/map/wall_side0.png",
    "w1": "assets/map/wall_side1.png",
    "w2": "assets/map/wall_side2.png",
    "c0": "assets/map/corner0.png",
    "c1": "assets/map/corner1.png",
    "c2": "assets/map/corner2.png",
    "c3": "assets/map/corner3.png",
    "nw": "assets/map/noramal_wall.png",
    "l0": "assets/map/l0.png",
    "l1": "assets/map/l1.png",
    "l2": "assets/map/l2.png",
    "l3": "assets/map/l3.png"
}


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.window.fill((0,0,255))

        self.all_sprites = Camera()
        self.colision_sprites = pygame.sprite.Group()
        self.music = pygame.mixer.Sound("assets/sounds/buzz.mp3")
        self.music.play(-1)


        self.generate_map()
        self.player = Player([200, 400], [200/7, 400/7],self.colision_sprites, self.all_sprites)

    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                if col in TILE_MAPPING:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    if col == "x":
                        Obj("assets/map/tile.png", [x, y], self.all_sprites)
                    if col == "w0":
                        Wall("assets/map/wall_side0.png", "w0", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "w1":
                        Wall("assets/map/wall_side1.png", "w1", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "w2":
                        Wall("assets/map/wall_side2.png", "w2", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "c0":
                        Wall("assets/map/corner0.png", "c0", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "c1":
                        Wall("assets/map/corner1.png", "c1", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "c2":
                        Wall("assets/map/corner2.png", "c2", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "c3":
                        Wall("assets/map/corner3.png", "c3", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "nw":
                        Wall("assets/map/noramal_wall.png", "nw", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "l0":
                        Wall("assets/map/l0.png", "l0", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "l1":
                        Wall("assets/map/l1.png", "l1",[x, y], self.all_sprites, self.colision_sprites)
                    if col == "l2":
                        Wall("assets/map/l2.png", "l2",[x, y], self.all_sprites, self.colision_sprites)
                    if col == "l3":
                        Wall("assets/map/l3.png", "l3",[x, y], self.all_sprites, self.colision_sprites)
    def events(self, event):
        pass

    def draw(self):
        self.window.fill((14,14,14))
        self.all_sprites.custom_draw(self.player)

    def update(self):
        self.all_sprites.update()