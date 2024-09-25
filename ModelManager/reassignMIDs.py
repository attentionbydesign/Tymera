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

def getSortedPaths(byname=True):
    sortedmdls = sortOMbyname()
    openorder = []
    for mdl in sortedmdls:
        mdlpath = mdl.openedAs[0]
        openorder.append(mdlpath)
    return openorder

def main():
    opls = getSortedPaths()
    om.closeAllModels()
    for mpth in opls:
        om.open(mpth)

if __name__ == '__main__':
    main()








