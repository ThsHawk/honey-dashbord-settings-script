# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

import sys

# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

def openFile(mode):
    argvLen = len(sys.argv)
    if argvLen < 2:
        print("Err: Too few arguments!")
        exit()
    elif argvLen > 3:
        print("Err: Too many arguments!")
        exit()
    else:
        try:
            file = open(sys.argv[1], mode)
        except FileNotFoundError:
            print("Err: File \'" + sys.argv[1] + "\' not found.")
            exit()
        return file