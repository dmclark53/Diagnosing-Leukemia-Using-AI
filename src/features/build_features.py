# build_features.py
import os
import sys
sys.path.append('..')
from time import time

import cv2 as cv
import numpy as np

# from src import constants as con
from importlib.machinery import SourceFileLoader

ROOT = '/content/drive'
PROJECT = 'My Drive/DataScience/Projects/GitHub/Diagnosing-Leukemia-Using-AI'
PROJECT_PATH = os.path.join(ROOT, PROJECT)

con = SourceFileLoader('constants', os.path.join(PROJECT_PATH, 'src', 'constants.py')).load_module()

def flatten_images(image_file_list):
    flattened_images = []
    start = time()
    for i, image_file in enumerate(image_file_list):
        print(f'{i}: Reading in image {image_file}...')
        image = cv.imread(os.path.join(con.RAW_IMAGES_DIR, image_file))
        print(f'{i}: Read in image.')
        print(f'{i}: Flattening image {image_file}...')
        flattened_images.append(image.flatten())
        print(f'{i}: Flattened image.')
    end = time()
    elapsed = end - start
    time_unit = 'seconds'
    if elapsed > 60:
        elapsed = elapsed / 60
        time_unit = 'minutes'
    print(f'It took {elapsed:0.3f} {time_unit} to load and flatten {len(image_file_list)} images.')
    flattened_images_array = np.array(flattened_images)
    memory_size = flattened_images_array.size * flattened_images_array.itemsize
    memory_unit = 'bytes'
    if memory_size >= 1e9:
        memory_size = memory_size / 1e9
        memory_unit = 'Gb'
    elif memory_size >= 1e6:
        memory_size = memory_size / 1e6
        memory_unit = 'Mb'
    elif memory_size >= 1e3:
        memory_size = memory_size / 1e3
        memory_unit = 'Kb'
    else:
        pass
    print(f'The array of flattened images takes up {memory_size:0.3f} {memory_unit} of memory.')
    return flattened_images_array
