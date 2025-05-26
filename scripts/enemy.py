import pygame
from collections import deque
import random
from scripts.settings import TILE_SIZE


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, graph, player, *groups):
        super().__init__(*groups)
        self.graph = graph
        self.size = size

        self.anim_down = [pygame.transform.scale(pygame.image.load(f"assets/enemy/down/f{i}.png"), size) for i in range(4)]
        self.anim_up = [pygame.transform.scale(pygame.image.load(f"assets/enemy/up/c{i}.png"), size) for i in range(4)]
        self.anim_side = [pygame.transform.scale(pygame.image.load(f"assets/enemy/x/e{i}.png"), size) for i in range(4)]

        self.anim_current = self.anim_down
        self.image = self.anim_current[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.flip_image = False

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3.8

        self.colision_group = colision_group

        self.frame = 0
        self.tick = 0

        self.path = []
        self.path_index = 0
        self.target_pos = None
        self.player = player
        self.recalculate_path()

    def recalculate_path(self):
        start = self.get_current_node()
        if start not in self.graph or not self.graph[start]:
            self.path = []
            self.target_pos = None
            return

        valid_goals = [node for node in self.graph if node != start]
        if not valid_goals:
            self.path = []
            self.target_pos = None
            return

        goal = random.choice(valid_goals)
        path = Enemy.bfs(self.graph, start, goal)

        if path and len(path) > 1:
            self.path = path
            self.path_index = 1
            self.target_pos = self.node_to_pos(self.path[self.path_index])
        else:
            self.path = []
            self.target_pos = None

    def get_current_node(self):
        col = self.rect.centerx // TILE_SIZE
        row = self.rect.centery // TILE_SIZE
        return (col, row)

    def node_to_pos(self, node):
        col, row = node
        x = col * TILE_SIZE + TILE_SIZE // 2
        y = row * TILE_SIZE + TILE_SIZE // 2
        return pygame.math.Vector2(x, y)

    def move_along_path(self):
        if not self.path or self.path_index >= len(self.path):
            self.recalculate_path()
            return

        if self.target_pos is None:
            self.target_pos = self.node_to_pos(self.path[self.path_index])
            self.recalculate_path()
            return

        direction = self.target_pos - pygame.math.Vector2(self.rect.center)
        if direction.length() > 0:
            self.direction = direction.normalize()
            self.update_animation_direction()

            move = self.direction * self.speed
            new_position = self.rect.center + pygame.math.Vector2(move.x, move.y)

            if self.is_walkable(new_position):
                self.rect.centerx += int(move.x)
                self.rect.centery += int(move.y)

            if pygame.math.Vector2(self.rect.center).distance_to(self.target_pos) < 2:
                self.path_index += 1
                if self.path_index < len(self.path):
                    self.target_pos = self.node_to_pos(self.path[self.path_index])
                else:
                    self.target_pos = None

    def move_towards_player(self):
        player_position = self.player.rect.center
        enemy_position = self.rect.center

        direction = pygame.math.Vector2(player_position[0] - enemy_position[0], player_position[1] - enemy_position[1])

        if direction.length() > 0:
            self.direction = direction.normalize()
            self.update_animation_direction()

        move = self.direction * self.speed
        new_position = self.rect.center + pygame.math.Vector2(move.x, move.y)

        if self.is_walkable(new_position):
            self.rect.centerx += int(move.x)
            self.rect.centery += int(move.y)
        else:
            alt_x = pygame.math.Vector2(move.x, 0)
            if self.is_walkable(self.rect.center + alt_x):
                self.rect.centerx += int(alt_x.x)
            else:
                alt_y = pygame.math.Vector2(0, move.y)
                if self.is_walkable(self.rect.center + alt_y):
                    self.rect.centery += int(alt_y.y)

    def is_walkable(self, position):
        col = int(position[0] // TILE_SIZE)
        row = int(position[1] // TILE_SIZE)
        return (col, row) in self.graph

    def update_animation_direction(self):
        dx, dy = self.direction.x, self.direction.y
        if abs(dx) > abs(dy):
            self.anim_current = self.anim_side
            self.flip_image = dx > 0
        elif dy > 0:
            self.anim_current = self.anim_down
            self.flip_image = False
        else:
            self.anim_current = self.anim_up
            self.flip_image = False

    def animate(self):
        self.tick += 1
        if self.tick >= 10:
            self.tick = 0
            self.frame = (self.frame + 1) % len(self.anim_current)
            self.image = self.anim_current[self.frame]
            if self.flip_image:
                self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        player_position = self.player.rect.center
        enemy_position = self.rect.center
        distance_to_player = pygame.math.Vector2(player_position[0] - enemy_position[0],
                                                 player_position[1] - enemy_position[1]).length()

        if distance_to_player < 1:
            self.move_towards_player()
        else:
            self.move_along_path()

        self.animate()

    @staticmethod
    def bfs(graph, start, goal):
        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
        return []
