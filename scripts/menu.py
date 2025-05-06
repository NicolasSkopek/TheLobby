import sys
import pygame

from scripts.button import Button
from scripts.scene import Scene
from scripts.obj import Obj
from scripts.settings import *


class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu/bg.png", [0,0], self.all_sprites)

        self.active = False # APAGAR DEPOIS - APENAS PARA PULAR O MENU PARA TESTES

        self.music = pygame.mixer.Sound("assets/sounds/libetsdelay.wav")
        self.music.play(-1)

        self.btn_play = Button(135, 450, "play", self.next_scene)
        self.btn_quit = Button(135, 500, "quit", self.quit_game)


    def next_scene(self):
        self.music.stop()
        self.active = False

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)

        return super().events(event)

    def update(self):
        self.btn_play.draw()
        self.btn_quit.draw()

