import pygame

from scripts.settings import PRIMARY_COLOR, SECONDARY_COLOR
from scripts.text import Text


class Button:
    def __init__(self, x, y, text, call_back):
        self.window = pygame.display.get_surface()
        self.text = text
        self.call_back = call_back

        self.hover_sound = pygame.mixer.Sound("assets/sounds/hoversound.mp3")
        self.hovered = False

        self.text_color = PRIMARY_COLOR
        self.render = Text("assets/font/simsunb.ttf", 40, self.text, self.text_color, (x, y))

    def draw(self):
        self.render.draw_center()

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.render.text_rect.collidepoint(event.pos):
                if not self.hovered:
                    self.hover_sound.play()
                    self.hovered = True
                self.render.update_text(self.text, SECONDARY_COLOR)
            else:
                self.hovered = False
                self.render.update_text(self.text, PRIMARY_COLOR)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.render.text_rect.collidepoint(event.pos):
                self.call_back()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.render.text_rect.collidepoint(event.pos):
                self.call_back()
