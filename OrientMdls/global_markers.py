#script to mark the global coordinate system origin and axes

import chimera, VolumePath
from chimera import Point, Vector, Xform, numpyArrayFromAtoms, angle, cross

black = (0,0,0,1)
axlen = 100


##globaxs = VolumePath.Marker_Set('GlobalAxes')
##globaxs.place_marker((0,0,0),black,5)
##globaxs.place_marker((axlen,0,0),black,3)
##globaxs.place_marker((0,axlen,0),black,3)
##globaxs.place_marker((0,0,axlen),black,3)

##if globaxs == None:
##    create_axes()

gaos = globaxs.molecule.openState

op = globaxs.markers()[0]
op.atom.label = 'O'
xp = globaxs.markers()[1]
xp.atom.label = 'X'
yp = globaxs.markers()[2]
yp.atom.label = 'Y'
zp = globaxs.markers()[3]
zp.atom.label = 'Z'

oglob = op.atom.xformCoord()
xglob = xp.atom.xformCoord()
yglob = yp.atom.xformCoord()
zglob = zp.atom.xformCoord()

toX = Point(axlen,0,0) - xglob
toY = Point(0,axlen,0) - yglob
toZ = Point(0,0,axlen) - zglob

xax = xglob - oglob
yax = yglob - oglob
zax = zglob - oglob

thx = angle(xax,Vector(1,0,0))
xrtax = cross(xax,Vector(1,0,0))
xrot = Xform.rotation(xrtax,thx)
gaos.globalXform(xrot)

thy = angle(yax,Vector(0,1,0))
yrtax = cross(yax,Vector(0,1,0))
yrot = Xform.rotation(yrtax,thy)
gaos.globalXform(yrot)

thz = angle(zax,Vector(0,0,1))
zrtax = cross(zax,Vector(0,0,1))
##zrot = Xform.rotation(zrtax,thz)
##gaos.globalXform(zrot)

#print xax,'\n',yax,'\n',zax

loccrds = numpyArrayFromAtoms(globaxs.molecule.atoms)
globcrds = numpyArrayFromAtoms(globaxs.molecule.atoms,xformed=True)








# def mark_origin():
#     #create atom marker object?#
# ##    import BuildStructure as bs
# ##    He = bs.placeHelium('He_Res','Origin')
# ##    He.label="Origin"
# ##    coords = numpyArrayFromAtoms([He], xformed=True)[0]
# ##    x,y,z = coords[0],coords[1],coords[2]
# ##    marker = Point(x,y,z)
# ##    toOrigin = marker - Point(0,0,0)
# ##    HeOS = He.molecule.openState
# ##    HeOS.globalXform(Xform.translation(toOrigin))
#     origin = create_marker('O')
#     om = origin.place_marker((0,0,0),(0,0,0,1),5)
#     om.atom.label='O'

# def mark_ax(ax):
#     axlen = 100
#     if ax == 'y':
#         y = create_marker('Y')
#         y.place_marker((0,axlen,0),(0,0,0,1),3)
#         y.markers()[]

#         ycoord = Point(x,y,z)
#     if ax == 'x':
#         x = create_marker('X')
#         xm = x.place_marker((axlen,0,0),(0,0,0,1),3)
#         xm.atom.label='X'
#     if ax == 'z':
#         z = create_marker('Z')
#         zm = z.place_marker((0,0,axlen),(0,0,0,1),3)
#         zm.atom.label='Z'

# def main():
#     mark_origin()
#     for i in ['x','y','z']:
#         mark_ax(i)

# if __name__ == '__main__':
#     main()

    
    
    

