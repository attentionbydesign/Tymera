import chimera
m = chimera.openModels.list()[1]


def calcwidth():
    xlist = []

    for a in m.atoms:
        x = a.xformCoord().x
        xlist.append(x)

    width = max(xlist)-min(xlist)
    return width

angles = {}

for i in range(0,36):
    xfcoords = chimera.numpyArrayFromAtoms(m.atoms,xformed=True)
    mos = m.openState
    mos.globalXform(chimera.Xform.rotation(0,1,0,10))
    w = calcwidth()
    angles[i] = w

def getmaxvalkey(dicte):
    maxval = max(dicte.values())
    for key in dicte:
        if dicte[key] == maxval:
            return key

mvk = getmaxvalkey(angles)
        



for i in range(0,mvk):
    mos = m.openState
    mos.globalXform(chimera.Xform.rotation(0,1,0,10))
    

    

