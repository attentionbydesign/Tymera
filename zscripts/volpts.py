from chimera import openModels as om, runCommand as rc
from VolumeViewer import volume
import numpy as np

###TRANSLATIONAL COMPONENTS###
#get lab/global origin
def getlabog(vol):
    ogtpl = vol.data.origin
    og = t2p(ogtpl)
    xf = vol.model_transform()
    labog = xf.apply(og)
    return labog

#get translation vector
def gettlv(v1,v2):
    v1o = getlabog(v1)
    v2o = getlabog(v2)
    tlv = v2o - v1o
    return tlv

#align global origins of two volumes via translation only
def align_position(v1,v2):
    tlv = gettlv(v1,v2)
    mag = tlv.length
    uv = tlv / mag
    x,y,z = uv
    rc('move {},{},{} {} models #{}'.format(x,y,z,-mag,v2.id))

###ROTATIONAL COMPONENTS###
#get Xform angle from rotation matrix for a volume
def gtheta(vol):
    xf = vol.model_transform()
    rot = xf.getRotation()
    thetaDEG = rot[1]
    return thetaDEG

#get Xform axis from rotation matrix for a volume
def gaxis(vol):
    xf = vol.model_transform()
    rot = xf.getRotation()
    axob = rot[0]
    return axob

def align_orientation(v1,v2):
    tv1 = gtheta(v1)
    tv2 = gtheta(v2)
    #theta = tv2 - tv1

    xv1 = gaxis(v1)
    i1,j1,k1 = xv1
    
    xv2 = gaxis(v2)
    i2,j2,k2 = xv2
    #axis = xv2 - xv1

    rc('turn {},{},{} {} models #{} center models'.format(i1,j1,k1,-tv1,v1.id))
    rc('turn {},{},{} {} models #{} center models'.format(i2,j2,k2,-tv2,v2.id))
    rc('turn x -90 models #{},{}'.format(v1.id,v2.id))

#align a ccp4 file to its corresponding mrc - will need more work on file-type verification, etc.
def ccp4lign(ccp4_id,mrc_id):
    mdls = om.list()
    for mdl in mdls:
        if mdl.id == ccp4_id:
            a = mdl
        elif mdl.id == mrc_id:
            s = mdl
    align_orientation(a,s)
    align_position(a,s)



