import pygame
from collections import deque
import random
from scripts.settings import TILE_SIZE

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size, colision_group, graph, *groups):
        super().__init__(*groups)
        self.graph = graph

        self.original_image = pygame.image.load("assets/player/sprite/idle/idle0.png")
        self.image = pygame.transform.scale(self.original_image, size)
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 3

        self.colision_group = colision_group
        self.size = size
        self.flip = False

        self.frame = 0
        self.tick = 0

        self.path = []
        self.path_index = 0
        self.target_pos = None
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
            direction = direction.normalize()
            self.direction = direction
            move = direction * self.speed
            self.rect.centerx += int(move.x)
            self.rect.centery += int(move.y)

            if pygame.math.Vector2(self.rect.center).distance_to(self.target_pos) < 2:
                self.path_index += 1
                if self.path_index < len(self.path):
                    self.target_pos = self.node_to_pos(self.path[self.path_index])
                else:
                    self.target_pos = None

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

    def update(self):
        self.move_along_path()
