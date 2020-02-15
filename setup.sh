#!/usr/bin/env bash

#create your python environment

#pip install into environment
pip install -r requirements.txt


# Download model
HEAD_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
python $HEAD_DIR/download_model.py