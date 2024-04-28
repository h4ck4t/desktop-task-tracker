#!/bin/bash

export SCRIPT_PATH='script'
export TASK_PATH='task'

# Set reg for persistent wallpaper path.
python script/set_reg_wallpaper_path.py

# Generate task tracker.
python "${SCRIPT_PATH}/gen.py"