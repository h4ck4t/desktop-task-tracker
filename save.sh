#!/bin/bash

# A script for simplifying git operations.

git pull
git add .
git commit -m "Save on $(date '+%Y-%m-%d %H:%M:%S'). $1"
git push
