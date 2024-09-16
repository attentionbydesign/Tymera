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

def get_mdlNo(sel,mid):
    for m in sel:
        if m.id == mid:
            return m

def fitseld():
    cursel = current_selection()
    nmol = typecount(cursel,'mol')
    nvol = typecount(cursel,'vol')

    #Fitting mol --> vol
    if len(cursel) / 2 == nmol == nvol == 1:
        tofit = getobj(cursel,'mol')
        fitinto = getobj(cursel,'vol')
        print("Fitting {} into {}...".format(tofit,fitinto))
        fitmap(tofit,fitinto)

    #Fitting vol --> vol
    elif len(cursel) == nvol == 2:
        for v in cursel:
            print v.id, v.name

        tofitID = input("Shift this volume (id): ")
        tofit = get_mdlNo(cursel, tofitID)

        fitintoID = input("Fit into this volume (id): ")
        fitinto = get_mdlNo(cursel, fitintoID)

        print("Fitting {} into {}...".format(tofit.name,fitinto.name))
        fitmap(tofit,fitinto) 
    else:
        print("Please select exactly one Volume and one Molecule, or exactly two Volumes.")


def loopfit(sel):
    from chimera import runCommand as rc
    refmdl = sel[0]
    for m in sel[1:len(sel)]:
        rc("fitmap #{} #{}".format(m.id, refmdl.id))




if __name__ == '__main__':
    fitseld()
