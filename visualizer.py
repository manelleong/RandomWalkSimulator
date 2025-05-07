
import os
import sys
import contextlib
from constants import GRID_WIDTH, GRID_HEIGHT, TILE_SIZE, BACKGROUND_COLOR, FOOD_COLOR

@contextlib.contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout

with suppress_stdout():
    import pygame

class Visualizer:
    def __init__(self, food_map, walkers):
        self.screen_width = GRID_WIDTH * TILE_SIZE
        self.screen_height = GRID_HEIGHT * TILE_SIZE
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Lévy vs Brownian Foraging")
        self.food_map = food_map
        self.walkers = walkers

    def render(self):
        # render background
        self.screen.fill(BACKGROUND_COLOR)
        
        # render food
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.food_map.has_food(x, y):
                    rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    pygame.draw.rect(self.screen, FOOD_COLOR, rect)

        # render walkers
        for walker in self.walkers:
            wx, wy = walker.pos
            px = int(wx * TILE_SIZE)
            py = int(wy * TILE_SIZE)
            pygame.draw.circle(self.screen, walker.color, (px, py), TILE_SIZE // 2)

        pygame.display.flip()
        pygame.event.pump()
