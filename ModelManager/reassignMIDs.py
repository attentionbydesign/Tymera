import chimera,time
from chimera import openModels as om

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

if __name__ == '__main__':
    main()








