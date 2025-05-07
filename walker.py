import random
from constants import GRID_WIDTH, GRID_HEIGHT
from config import WALKER_VISION, WALKER_STEP_SIZE

class Walker:
    def __init__(self, name, movement_fn, color):
        self.name = name
        self.movement_fn = movement_fn
        self.color = color
        self.pos = (random.uniform(0, GRID_WIDTH), random.uniform(0, GRID_HEIGHT))
        self.steps_taken = 0
        self.food_eaten = 0

    def update(self, food_map):
        # check surroundings first
        target = self._find_nearest_visible_food(food_map)
        if target:
            self._move_toward(target)
        else: # no food in view
            new_pos = self.movement_fn(self.pos)
            self.pos = (new_pos[0] % GRID_WIDTH, new_pos[1] % GRID_HEIGHT)

        # try to eat
        x, y = int(self.pos[0]) % GRID_WIDTH, int(self.pos[1]) % GRID_HEIGHT
        if food_map.try_to_eat(x, y):
            self.food_eaten += 1

        self.steps_taken += 1

    def _find_nearest_visible_food(self, food_map):
        cx, cy = int(self.pos[0]), int(self.pos[1])
        best = None
        best_dist_sq = float('inf')

        for dy in range(-WALKER_VISION, WALKER_VISION + 1):
            for dx in range(-WALKER_VISION, WALKER_VISION + 1):
                x = (cx + dx) % GRID_WIDTH
                y = (cy + dy) % GRID_HEIGHT
                if food_map.has_food(x, y):
                    dist_sq = dx**2 + dy**2
                    if dist_sq < best_dist_sq:
                        best = (x, y)
                        best_dist_sq = dist_sq

        return best
    
    def _move_toward(self, target):
        from math import atan2, cos, sin

        tx, ty = target
        dx = (tx + 0.5) - self.pos[0]
        dy = (ty + 0.5) - self.pos[1]

        angle = atan2(dy, dx)
        step_dx = cos(angle) * WALKER_STEP_SIZE
        step_dy = sin(angle) * WALKER_STEP_SIZE

        self.pos = (
            (self.pos[0] + step_dx) % GRID_WIDTH,
            (self.pos[1] + step_dy) % GRID_HEIGHT,
        )