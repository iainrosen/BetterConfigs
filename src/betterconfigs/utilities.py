import pickle
import os
import warnings
from __init__ import executableVersion
def ls(path):
    with open(path, 'rb') as handle:
        loadedConfig = pickle.load(handle)
    print("Version: ",loadedConfig['_version'])