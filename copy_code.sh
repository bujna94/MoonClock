#!/bin/bash

find ./MOONCLOCK -maxdepth 1 ! -name "secrets.py" ! -name "conf.py" -name "*.py" | xargs cp -t "$1"
