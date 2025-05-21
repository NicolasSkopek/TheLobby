import sys

import pygame

from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene

class GameOver(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu/gameover.png", [0, 0], self.all_sprites)

        self.music = pygame.mixer.Sound("assets/sounds/gameover_ost.mp3")
        self.music.play(-1)

        self.btn_return = Button(630, 450, "return to menu", self.next_scene)
        self.btn_quit = Button(630, 500, "quit", self.quit_game)

    def next_scene(self):
        self.music.stop()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.btn_return.events(event)
        self.btn_quit.events(event)

        return super().events(event)

    def update(self):
        self.btn_return.draw()
        self.btn_quit.draw()