import pygame.sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load("assets/player/sprite/idle/idle0.png")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        self.on_ground = False
        self.colision_group = colision_group
        self.flip = False

        self.frame = 0
        self.tick = 0

        self.running_sound = pygame.mixer.Sound("assets/sounds/running.mp3")

        self.size = size

    def input(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
            self.flip = False
            self.play_running_sound()
            self.animation(8, 6, "assets/player/sprite/running_up/running_up", "png")
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.flip = False
            self.play_running_sound()
            self.animation(8, 6, "assets/player/sprite/running_down/running_down", "png")
        else:
            self.direction.y = 0


        if key[pygame.K_a]:
            self.direction.x = -1
            self.flip = True
            self.play_running_sound()
            self.animation(8, 6, "assets/player/sprite/running_x/running_x", "png")
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.flip = False
            self.play_running_sound()
            self.animation(8, 6, "assets/player/sprite/running_x/running_x", "png")
        else:
            self.direction.x = 0

        if self.direction.x == 1 and self.direction.y == -1:
            self.flip = False
            self.animation(60, 6, "assets/player/sprite/running_x/running_x", "png")
        elif self.direction.x == -1 and self.direction.y == -1:
            self.flip = True
            self.animation(60, 6, "assets/player/sprite/running_x/running_x", "png")
        elif self.direction.x == 1 and self.direction.y == 1:
            self.flip = False
            self.animation(60, 6, "assets/player/sprite/running_x/running_x", "png")
        elif self.direction.x == -1 and self.direction.y == 1:
            self.flip = True
            self.animation(60, 6, "assets/player/sprite/running_x/running_x", "png")

        if self.direction.x == 0 and self.direction.y == 0:
            self.animation(8, 2, "assets/player/sprite/idle/idle", "png")

    def play_running_sound(self):
        if not pygame.mixer.get_busy():
            self.running_sound.play(-1)

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def collision(self):
        for sprite in self.colision_group:
            if sprite.rect.colliderect(self.rect):
                if sprite.type == "w0":
                    self.rect.left = sprite.rect.right
                if sprite.type == "w1":
                    self.rect.right = sprite.rect.left
                if sprite.type == "w2":
                    self.rect.bottom = self.rect.top + 52
                if sprite.type == "nw":
                    self.rect.top = sprite.rect.bottom
                if sprite.type == "l1":
                    if self.rect.right - 200 == sprite.rect.left:
                        self.rect.right = self.rect.left
                    elif self.rect.bottom == sprite.rect.top:
                        self.rect.bottom = self.rect.top


    def animation(self, speed, frames, path, file_type):
        self.tick += 1
        if self.tick > speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.original_image = pygame.image.load(f"{path}{self.frame}.{file_type}")
            self.image = pygame.transform.scale(self.original_image, self.size)
            self.image = pygame.transform.flip(self.image, self.flip, False)

    def update(self):
        self.input()
        self.move()
        self.collision()

