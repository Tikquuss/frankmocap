#!/bin/bash

# Usage : 
# chmod +x ./setup.sh
# ./setup.sh

set -e

# a || b ==> try { a } except { b }, thanks https://stackoverflow.com/questions/6961389/exception-handling-in-shell-scripting

echo "===== The basic installation ====="
sudo apt-get install ffmpeg || echo "WARNING"
pip install -r docs/requirements.txt || echo "WARNING"

echo "===== Install Detectron2 (for hand module) ====="
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.6/index.html || echo "WARNING"

echo "===== Install pytorch3d (optional, for pytorch3d renderering) ====="
pip install pytorch3d || echo "WARNING"
 
echo "===== Install other third-party libraries + download pretrained models and sample data ====="
sh scripts/install_frankmocap.sh