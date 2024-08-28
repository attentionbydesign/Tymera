from chimera import openModels as om
he=om.list()[9]

def gcrd(mdl):
    return mdl.atoms[0].xformCoord()
    
def xl2p(mdl,coord):
    from chimera import Xform, Point
    pi = gcrd(mdl)
##    pf = None
##    if coord == tuple and len(coord) == 3:
##    x,y,z = coord
##    pf = Point(x,y,z)
##    elif str(type(coord)) == "<type '_chimera.Point'>":
    pf = coord
    tlv = pf - pi
    tl = Xform.translation(tlv)
    mdl.openState.globalXform(Xform.translation(tlv))

def vgori(vol):
    import chimera, VolumeViewer as vv, ModelPanel as mp, Molecule
    from VolumeViewer import volume as v
    from chimera import Point, Vector, Xform

##    vols=om.list(modelTypes=[v.Volume])
##    for vol in vols:
##        if vol.id == mid:
    vd = vol.data
    
    lot = vd.origin
    x,y,z = lot
    lop = Point(x,y,z)
    
    vxf = vol.model_transform()
    vxfi = vxf.inverse()
    
    gop = vxf.apply(lop)

    return gop

def mark_vori():
    volsel = chimera.selection.currentGraphs()[0]
    xl2p(he, vgori(volsel))
    from chimera import runCommand as rc
    rc('molmap #{} 20'.format(he.id))

def main():
    mark_vori()
    
if __name__ == '__main__':
    main()