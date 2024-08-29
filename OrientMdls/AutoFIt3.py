from chimera import openModels as om, runCommand as rc, Molecule
from VolumeViewer import volume
import numpy as np
import StructMeasure as sm

def cofralign():
    mdls=[]
    mdls=om.list()
    rc('cofr view')
    for m in mdls:
        rc('move cofr models #{}'.format(m.id))
    rc('cofr models')

def vol_uv(vol,axis_input):
    axky = {'x': 0, 'y': 1, 'z': 2}
    if type(axis_input) == str:
        axis = axky[axis_input]
    elif type(axis_input) == int:
        axis = axis_input
    uv = vol.axis_vector(axis)
    return uv

def vol_axes(vol):
    axes = []
    dg = 1
    axky = {0:'x', 1:'y', 2:'z'}
    for ax in axky:
        uv = vol_uv(vol,ax)
        axes.append(uv)
        x,y,z = uv
        print axky[ax],round(x,dg),round(y,dg),round(z,dg)
    #return axes

def vtest(vol,turnax):
    vol_axes(vol)
    rc('turn {} 90 models #{}'.format(turnax,vol.id))
    print('turn')
    vol_axes(vol)
    rc('turn {} -90 models #{}'.format(turnax,vol.id))

def vtest_all(vol):
    trxs = ['x','y','z']
    for trx in trxs:
        print('+90 DEG TURN ABOUT {}-axis:'.format(trx))
        vtest(vol,trx)

vtest_all(v)
    
mols = om.list(modelTypes=[Molecule])
vols = om.list(modelTypes=[volume.Volume])

m = mols[0]
v = vols[0]
vmp = vols[1] #molmap

atms = m.atoms
#a0 = atms[0]
#a1k = atms[1000]

rdig = 1

marr = chimera.numpyArrayFromAtoms(atms,xformed=True)
mpoint,mvect = sm.axis(marr)
mx,my,mz = mvect
#print round(mx,rdig),round(my,rdig),round(mz,rdig)

##get the unit vector in global coordinates that
##represents the current positioning of volume's z-axis
vax = v.axis_vector(0)
vx,vy,vz = vax
#print round(vx,rdig),round(vy,rdig),round(vz,rdig)




##def principal_axes_of_molecule(molecule):
##    # Calculate center of mass
##    atoms = molecule.atoms
##    coords = np.array([atom.coord().data() for atom in atoms])
##    center_of_mass = coords.mean(axis=0)
##
##    # Center the molecule at the origin
##    centered_coords = coords - center_of_mass
##
##    # Calculate inertia tensor
##    inertia_tensor = np.dot(centered_coords.T, centered_coords)
##    
##    # Compute eigenvalues and eigenvectors
##    eigenvalues, eigenvectors = np.linalg.eigh(inertia_tensor)
##    
##    # The eigenvectors are the principal axes
##    return eigenvectors
