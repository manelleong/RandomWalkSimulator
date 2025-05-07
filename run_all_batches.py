import os
import shutil
import subprocess

CONFIG_DIR = "configs/nonvisual"
TARGET_CONFIG = "config.py"
RESULTS_DIR = "results"

os.makedirs(RESULTS_DIR, exist_ok=True)

configs = sorted(f for f in os.listdir(CONFIG_DIR) if f.startswith("config_") and f.endswith(".py"))

for config_file in configs:
    print(f"Running batch: {config_file}")

    # copy the selected config file over config.py
    shutil.copy(os.path.join(CONFIG_DIR, config_file), TARGET_CONFIG)

    result_file = os.path.join(RESULTS_DIR, config_file.replace(".py", ".txt"))

    # run the batch simulation and capture output
    with open(result_file, "w") as out:
        subprocess.run(["python", "main.py"], stdout=out)

    print(f"Finished: {result_file}")

print("All batches complete.")
