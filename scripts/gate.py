import pygame.sprite

class Gate(pygame.sprite.Sprite):
    def __init__(self, pos, size, tag, *groups):
        super().__init__(*groups)
        self.frames = [
            pygame.image.load(f"assets/gate/gate{i}.PNG") for i in range(7)
        ]
        self.frame = 0
        self.image = self.frames[self.frame]
        self.rect = self.image.get_rect(topleft=pos)
        self.original_image = self.image.copy()
        self.tag = tag

    def change_image(self, fixed_panels):
        max_frame = len(self.frames) - 1
        self.frame = min(fixed_panels, max_frame)
        self.image = self.frames[self.frame]
        self.original_image = self.image.copy()


    def update(self):
        pass