import random
from constants import GRID_WIDTH, GRID_HEIGHT
from config import NUM_FOOD_ITEMS, NUM_CLUMPS, CLUMP_SPREAD

class FoodMap:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.place_food()
        self.food_count = self.count_food()

    def reset(self):
        for r in range(GRID_HEIGHT):
            for c in range(GRID_WIDTH):
                self.grid[r][c] = 0

        self.place_food()
    
    def place_food(self):
        if NUM_CLUMPS <= 0:
            self._place_uniform(NUM_FOOD_ITEMS)
            return
        
        # clumped placement
        placed = 0
        attempts = 0
        max_attempts = NUM_FOOD_ITEMS * 20

        clump_centers = [
            (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            for _ in range(NUM_CLUMPS)
        ]

        attempts = 0
        while placed < NUM_FOOD_ITEMS and attempts < max_attempts:
            cx, cy = random.choice(clump_centers)
            dx = random.randint(-CLUMP_SPREAD, CLUMP_SPREAD)
            dy = random.randint(-CLUMP_SPREAD, CLUMP_SPREAD)
            x = (cx + dx) % GRID_WIDTH
            y = (cy + dy) % GRID_HEIGHT

            if self.grid[y][x] == 0:
                self.grid[y][x] = 1
                placed += 1

            attempts += 1

        # place remaining food uniformly if needed
        if placed < NUM_FOOD_ITEMS:
            self._place_uniform(NUM_FOOD_ITEMS - placed)

    def _place_uniform(self, count):
        placed = 0
        attempts = 0
        max_attempts = count * 20

        while placed < count and attempts < max_attempts:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if self.grid[y][x] == 0:
                self.grid[y][x] = 1
                placed += 1
            attempts += 1
    
    def has_food(self, x, y):
        return self.grid[y][x] == 1

    def try_to_eat(self, x, y):
        if self.grid[y][x] == 1:
            self.grid[y][x] = 0
            self.food_count -= 1
            return True
        return False
    
    def count_food(self):
        total = 0
        for r in range(GRID_HEIGHT):
            for c in range(GRID_WIDTH):
                if self.grid[r][c] == 1:
                    total += 1

        return total

    def is_empty(self):
        return self.food_count <= 0