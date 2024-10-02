import chimera
from tymera.commonfunctions import current_selection

cursel=current_selection()

for m in cursel:
    filepath = m.openedAs[0]

#need function to write the current selection as individual files in a specified directory relative to each other or something
# 
# then you can integrate this with phenix potentially...
# 
# Ultimate goal is to select the models you want to use in any of the phenix jobs, then run the command to set up phenix with those inputs
# 
# Automatically generate sequence FASTA file based on selected chain if desired
# 
# Automatically resample if needed
# 
# Automatically look for CCP4 preferentially over MRC if volume not selected?
# 
# Automatically name output     