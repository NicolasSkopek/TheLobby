import pygame.sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load("assets/player/sprite/idle/idle0.png")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4

        self.on_ground = False
        self.colision_group = colision_group
        self.flip = False

        self.frame = 0
        self.tick = 0

        self.running_sound = pygame.mixer.Sound("assets/sounds/running.mp3")
        self.running_sound.set_volume(4)

        self.is_running = False
        self.size = size

    def input(self):
        key = pygame.key.get_pressed()

        moving = False

        if key[pygame.K_w]:
            self.direction.y = -1
            self.flip = False
            self.animation(4, 8, "assets/player/sprite/running_up/running_up", "png")
            moving = True
        elif key[pygame.K_s]:
            self.direction.y = 1
            self.flip = False
            self.animation(4, 8, "assets/player/sprite/running_down/running_down", "png")
            moving = True
        else:
            self.direction.y = 0

        if key[pygame.K_a] and self.direction.y == 0:
            self.direction.x = -1
            self.flip = True
            self.animation(4, 8, "assets/player/sprite/running_x/running_x", "png")
            moving = True
        elif key[pygame.K_d] and self.direction.y == 0:
            self.direction.x = 1
            self.flip = False
            self.animation(4, 8, "assets/player/sprite/running_x/running_x", "png")
            moving = True
        else:
            self.direction.x = 0

        if self.direction.x == 0 and self.direction.y == 0:
            self.animation(15, 2, "assets/player/sprite/idle/idle", "png")

        if moving:
            self.play_running_sound(True)
        else:
            self.play_running_sound(False)


    def play_running_sound(self, is_running):
        if is_running and not self.is_running:
            self.running_sound.play(-1)
            self.is_running = True
        elif not is_running and self.is_running:
            self.running_sound.stop()
            self.is_running = False

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
                    if self.rect.bottom > sprite.rect.top:
                        self.rect.bottom = sprite.rect.top
                if sprite.type in ["nw", "h1", "rg", "ww", "br", "sd", "bc", "bl"]:
                    limit = sprite.rect.top + sprite.rect.height * 0.35
                    if self.rect.top < limit:
                        self.rect.top = limit

                if sprite.type == "l1":
                    if self.rect.right > sprite.rect.left and self.rect.left < sprite.rect.left:
                        self.rect.right = sprite.rect.left

                    elif self.rect.bottom > sprite.rect.top and self.rect.top < sprite.rect.top:
                        self.rect.bottom = sprite.rect.top
                if sprite.type == "l0":
                    if self.rect.left < sprite.rect.right and self.rect.right > sprite.rect.right:
                        self.rect.left = sprite.rect.right

                    elif self.rect.bottom > sprite.rect.top and self.rect.top < sprite.rect.top:
                        self.rect.bottom = sprite.rect.top

                if sprite.type == "p2":
                    if self.rect.colliderect(sprite.rect):
                        if self.rect.right > sprite.rect.left and self.rect.left < sprite.rect.left:
                            self.rect.right = sprite.rect.left
                        elif self.rect.left < sprite.rect.right and self.rect.right > sprite.rect.right:
                            self.rect.left = sprite.rect.right
                        elif self.rect.bottom > sprite.rect.top and self.rect.top < sprite.rect.top:
                            self.rect.bottom = sprite.rect.top
                        elif self.rect.top < sprite.rect.bottom and self.rect.bottom > sprite.rect.bottom:
                            self.rect.top = sprite.rect.bottom

                if sprite.type == "p1":
                    limit = sprite.rect.top + sprite.rect.height * 0.35
                    if self.rect.top < limit:
                        self.rect.top = limit


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
