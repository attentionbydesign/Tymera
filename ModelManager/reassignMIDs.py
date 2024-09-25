import chimera
from chimera import openModels as om, Molecule, runCommand
from tymera.commonfunctions import getKoD

def sortOMbyname():
    allmdls = om.list()
    mdlnames = [m.name for m in allmdls]
    mdlnames.sort()

    sortedmdls = []
    for name in mdlnames:
        for m in allmdls:
            if m.name == name:
                sortedmdls.append(m)

    return sortedmdls




