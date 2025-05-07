import os

with open("config_TEMPLATE.py") as f:
    template = f.read()

distributions = ['uniform', 'clumped']
visions = [0, 3]
food_counts = [30, 100]
walker_modes = ['levy', 'brownian', 'both']

clumps_map = {'uniform': 0, 'clumped': 12}
walker_flags = {
    'levy': (True, False),
    'brownian': (False, True),
    'both': (True, True)
}

os.makedirs("configs/nonvisual", exist_ok=True)
os.makedirs("configs/visual_single_trial", exist_ok=True)

def make_config(text, replacements):
    for key, val in replacements.items():
        text = text.replace("{" + key + "}", str(val))
    return text

for dist in distributions:
    for vision in visions:
        for food_count in food_counts:
            for mode in walker_modes:
                name = f"{dist}_vision{vision}_food{food_count}_{mode}"
                levy, brownian = walker_flags[mode]

                base_replacements = {
                    "NUM_FOOD_ITEMS": food_count,
                    "NUM_CLUMPS": clumps_map[dist],
                    "CLUMP_SPREAD": 2,
                    "WALKER_VISION": vision,
                    "INCLUDE_LEVY": levy,
                    "INCLUDE_BROWNIAN": brownian,
                    "WALKER_STEP_SIZE": 1,
                    "SIMULATION_DELAY": 30,
                }

                # nonvisual trials
                nonvisual = make_config(template, {
                    **base_replacements,
                    "NUM_TRIALS": 500,
                    "PARALLEL_SIMULATION_COUNT": 8,
                    "USE_VISUALIZATION": False,
                })
                with open(f"configs/nonvisual/config_{name}.py", "w") as f:
                    f.write(nonvisual)

                # visual demos
                visual = make_config(template, {
                    **base_replacements,
                    "NUM_TRIALS": 1,
                    "PARALLEL_SIMULATION_COUNT": 1,
                    "USE_VISUALIZATION": True,
                })
                with open(f"configs/visual_single_trial/config_{name}.py", "w") as f:
                    f.write(visual)
