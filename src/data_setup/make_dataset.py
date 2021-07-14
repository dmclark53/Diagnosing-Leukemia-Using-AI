# make_dataset.py
import os
import pickle

from importlib.machinery import SourceFileLoader

ROOT = '/content/drive'
PROJECT = 'My Drive/DataScience/Projects/GitHub/Diagnosing-Leukemia-Using-AI'
PROJECT_PATH = os.path.join(ROOT, PROJECT)

# from src import constants as con
con = SourceFileLoader('constants', os.path.join(PROJECT_PATH, 'src', 'constants.py')).load_module()

def load_train_test():
    """
    Load pickled training and test data from file.
    """

    file_list = ['X_train', 'X_test', 'y_train', 'y_test']
    data_sets = []
    for filename in file_list:
        data_sets.append(pickle.load(open(os.path.join(con.PROCESSED_DATA_DIR, filename), 'rb')))
    return tuple(data_sets)


def load_train():
    """
    Load pickled training and test data from file.
    """

    file_list = ['X_train', 'y_train']
    data_sets = []
    for filename in file_list:
        data_sets.append(pickle.load(open(os.path.join(con.PROCESSED_DATA_DIR, filename), 'rb')))
    return tuple(data_sets)
