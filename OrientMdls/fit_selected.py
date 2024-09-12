import chimera, VolumeViewer
from tymera.commonfunctions import current_selection
from chimera import runCommand as rc

def getmdlsel(sel,ctype):
    if ctype == 'mol':
        ct = chimera.Molecule
    if ctype == 'vol':
        ct = VolumeViewer.volume.Volume
    mdlsel = [m for m in sel if type(m) == ct]
    return mdlsel

def typecount(sel,ctype):
    mdlsel = getmdlsel(sel,ctype)
    return len(mdlsel)
    
def getobj(sel,ctype):
    mdlsel = getmdlsel(sel,ctype)
    return mdlsel[0]

def fitmap(tofit,fitinto):
    rc("fitmap #{} #{}".format(tofit.id,fitinto.id))

def fitseld():
    cursel = current_selection()
    nmol = typecount(cursel,'mol')
    nvol = typecount(cursel,'vol')
    if len(cursel) == nmol + nvol == 2:
        tofit = getobj(cursel,'mol')
        fitinto = getobj(cursel,'vol')
        print("Fitting {} into {}...".format(tofit,fitinto))
        fitmap(tofit,fitinto)
    elif len(cursel) == nvol == 2:
        for v in cursel:
            print v.id, v.name
        tofit = input("Shift this volume (id): ")
        fitinto = input("Fit into this volume (id): ")
        print("Fitting {} into {}...".format(tofit,fitinto))
        fitmap(tofit,fitinto) 
    else:
        print("Please select exactly one Volume and one Molecule, or exactly two Volumes.")

if __name__ == '__main__':
    fitseld()
