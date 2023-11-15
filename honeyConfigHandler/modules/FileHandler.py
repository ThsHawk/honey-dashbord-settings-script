# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import sys

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def openFile(mode, path):
    try:
        file = open(path, mode)
    except FileNotFoundError:
        print("Err: File \'" + path + "\' not found.")
        exit()
    return file