import pygame.sprite

class Panel(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load("assets\panel\panel0.PNG")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.colision_group = colision_group

        self.frame = 0
        self.tick = 0
        self.size = size

    def events(self):
        pass

    def animation(self, speed, frames):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.original_image = pygame.image.load(f"assets/panel/panel{self.frame}.png")
            self.image = pygame.transform.scale(self.original_image, self.size)

    def update(self):
        self.animation(5, 5)