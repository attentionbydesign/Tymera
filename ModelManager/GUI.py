from chimera import runCommand as rc
from Tkinter import * 
import tkFileDialog as filedialog 

def openFileDialog():
    filepath = filedialog.askopenfilename(initialdir = "/PROJECTS/",
                    title = "Select a File",
                    filetypes = (("PDB files",
                                    "*.pdb*"),
                                ("MRC files","*.mrc"),
                                ("all files",
                                    "*.*")))

    # Change label contents
    print(filepath)

    rc("open "+filepath)
                                                                                                    





