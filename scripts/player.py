import pygame.sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, *groups):
        super().__init__(*groups)

        self.original_image = pygame.image.load("assets/player/sprite/idle/idle0.png")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3
        self.gravity = 0.8
        self.jump_force = 18
        self.on_ground = False
        self.colision_group = colision_group
        self.flip = False

        self.frame = 0
        self.tick = 0
        self.current_animation = "idle"
        self.size = size

    def input(self):
        key = pygame.key.get_pressed()

        horizontal_movement = key[pygame.K_a] or key[pygame.K_d]
        vertical_movement = key[pygame.K_w]
        vertical_movement_down = key[pygame.K_s]

        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if key[pygame.K_a]:
            self.direction.x = -1
            self.flip = True
        elif key[pygame.K_d]:
            self.direction.x = 1
            self.flip = False
        else:
            self.direction.x = 0

        if horizontal_movement:
            self.set_animation("running_x", "assets/player/sprite/running_x/running_x", 6, 5)
        elif vertical_movement:
            self.set_animation("running_up", "assets/player/sprite/running_up/running_up", 6, 5)
        elif vertical_movement_down:
            self.set_animation("running_down", "assets/player/sprite/running_down/running_down", 7, 7)
        else:
            self.set_animation("idle", "assets/player/sprite/idle/idle", 2, 50)

    def move(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def set_animation(self, anim_name, path, frames, speed):
        if self.current_animation != anim_name:
            self.current_animation = anim_name
            self.frame = 0
            self.tick = 0
        self.animation(speed, frames, path, "png")

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
