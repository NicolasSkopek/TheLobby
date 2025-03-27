import pygame

from scripts.settings import WIDTH, HEIGHT


class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

        self.window = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - WIDTH / 2
        self.offset.y = player.rect.centery - HEIGHT / 2


        for sprite in self.sprites():
            off_rect = sprite.rect.copy()
            off_rect.center -= self.offset
            self.window.blit(sprite.image, off_rect)