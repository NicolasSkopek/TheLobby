import pygame

from scripts.settings import *


class Text:
    def __init__(self, font, size, text, color, pos):
        self.window = pygame.display.get_surface()

        self.font = pygame.font.Font(font, size)
        self.text_str = text
        self.color = color

        self.text = self.font.render(self.text_str, True, self.color)
        self.text_rect = self.text.get_rect(center=pos)

    def draw(self):
        self.window.blit(self.text, self.text_rect.topleft)

    def update_text(self, text, color):
        self.text_str = text
        self.color = color
        self.text = self.font.render(self.text_str, True, self.color)
        self.text_rect = self.text.get_rect(center=self.text_rect.center)

    def draw_center(self):
        self.window.blit(self.text, self.text_rect)