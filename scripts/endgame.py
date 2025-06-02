import pygame
import sys

from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene

class EndGame(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu/endgame.png", [0, 0], self.all_sprites)

        self.music_channel = pygame.mixer.Channel(2)
        self.music = pygame.mixer.Sound("assets/sounds/endgame.mp3")
        self.music_channel.play(self.music, loops=-1)

        self.music_channel_2 = pygame.mixer.Channel(1)
        self.music_2 = pygame.mixer.Sound("assets/sounds/endgame.mp3")
        self.music_2.set_volume(0)
        self.music_channel_2.set_volume(0)
        self.music_channel_2.play(self.music, loops=-1)

        self.btn_return = Button(1050, 380, "return to menu", self.next_scene)
        self.btn_quit = Button(1050, 430, "quit", self.quit_game)

        self.images = [
            pygame.image.load("assets/menu/image1.png"),
            pygame.image.load("assets/menu/image2.png"),
            pygame.image.load("assets/menu/image3.png"),
            pygame.image.load("assets/menu/image4.png"),
            pygame.image.load("assets/menu/image5.png"),
            pygame.image.load("assets/menu/image7.png"),
            pygame.image.load("assets/menu/image9.png"),
        ]
        self.current_image_index = 0
        self.alpha = 0
        self.fade_in = True

        self.image_display_time = 6000
        self.fade_out_delay = 3000
        self.last_change_time = pygame.time.get_ticks()
        self.fade_out_start_time = None

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

        current_time = pygame.time.get_ticks()
        if current_time - self.last_change_time > self.image_display_time:
            self.last_change_time = current_time
            self.current_image_index = (self.current_image_index + 1) % len(self.images)

            self.alpha = 0
            self.fade_in = True
            self.fade_out_start_time = None

        if self.fade_in:
            self.alpha += 5
            if self.alpha >= 255:
                self.alpha = 255
                self.fade_in = False
                self.fade_out_start_time = current_time
        else:
            if self.fade_out_start_time and current_time - self.fade_out_start_time >= self.fade_out_delay:
                self.alpha -= 2
            if self.alpha <= 0:
                self.alpha = 0
                self.fade_in = True

        image = self.images[self.current_image_index].copy()
        image.set_alpha(self.alpha)

        self.window.blit(image, (125, 200))

        self.btn_return.draw()
        self.btn_quit.draw()

        pygame.display.flip()
