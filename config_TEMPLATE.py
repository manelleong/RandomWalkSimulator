# Simulation
NUM_TRIALS = {NUM_TRIALS}
SIMULATION_DELAY = {SIMULATION_DELAY} # ms waited between each update, automatically ignored if USE_VISUALIZATION is False
PARALLEL_SIMULATION_COUNT = {PARALLEL_SIMULATION_COUNT} # ideally the number of cores your cpu has for optimal performance

# Food
NUM_FOOD_ITEMS = {NUM_FOOD_ITEMS} # any food that doesn't fit into the clumps will be spread uniformly
NUM_CLUMPS = {NUM_CLUMPS} # 0 for uniform placement
CLUMP_SPREAD = {CLUMP_SPREAD} # how far from the clump center a food can spawn

# Walkers
WALKER_VISION = {WALKER_VISION}
INCLUDE_LEVY = {INCLUDE_LEVY}
INCLUDE_BROWNIAN = {INCLUDE_BROWNIAN}
WALKER_STEP_SIZE = {WALKER_STEP_SIZE} # would not recommend ever changing this

# Visualization
USE_VISUALIZATION = {USE_VISUALIZATION} # if PARALLEL_SIMULATION_COUNT > 1 will not render