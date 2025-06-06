import pygame, sys
from pygame import KEYDOWN

from scripts import game
from scripts.endgame import EndGame
from scripts.menu import *
from scripts.settings import *
from scripts.game import *
from scripts.gameover import *

class StartGame:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.window = pygame.display.set_mode([WIDTH, HEIGHT])

        pygame.display.set_caption(TITLE)

        icon = pygame.image.load("assets/icon/icon.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)


        self.scene = "menu"
        self.current_scene = Menu()

        self.fps = pygame.time.Clock()

    def run(self):
        while True:
            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False and self.current_scene.gameover == True:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "game" and self.current_scene.active == False and self.current_scene.gameover == False:
                self.scene = "endgame"
                self.current_scene = EndGame()
            elif self.scene == "endgame" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.current_scene.events(event)

            self.fps.tick(60)
            self.window.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()