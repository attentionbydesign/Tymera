from chimera import Xform, openModels as om, Molecule, UserError, numpyArrayFromAtoms, Point, Vector
import numpy as np
from VolumeViewer import volume

#####_DEFINE FUNCTIONS_#####----------------

#rotation matrix
def get_rmx(vol,invert=False):
    from chimera import Xform
    xf = vol.model_transform()
    if invert == True:
        xf.invert()
        
    rot = xf.getRotation() #get rotation object
    uv,a = rot  #unpack chimera Vector (unit vector/axis) and float (angle)
    rmx = Xform.rotation(uv,a)  #convert to chimera Xform (transformation matrix)
    return rmx

#origin correction vector for translation matrix
def oricrv(vol):
    from chimera import Point
    vbx = vol.bbox()[1]
    vc = vbx.center()
    return(Point() - vc)

#translation matrix
def get_tmx(vol,invert=False):
    from chimera import Xform
    xf = vol.model_transform()
    if invert == True:
        xf.invert()
        
    xlv = xf.getTranslation() + oricrv(vol) #translation vector + origin correction 
    tmx = Xform.translation(xlv) #convert to chimera Xform (transformation matrix)

    return tmx


def run_ov():
    #####_RUN SCRIPT_#####-------------------
    #vols = chimera.selection.currentGraphs()
    #vol = vols[0]
    vols = om.list(modelTypes=[volume.Volume])

    for vol in vols:
        vbx = vol.bbox()[1]
        vc = vbx.center()

        tmxi = get_tmx(vol,True)
        rmxi = get_rmx(vol,True)
        
        vos = vol.openState
        vos.globalXform(rmxi)
        vos.globalXform(tmxi)

        vos.globalXform(Xform.rotation(Vector(1,0,0),90))


    
    





