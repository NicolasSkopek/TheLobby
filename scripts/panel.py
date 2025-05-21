import pygame.sprite

class Panel(pygame.sprite.Sprite):
    def __init__(self, pos, size, type, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load(r"assets/panel/panel0.PNG")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.type = type
        self.fixed = False
        self.frame = 0
        self.tick = 0
        self.size = size

    def events(self):
        pass

    def change_image(self):
        if not self.fixed:
            self.fixed = True
            self.original_image = pygame.image.load("assets/panel/panel5.PNG")
            self.image = pygame.transform.scale(self.original_image, self.size)


    def animation(self, speed, frames):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.original_image = pygame.image.load(f"assets/panel/panel{self.frame}.png")
            self.image = pygame.transform.scale(self.original_image, self.size)

    def update(self):
        if not self.fixed:
            self.animation(5, 5)