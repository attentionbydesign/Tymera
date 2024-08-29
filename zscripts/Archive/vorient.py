from chimera import openModels as om, Point, Vector
import numpy as np

def cofm(nparr):
    # Generate coordinates for each dimension
    x,y,z = np.indices(nparr.shape)

    # Calculate the total mass
    total_mass = nparr.sum()

    # Compute the center of mass along each axis
    x_center_of_mass = (x * nparr).sum() / total_mass
    y_center_of_mass = (y * nparr).sum() / total_mass
    z_center_of_mass = (z * nparr).sum() / total_mass

    center_of_mass = (x_center_of_mass, y_center_of_mass, z_center_of_mass)

    return center_of_mass

def vori(vol):
    
    vos = vol.openState

    ###bounding box center (local coord)###
    vbx = vol.bbox()[1]
    #print vbx.center()

    ###transformation to global###
    vxf = vol.model_transform()
    vxf.invert()
    xlv = vxf.getTranslation()

    vm = vol.matrix()

    ###center of mass###
    print("Center of Mass (local) {}".format(cofm(vm)))
    cx,cz,cy = cofm(vm)
    cfmp = Vector(cx,cy,cz)
    cxlv = cfmp - xlv
    print("Center of Mass (global) {}".format(cxlv))

    toOrigin = Point() - cxlv
    ox,oy,oz = toOrigin
    tov = Vector(ox,oy,oz)

    ###maximum density###
    vmx = vm.max()
    npw = np.where(vm == vmx)
    mxd = np.array([npw[0][0],npw[1][0],npw[2][0]])
    mxdp = Point(mxd[0],mxd[1],mxd[2])
    #print("Max Density (local) {}".format(mxd))

    globmxd = mxd - xlv

    #print("Max Density (global) {}".format(globmxd))

    #toOrigin = -Vector(globmxd[0],globmxd[1],globmxd[2])

    #print toOrigin

    #vos.globalXform(Xform.translation(tov))

    #print xlv

    vos.globalXform(vxf)


vols = chimera.selection.currentGraphs()
#vol = vols[0]
for vol in vols:
    vori(vol)

