import chimera,time
from chimera import openModels as om
from tymera.OrientMdls.lineup_view import save_positions,revert_positions

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
        if hasattr(mdl,'openedAs'):
            mdlpath = mdl.openedAs[0]
            openorder.append(mdlpath)
    return openorder

def main():
    snapshot = save_positions()
    opls = getSortedPaths()
    
    om.close(om.list())

    counter = 0
    timeout = 120
    while counter < timeout:
        if len(om.list()) == 0:
            break
        counter += 1
        time.sleep(1)
        
    for mpth in opls:
        om.open(mpth)
    
    revert_positions(snapshot)

if __name__ == '__main__':
    main()








