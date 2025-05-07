# Lévy Walk Foraging Simulation

This project simulates animals using Lévy and Brownian motion to forage for food on a 2D plane.

## Installation

Clone or download the project files.  

python -m venv venv  

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate  # on Windows  

source venv/bin/activate  # on Mac/Linux  

pip install -r requirements.txt  

## Usage

If you want to mess with colors or grid size (not recommended) you can do so in constants.py

config.py is where you'll be adjusting most of your arguments, here are the important ones:

NUM_TRIALS - the total number of times the simulation will run
SIMULATION_DELAY - ms delay between each update (only applies if rendering is on)
PARALLEL_SIMULATION_COUNT - this is for how many simulations can run at once (ideally no larger than your number of cores, and 1 if you want to see the visualization)
NUM_FOOD_ITEMS - total count of food on the map
NUM_CLUMPS - if 0, does a uniform distribution, if > 0 will divide food into that many clumps
CLUMP_SPREAD - the max distance from each clump center that a food can spawn
WALKER_VISION - how far the walkers can see food (when they see food they walk toward it)
INCLUDE_LEVY - introduces a levy walking animal to the simulation
INCLUDE_BROWNIAN - introduces a brownian walking animal to the simulation
USE_VISUALIZATION - this turns on the visualization for the sim, but remember it will not render unless PARALLEL_SIMULATION_COUNT = 1

To run the simulation based on the settings in config.py:
python main.py

The best way to cancel a simulation mid-run is to just kill the terminal.

## Notes
generate_configs.py is just for me and my testing, it creates a bunch of example config files for my various trials under the configs folder.
Feel free to copy any of them (the ones under visual_single_trial are for watching) into config.py and then run main.
config_TEMPLATE.py should be ignored as well, only use config.py
run_all_trials.py can be ignored and even removed from the project and main will run just fine.  It is used for running my 24 trials all at once.  You can run it if you are curious how long it takes to run everything (it's optimized for cpu, so a lower PARALLEL_SIMULATION_COUNT might make it faster or slower for you)