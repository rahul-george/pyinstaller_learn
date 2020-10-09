# returns the directory where the hidden imports are defined. 
import os

def get_hook_dirs():
    return [os.path.dirname(__file__)]