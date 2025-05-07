import multiprocessing
import sys
from tqdm import tqdm
from config import NUM_TRIALS, PARALLEL_SIMULATION_COUNT
from collections import defaultdict

def run_single_simulation(_):
    from simulation import Simulation
    sim = Simulation()
    return sim.run()

class BatchRunner:
    def __init__(self):
        pass
    
    def run(self):
        with multiprocessing.Pool(PARALLEL_SIMULATION_COUNT) as pool:
            results = list(tqdm(pool.imap_unordered(run_single_simulation, range(NUM_TRIALS)), total=NUM_TRIALS, file=sys.stderr))

        self._report(results)

    def _report(self, results):
        agg = defaultdict(lambda: {"efficiency": [], "steps": [], "food": []})

        for sim_result in results:
            for walker in sim_result:
                name = walker["name"]
                steps = walker["steps_taken"]
                food = walker["food_eaten"]
                efficiency = food / steps if steps > 0 else 0

                agg[name]["efficiency"].append(efficiency)
                agg[name]["steps"].append(steps)
                agg[name]["food"].append(food)

        print("=== Batch Results ===")
        for name, data in agg.items():
            n = len(data["efficiency"])
            avg_eff = sum(data["efficiency"]) / n
            avg_steps = sum(data["steps"]) / n
            avg_food = sum(data["food"]) / n

            print(f"{name}:")
            print(f"  Trials Run:     {n}")
            print(f"  Avg Efficiency: {avg_eff:.3f} (food / step)")
            print(f"  Avg Steps:      {avg_steps:.1f}")
            print(f"  Avg Food:       {avg_food:.1f}")
