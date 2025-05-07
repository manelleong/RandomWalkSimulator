import math
import random
from config import WALKER_STEP_SIZE

def brownian_step(pos):
    import math, random
    angle = random.uniform(0, 2 * math.pi)
    dx = math.cos(angle) * WALKER_STEP_SIZE
    dy = math.sin(angle) * WALKER_STEP_SIZE
    return (pos[0] + dx, pos[1] + dy)

_levy_states = {}

def levy_step(pos):
    pos_id = id(pos)
    if pos_id not in _levy_states:
        _levy_states[pos_id] = {
            "angle": random.uniform(0, 2 * math.pi),
            "steps_left": 0
        }

    state = _levy_states[pos_id]

    if state["steps_left"] <= 0:
        state["angle"] = random.uniform(0, 2 * math.pi)
        alpha = 1.5
        state["steps_left"] = max(1, int(random.paretovariate(alpha)))

    dx = math.cos(state["angle"]) * WALKER_STEP_SIZE
    dy = math.sin(state["angle"]) * WALKER_STEP_SIZE
    state["steps_left"] -= 1

    return (pos[0] + dx, pos[1] + dy)