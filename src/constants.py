# constants.py

import os

# Project directory
ROOT = '/content/drive'
PROJECT = 'My Drive/DataScience/Projects/GitHub/Diagnosing-Leukemia-Using-AI'
PROJECT_DIR = os.path.join(ROOT, PROJECT)

# Data directories
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
RAW_IMAGES_DIR = os.path.join(RAW_DATA_DIR, 'AML-Cytomorphology')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Reference directory
REFERENCES_DIR = os.path.join(PROJECT_DIR, 'references')
IMAGE_STATS = 'image_stats.csv'
