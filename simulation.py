import time
from food_map import FoodMap
from walker import Walker
from visualizer import Visualizer
from strategies import brownian_step, levy_step
from config import INCLUDE_LEVY, INCLUDE_BROWNIAN, USE_VISUALIZATION, PARALLEL_SIMULATION_COUNT, SIMULATION_DELAY
from constants import LEVY_COLOR, BROWNIAN_COLOR

class Simulation:
    def __init__(self):
        self.food_map = FoodMap()
        self.walkers = self._create_walkers()
        self.is_finished = False
        self.visualizer = Visualizer(self.food_map, self.walkers) if USE_VISUALIZATION and PARALLEL_SIMULATION_COUNT == 1 else None

    def _create_walkers(self):
        walkers = []
        if INCLUDE_LEVY:
            walkers.append(Walker("levy", levy_step, LEVY_COLOR))
        if INCLUDE_BROWNIAN:
            walkers.append(Walker("brownian", brownian_step, BROWNIAN_COLOR))

        return walkers
    
    def _step(self):
        for walker in self.walkers:
            walker.update(self.food_map)

        if USE_VISUALIZATION and PARALLEL_SIMULATION_COUNT == 1:
            self.visualizer.render()
            time.sleep(SIMULATION_DELAY / 1000)
        
        if self.food_map.is_empty():
            self.is_finished = True

    def run(self):
        while not self.is_finished:
            self._step()

        return [
            {
                "name": walker.name,
                "steps_taken": walker.steps_taken,
                "food_eaten": walker.food_eaten
            }
            for walker in self.walkers
        ]
 