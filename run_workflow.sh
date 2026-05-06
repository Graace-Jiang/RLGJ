#!/bin/bash

python scripts/merge_data.py
python scripts/clean_data.py
python scripts/analysis_modified.py
python scripts/analysis_visualization_test.py