# Simulation
NUM_TRIALS = 500
SIMULATION_DELAY = 30 # ms waited between each update, automatically ignored if USE_VISUALIZATION is False
PARALLEL_SIMULATION_COUNT = 8 # ideally the number of cores your cpu has for optimal performance

# Food
NUM_FOOD_ITEMS = 100 # any food that doesn't fit into the clumps will be spread uniformly
NUM_CLUMPS = 0 # 0 for uniform placement
CLUMP_SPREAD = 2 # how far from the clump center a food can spawn

# Walkers
WALKER_VISION = 0
INCLUDE_LEVY = True
INCLUDE_BROWNIAN = False
WALKER_STEP_SIZE = 1 # would not recommend ever changing this

# Visualization
USE_VISUALIZATION = False # if PARALLEL_SIMULATION_COUNT > 1 will not render