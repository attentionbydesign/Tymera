from chimera import openModels as om, runCommand as rc

mdls=[]
mdls=om.list()
class coords:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

mcrds = {}

for mdl in mdls:
    bbx_tpl = mdl.bbox()
    bbx = bbx_tpl[1]
    x,y,z = bbx.center()
    mcrds[mdl.id] = coords(x,y,z)
##bbox() method returns a two-value tuple; first is a boolean
##that reports if the bounding-box calculation was done/successful
##Second is the actual bounding-box object itself
##center() method returns the coordinates for the center of the
##bounding box object (assigned to the bbx variable, in this case)
##as a tuple, which is unpacked to x, y, z variables
##each of the x-z variables are assigned to the coords object class
##which are appended to the mcrds (model-coordinates) dictionary

m0_crds = (mcrds[0].x,mcrds[0].y,mcrds[0].z)
sx,sy,sz = m0_crds

for i in mcrds:
    #print i, mcrds[i].x, mcrds[i].y, mcrds[i].z
    dx = mcrds[i].x -sx
    dy = mcrds[i].y - sy
    dz = mcrds[i].z - sz
    args = [
        'x {} models #{}'.format(dx,str(i)),
        'y {} models #{}'.format(dy,str(i)),
        'z {} models #{}'.format(dz,str(i))
        ]
    print(dx,dy,dz)
    rc('move '+"; move ".join(args))


