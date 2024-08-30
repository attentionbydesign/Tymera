import chimera, os
tymera_path = os.path.dirname(os.path.dirname(__file__))
from tymera.ColorBySeq import sequence_identifier
from tymera.commonfunctions import r2d

##return <chimera.Sequence.StructureSequence object> of the
##first listed actin chain in the molecule
##(faco = "first actin chain object")
def get_faco(mol):
    #print("Running get_faco(mol) for {}".format(mol.name))
    chain_key = r2d(tymera_path+'/ref/chain_key.txt')
    chain_objs = mol.sequences()
    first_actin = None
    for cobj in chain_objs:
        match = sequence_identifier.identify_seq(cobj)
        if match == "Actin":
            first_actin = cobj
            break
        else:
            continue
        break
    return first_actin

##get vector from barbed to pointed end of first actin chain
def get_acvec(mol):
    #print("Running get_acvec(mol) for {}".format(mol.name))
    
    if get_faco(mol):
        faco = get_faco(mol) #chain obj for first actin
        ma = mol.atoms
        fac_atms=[]; a=None
        for a in ma:
            if a.residue.id.chainId == faco.chain:
                fac_atms.append(a)

        for a in fac_atms:
            if a.residue.id.position == 44:
                natm = a
            elif a.residue.id.position == 170:
                satm = a

        np = natm.xformCoord()
        sp = satm.xformCoord()

        actin_vector = np - sp

        print("Actin Vector (Barbed > Pointed): {}".format(actin_vector))

        return actin_vector

def actin_polcorr(mol):
    #print("Running actin_polcorr(mol) for {}".format(mol.name))
    from chimera import Xform, angle, Vector, Point, cross
    if get_acvec(mol):
        av = get_acvec(mol)
        y_axis = Vector(0,1,0)
        delta = angle(av, y_axis)
        rotax = cross(av, y_axis)
        if abs(delta) > 0.0001:
            mos = mol.openState
            mos.globalXform(Xform.rotation(rotax,delta))

def orient_run(mol):
    #print("Running orient_run(mol) for {}".format(mol.name))
    from chimera import numpyArrayFromAtoms, Xform, Point, cross, angle, Vector
    coords = numpyArrayFromAtoms(mol.atoms, xformed=True)
    from StructMeasure import bestLine
    
    centroidPt, majorVec, centroidArray, majorArray, centered, vals, vecs = \
                    bestLine(coords)
    sortableVecs = zip(vals, vecs)
    sortableVecs.sort()
    sortableVecs.reverse()

    openState = mol.openState

    ###TRASLATION###
    toOrigin = Point() - centroidPt
    sv1, sv2 = sortableVecs[0][1], sortableVecs[1][1]
    v1 = Vector(*sv1)
    v2 = Vector(*sv2)
    openState.globalXform(Xform.translation(toOrigin))
    print v1, v2

    ###ROTATION###
    
    # major axis onto Y
    y_axis = Vector(0.0, 1.0, 0.0)
    delta = angle(y_axis, v1)
    print("Delta = {}".format(delta))
    if abs(delta) > 0.001 and abs(180.0 - delta) > 0.001:
            rotAxis = cross(y_axis, v1)
            rot = Xform.rotation(rotAxis, -delta)
            openState.globalXform(rot)
            rv2 = rot.apply(v2)
    else:
            rv2 = v2

    # second axis onto X
    x_axis = Vector(1.0, 0.0, 0.0)
    delta = angle(x_axis, rv2)
    if abs(delta) > 0.001 and abs(180.0 - delta) > 0.001:
            rotAxis = cross(x_axis, rv2)
            rot = Xform.rotation(rotAxis, -delta)
            openState.globalXform(rot)
            print('2nd-Axis onto X:'+"\n\n"+str(rotAxis))


def run_om():
    from chimera import openModels, Molecule
    mols = openModels.list(modelTypes=[Molecule])
    for mol in mols:
        print ""
        print("___ORIENTING #{}: {}___".format(mol.id,mol.name))
        orient_run(mol)
        actin_polcorr(mol)
        print ""

if __name__ == '__main__':
    from chimera import selection
    selected_mols = selection.currentMolecules()
    tmol = selected_mols[0]
    for mol in selected_mols:
        orient_run(mol)
        actin_polcorr(mol)
