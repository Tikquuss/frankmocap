#!/bin/bash

# Usage : 
# chmod +x ./setup.sh
# ./setup.sh

set -e

# The basic installation
sudo apt-get install ffmpeg
pip install -r docs/requirements.txt

# Install Detectron2 (for hand module)
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.6/index.html

# Install pytorch3d (optional, for pytorch3d renderering)
pip install pytorch3d

# Install other third-party libraries + download pretrained models and sample data
sh scripts/install_frankmocap.sh