#!/bin/bash
# Checks and installs all packages needed for UpdatePlots.py to run

pip3 install selenium
pip3 install beautifulsoup4
pip3 install Plotly
conda install -c plotly plotly-orca
