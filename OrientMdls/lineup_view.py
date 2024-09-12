## script for lining up similar models for comparison

""" 
e.g., 10 classes from 3D sorting

* option to toggle between superimposed/aligned
vs. line-up/spaced out views

* save state / global xforms of all models at any given
time, thereby allowing an easier option to undo movement

* keyboard shortcut to "Tools > Movement > Undo Move / Redo Move" 
"""
import chimera
from tymera.commonfunctions import current_selection
from tymera.OrientMdls import orient_

def save_current_positions():
    pass
#placeholder for now - will edit later, so you can revert back to original view




def 






cursel = current_selection()

for m in cursel:
