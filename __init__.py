# this makes the whole tymera_1.0/ directory 
# recognizable as a plugin if you set the path 
# to the folder ONE LEVEL ABOVE it as that for 
# third-party plugins in the Chimera GUI


# i.e., the path to the folder you put all your 
# third-party plugins (e.g., iMODFIT) will be
# part of sys.path from startup instead of needing
# to append it for every session


# NOTE: any lines of code in here are only run if you use the
# Python 2.7.14 Shell (IDLE) and use import tymera.  If you want
# to run code upon activating tymera as a plugin (e.g., clicking on 
# Tools > Custom Plugins > Tymera), put it in the tymera_init.py 
# module which is run by ChimeraExtension.py; i.e., simply starting
# the Tymera plugin does not import everything into the IDLE session
# by default; the IDLE is technically a separate layer on top of chimera
# itself that lets you interact with chimera

import ColorBySeq, os 

tymera_path = os.path.dirname(__file__)

# for example, if this __init__.py file contains
# 'import ColorBySeq', then after opening the IDLE
# and importing tymera, it will autofill 'ColorBySeq' 
# when you type 'tymera.' in the terminal and press tab.
# The same goes for defined variables, such as tymera_path:
# the tymera. autofill menu will include tymera.tymera_path
# which you can show using print(tymera.tymera_path)

#print("os.chdir(os.path.dirname(tymera.__file__))")
from tymera.commonfunctions import cwd2tymera
cwd2tymera()

