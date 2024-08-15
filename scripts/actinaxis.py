from chimera import runCommand as rc, openModels as om

##mid = 1
cid = 'D'

#residue numbers/positions of north (pointed) and south (barbed), respectively; chose SER60, GLY168
rp=[60,168]

##get a single point representing a pole as defined above - arguments
##are (1) mid =  model id and (2) pos = residue position (e.g., 60 for SER60)
def getpole(mid,pos):
    rc('select #{}:{}.{}@CA'.format(mid,pos,cid))
    atm = chimera.selection.currentAtoms()
    a = atm[0]
    crd = a.xformCoord()
    return crd

def getactinvect(mid):
    import math
    #Get north and south pole coordinates
    Np = getpole(mid,rp[0])
    Sp = getpole(mid,rp[1])

    #subtract north point by south point to get S-->N axis vector
    av = Np - Sp

    #get actin vector magnitude
    avm = math.sqrt(sum(i**2 for i in av))

    #divide actin vector by its magnitude to get unit axis vector
    uv = av / avm
    return uv

def getSMaxis(mid):
    from chimera import openModels as om
    import StructMeasure as sm
    mdls = om.list()
    m = mdls[mid]
    at = m.atoms
    npar = chimera.numpyArrayFromAtoms(at, xformed=True)
    axobj = sm.axis(npar)
    axvect = axobj[1]
    return axvect

#get alignment of molecule axis vector with the lab Y-axis as a percentage
##def get_molalign():
##    maxis = getactinvect()
##    x,y,z = maxis
##    yalign = str(round(y*100,2))
##    return yalign

def corrSMpol(mid):
    actaxis = getactinvect(mid)
    ax,ay,az = actaxis
##    print('Actin axis vector: {}'.format(actaxis))
##    print('y-component: '+str(round(ay)))
##    print ""
    mdlaxis = getSMaxis(mid)
    mx,my,mz = mdlaxis
##    print('Model axis vector: {}'.format(mdlaxis))
##    print('y-component: '+str(round(my)))
    if round(ay) == -round(my):
        print('AXES INVERTED')
##        print ""
        return -mdlaxis
    else:
        return mdlaxis

def mdltype(mid):
    from chimera import openModels as om
    mdls = om.list()
    mdl = mdls[mid]
    if str(type(mdl)) == "<class 'VolumeViewer.volume.Volume'>":
        mdltype = 'vol'
    elif str(type(mdl)) == "<type '_molecule.Molecule'>":
        mdltype = 'mol'
    else:
        print "---unknown model type---"
        mdltype = None
    return mdltype


#---REFERENCE_VOLUME---#----------------------------------------------------
def getvobj(mid):
    from chimera import openModels
    from VolumeViewer import volume
    volumes = openModels.list(modelTypes=[volume.Volume])
    for vobj in volumes:
        if vobj.id == mid:
            return vobj

def getvax(mid):
    if mdltype(mid) != 'vol':
        print "ERROR: Model ID is not associated with Volume"
    else:
        from chimera import openModels as om
        mdls = om.list()
        v = mdls[mid]
        vax = v.axis_vector(2)
        vx,vy,vz = vax
        cvax = (-vx,-vy,-vz)
        return cvax

#print "Volume is {}% aligned with laboratory Y-axis".format(str(round(-vy*100,2)))



def align_model(mid):

    #translate to center
    from chimera import runCommand as rc, openModels as om
##    mdls = om.list()
    rc('cofr front')
##    for mdl in mdls:
##        rc('move cofr models #{}'.format(mdl.id))
    rc('move cofr models #{}'.format(mid))
    rc('cofr models')
    
    

    #align central axes to lab y-axis
    phi = 1
    while phi > 0:
        from math import atan, acos, pi
        if mdltype(mid) == 'mol':
            maxis = corrSMpol(mid)
        elif mdltype(mid) == 'vol':
            maxis = getvax(mid)
        x,y,z = maxis
        theta = atan(x/z)*180/pi
        phi = acos(y)*180/pi
        print('theta: {}, phi: {}'.format(theta, phi))
        rc('turn y {} models #{}'.format(-theta,mid))
        rc('turn x {} models #{}'.format(-phi,mid))


mdls = om.list()
for mdl in mdls:
    mid = mdl.id
    align_model(mid)
