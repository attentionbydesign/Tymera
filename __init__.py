# this makes the whole tymera_1.0/ directory 
# recognizable as a plugin if you set the path 
# to the folder ONE LEVEL ABOVE it as that for 
# third-party plugins in the Chimera GUI


# i.e., the path to the folder you put all your 
# third-party plugins (e.g., iMODFIT) will be
# part of sys.path from startup instead of needing
# to append it for every session

import ColorBySeq, os

tymera_path = os.path.dirname(__file__)

def r2d(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 2:
                key = columns[0]
                value = columns[1]
                result_dict[key] = value
    return result_dict
    file.close()


