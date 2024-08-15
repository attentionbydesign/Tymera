from chimera import openModels as om, runCommand as rc
from VolumeViewer import volume
import numpy as np

sid=8
aid=7

mdls = om.list()
segv = mdls[sid]
asv = mdls[aid]

#get LOCAL/MODEL origins
def getov(vol):
    orls = []
    ori = vol.data.origin
    for i in ori:
        orls.append(i)
    return np.array(orls)

print '#{} origin is at {}'.format(segv.id,getov(segv))
print '#{} origin is at {}'.format(asv.id,getov(asv)) 

def align_origin(v1,v2):
    ov1 = getov(v1)
    ov2 = getov(v2)
    if np.array_equal(v1,v2) == True:
        print 'same origin'
    elif np.array_equal(v1,v2) == False:
        print 'different origin'
        v1.data.set_origin(ov2)

#get translational column vector
#from the overall 3x4 xform matrix
def getxfv(vol):
    xf = vol.model_transform()
    tlv = xf.getTranslation()
    tlarr = []
    for i in tlv:
        tlarr.append(i)
    return tlarr

sxv = getxfv(segv)
axv = getxfv(asv)
#print "translation vectors: ",sxv, axv

#coordinates of origin in lab frame = apply translation to origin
def getogcrd(vol):
    orv = getov(vol)
    txv = getxfv(vol)
    return np.subtract(txv,orv)

socrd = getogcrd(segv)
aocrd = getogcrd(asv)

print '#{} xform origin is at {}'.format(segv.id,socrd)
print '#{} xform origin is at {}'.format(asv.id,aocrd)

print np.subtract(socrd,aocrd)

#asv.data.set_origin(so)

#rc('matrixcopy #8 #7')

##sxf = segv.model_transform()
##sp = sxf.getTranslation()
##axf = asv.model_transform()
##ap = axf.getTranslation()
##
##s = segv.grid_points(sxf)
##a = asv.grid_points(axf)
##
##
##
##sc = np.mean(s,axis=0)
##ac = np.mean(a,axis=0)
##
##sct = tuple(sc)
##sx,sy,sz = sct
##act = tuple(ac)
##ax,ay,az = act
##
##sav = (sx-ax,sy-ay,sz-az)
##
##print 'sct: '+str(sct)
##print 'act: '+str(act)
##print 'sav: '+str(sav)
##
###translation vector between models
##tls = ap - sp
###tuple form of translation vector
##tlst=tuple(tls)
##
##
##print 'origin translation vector: '+str(tlst)
##a,b,c = so
##
###calculate distance between origins of the models
##import math
##print "distance: "+str(math.sqrt(sum(i**2 for i in tls)))


def ogfit():
    from chimera import runCommand as rc
    mid=sid

    axv = {a:x,b:y,c:z}
    for i in axv:
        rc('move {} {} models #{} coordinateSystem #{}'.format(axv[i],-i,mid,mid))
