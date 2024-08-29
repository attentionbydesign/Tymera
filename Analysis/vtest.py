from chimera import openModels, Molecule, UserError, numpyArrayFromAtoms, Point, Vector
import numpy as np

#####_DEFINE FUNCTIONS_#####----------------
def cofm(vol):

    nparr = vol.matrix()
    
    # Generate coordinates for each dimension
    x,y,z = np.indices(nparr.shape)

    # Calculate the total mass
    total_mass = nparr.sum()

    # Compute the center of mass along each axis
    x_center_of_mass = (x * nparr).sum() / total_mass
    y_center_of_mass = (y * nparr).sum() / total_mass
    z_center_of_mass = (z * nparr).sum() / total_mass

    center_of_mass = Point(x_center_of_mass, y_center_of_mass, z_center_of_mass)

    return center_of_mass

#-----.getRotation() returns a tuple of:
#-------[1] a chimera Vector object (axis of rotation/unit vector) and
#-------[2] a float (angle of rotation)
def get_rmx(vol,invert=False):
    xf = vol.model_transform()
    if invert == True:
        xf.invert()
        
    rot = xf.getRotation() #get rotation object
    uv,a = rot  #unpack chimera Vector (unit vector/axis) and float (angle)
    rmx = Xform.rotation(uv,a)  #convert to chimera Xform (transformation matrix)
    return rmx

#origin correction vector
##This corrects for bounding box centers that are shifted from
##the local origin - e.g., CCP4 files often have the origin located
##at the bottom left corner (LLF), so simply translating them to the
##global origin technically means translating until the LLF aligns with the
##global origin/center of the display; instead, you want to align the local/volume
##center with the global origin/center of display.
def ocrv(vol):
        vbx = vol.bbox()[1]
        vc = vbx.center()
        return(Point() - vc)

#-----.getTranslation() returns a chimera Vector object
def get_tmx(vol,invert=False):
    xf = vol.model_transform()
    if invert == True:
        xf.invert()
        
    xlv = xf.getTranslation() #get translation vector
    crv = ocrv(vol)     #origin correction vector
    xlv = xlv + crv     #apply correction
        
    tmx = Xform.translation(xlv) #convert to chimera Xform (transformation matrix)
    return tmx

##def strmatch(s,p):
##    import re
##    nr = {}
##    regex = []
##    for c in p:
##        if c not in nr:
##            regex.append('(.+)')
##            nr[c] = len(nr) + 1
##        else:
##            regex.append('\\%d' % nr[c])
##
##    return bool(re.match(''.join(regex) + '$',s))

##def voltype(vol):
##    if vol.openedAs[1] == 'MRC density map':
##        print 'MRC FILE - ORIGIN CENTERED'
##    elif vol.openedAs[1] == 'SPIDER volume data':
##        print 'SPIDER DAT FILE - ORIGIN CENTERED'
##    elif vol.openedAs[1] == 'CCP4 density map':
##        print('CCP4 FILE - ORIGIN AT (0,0)')





#####_RUN SCRIPT_#####-------------------
#vols = chimera.selection.currentGraphs()
#vol = vols[0]
vols = om.list(modelTypes=[volume.Volume])

for vol in vols:
    vbx = vol.bbox()[1]
    vc = vbx.center()
    vllf = vbx.llf
    vurb = vbx.urb
    print('')
    print(vol.name_with_id())
    print("LLF: {}".format(vllf))
    print("Center: {}".format(vc))
    print("URB: {}".format(vurb))

    ###The Complete Transform & Inverse
    #vxf = vol.model_transform()
    #vxfi = vxf.inverse()
    
    ###Translation Matrix & Inverse
    tmx = get_tmx(vol)
    tmxi = get_tmx(vol,True)
    
    ###Rotation Matrix & Inverse
    rmx = get_rmx(vol)
    rmxi = get_rmx(vol,True)

    if vol.openedAs[1] == 'MRC density map':
        print 'MRC FILE - ORIGIN CENTERED'
    elif vol.openedAs[1] == 'SPIDER volume data':
        print 'SPIDER DAT FILE - ORIGIN CENTERED'
    elif vol.openedAs[1] == 'CCP4 density map':
        print('CCP4 FILE - ORIGIN AT (0,0)')

    print tmxi, rmxi
    
        
    tog = vllf-xlv
    togv = Point()-tog
    togv.negate()

    vos = vol.openState
    vos.globalXform(rmxi)
    vos.globalXform(tmxi)
    vos.globalXform(Xform.rotation(1,0,0,90))
    
    #print('TRANSLATION VECTOR: {}'.format(togv))
    #vos.globalXform(vxfi)
    #vos.globalXform(Xform.rotation(uv,a))
    #vos.globalXform(Xform.translation(togv))
