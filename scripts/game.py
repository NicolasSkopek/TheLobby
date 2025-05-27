import pygame

from scripts.camera import Camera
from scripts.enemy import Enemy
from scripts.gate import Gate
from scripts.obj import *
from scripts.player import Player
from scripts.scene import Scene
from scripts.settings import *
from scripts.panel import *
from scripts.text import Text

TILE_MAPPING = {
    "x1": "assets/map/tile.png",
    "w0": "assets/map/wall_side0.png",
    "w1": "assets/map/wall_side1.png",
    "w2": "assets/map/wall_side2.png",
    "c0": "assets/map/corner0.png",
    "c1": "assets/map/corner1.png",
    "nw": "assets/map/noramal_wall.png",
    "l0": "assets/map/l0.png",
    "l1": "assets/map/l1.png",
    "p1": "assets/map/pilar1.jpg",
    "p2": "assets/map/pilar2.jpg",
    "rg": "assets/map/poster_wall.png",
    "ww": "assets/map/windowns_wall.png",
    "h1": "assets/map/handl_wall.png",
    "br": "assets/map/bloodRight_wall.png",
    "sd": "assets/map/stDireita_wall.png",
    "bc": "assets/map/bloodCenterl_wall.png",
    "bl": "assets/map/bloodLeft_wall.png"
}


class Game(Scene):

    def __init__(self):
        super().__init__()
        self.window.fill((0, 0, 255))

        self.all_sprites = Camera()
        self.colision_sprites = pygame.sprite.Group()
        self.music = pygame.mixer.Sound("assets/sounds/buzz.mp3")
        self.death_sound = pygame.mixer.Sound("assets/sounds/death_sound.mp3")
        self.panel_sound = pygame.mixer.Sound("assets/sounds/panel_sound.mp3")
        self.music.play(-1)

        self.interaction_text = Text("assets/font/simsunb.ttf", 24, "press 'E' to interact", (255, 255, 255), (130, 20))
        self.interaction_timer = 200
        self.message_text = Text("assets/font/simsunb.ttf", 24, "you only got one chance", (255, 255, 255), (140, 20))
        self.message_timer = 420

        self.gameover = False

        self.fixed_panels = 0
        self.graph = 0
        self.show_graph = False
        self.generate_map()
        self.gate = Gate([1090, 256], [64, 64], "gate", self.all_sprites, self.colision_sprites)
        self.player = Player([208, 470], [200 / 8, 400 / 8], self.colision_sprites, self.all_sprites)
        self.enemy = Enemy([1394, 1443], [187 / 6, 486 / 6], self.colision_sprites, self.graph, self.player, self.all_sprites)
        ##self.enemy_2 = Enemy([1696, 450], [200 / 7, 400 / 7], self.colision_sprites, self.graph, self.player, self.all_sprites)

    def generate_map(self):
        for row_index, row in enumerate(MAP1):
            for col_index, col in enumerate(row):
                if col in TILE_MAPPING:
                    x = col_index * TILE_SIZE
                    y = row_index * TILE_SIZE
                    if col == "x1":
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
                    if col == "nw":
                        Wall("assets/map/noramal_wall.png", "nw", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "l0":
                        Wall("assets/map/l0.png", "l0", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "l1":
                        Wall("assets/map/l1.png", "l1", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "p1":
                        Wall("assets/map/pilar1.jpg", "p1", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "p2":
                        Wall("assets/map/pilar2.jpg", "p2", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "rg":
                        Wall("assets/map/poster_wall.png", "rg", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "ww":
                        Wall("assets/map/windowns_wall.png", "ww", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "h1":
                        Wall("assets/map/handl_wall.png", "h1", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "br":
                        Wall("assets/map/bloodRight_wall.png", "br", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "sd":
                        Wall("assets/map/stDireita_wall.png", "sd", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "bc":
                        Wall("assets/map/bloodCenterl_wall.png", "bc", [x, y], self.all_sprites, self.colision_sprites)
                    if col == "bl":
                        Wall("assets/map/bloodLeft_wall.png", "bl", [x, y], self.all_sprites, self.colision_sprites)

            Panel([813, 145], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)
            Panel([300, 1172], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)
            Panel([1232, 2255], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)
            Panel([2160, 1105], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)
            Panel([3308, 1170], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)
            Panel([4075, 1360], [108 / 3.3, 94 / 3.3], "panel", self.all_sprites, self.colision_sprites)


        self.graph = self.build_graph(MAP1)

    def build_graph(self, map_data):
        graph = {}

        for row in range(len(map_data)):
            for col in range(len(map_data[0])):
                if map_data[row][col] == "x1":
                    neighbors = []

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = col + dx, row + dy

                        if 0 <= ny < len(map_data) and 0 <= nx < len(map_data[0]):
                            if map_data[ny][nx] == "x1":
                                neighbors.append((nx, ny))

                    if neighbors:
                        graph[(col, row)] = neighbors

        return graph

    def fix_panel(self):
        self.fixed_panels += 1
        for sprite in self.colision_sprites:
            if isinstance(sprite, Panel):
                if sprite.rect.colliderect(self.player.rect) and sprite.fixed == False:
                    sprite.change_image()
                    self.panel_sound.play()
                    self.gate.change_image(self.fixed_panels)

    def finishGame(self):
        if self.gate.rect.colliderect(self.player.rect) and self.fixed_panels == 6:
            self.active = False
            self.stopAllSounds()
            self.fixed_panels = 0

    def game_over(self):
        if self.enemy.rect.colliderect(self.player.rect):
            self.death_sound.play()
            self.active = False
            self.gameover = True
            self.stopAllSounds()
            self.fixed_panels = 0

    def stopAllSounds(self):
        self.music.stop()
        self.player.running_sound.stop()
        ##self.enemy.scream_sound.stop()
        ##self.enemy.chase_sound.stop()

    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self.show_graph = not self.show_graph

            if event.key == pygame.K_e:
                self.finishGame()
                for sprite in self.colision_sprites:
                    if isinstance(sprite, Panel) and sprite.rect.colliderect(self.player.rect) and not sprite.fixed:
                        self.fix_panel()
                        break

    def draw(self):
        self.window.fill((14, 14, 14))
        self.all_sprites.custom_draw(self.player)

        if self.interaction_timer > 0:
            self.interaction_text.draw()

        if self.message_timer > 0 >= self.interaction_timer:
            self.message_text.draw()

        if self.show_graph:
            self.draw_graph_debug()

    def draw_graph_debug(self):
        offset = self.all_sprites.offset

        for node, neighbors in self.graph.items():
            x = node[0] * TILE_SIZE + TILE_SIZE // 2 - offset.x
            y = node[1] * TILE_SIZE + TILE_SIZE // 2 - offset.y
            pygame.draw.circle(self.window, (255, 0, 0), (int(x), int(y)), 5)

            for neighbor in neighbors:
                nx = neighbor[0] * TILE_SIZE + TILE_SIZE // 2 - offset.x
                ny = neighbor[1] * TILE_SIZE + TILE_SIZE // 2 - offset.y
                pygame.draw.line(self.window, (0, 255, 0), (int(x), int(y)), (int(nx), int(ny)), 1)

    def update(self):
        self.all_sprites.update()
        self.game_over()

        if self.interaction_timer > 0:
            self.interaction_timer -= 1
        elif self.message_timer > 0:
            self.message_timer -= 1