from chimera import openModels, Molecule, UserError, numpyArrayFromAtoms, Point


def meet():
    import StructMeasure as sm
    sl = chimera.selection.currentMolecules()
    m1 = sl[0]
    m2 = sl[1]
    crd1 = numpyArrayFromAtoms(m1.atoms, xformed=True)
    crd2 = numpyArrayFromAtoms(m2.atoms, xformed=True)
    p1 = sm.bestLine(crd1)[0]
    p2 = sm.bestLine(crd2)[0]
    vec = (p2 - p1) / 2
    os1 = m1.openState
    os2 = m2.openState
    os1.globalXform(Xform.translation(vec))
    os2.globalXform(Xform.translation(-vec))
    
def orient_run(mol):
    coords = numpyArrayFromAtoms(mol.atoms, xformed=True)
    from StructMeasure import bestLine
    centroidPt, majorVec, centroidArray, majorArray, centered, vals, vecs = \
                    bestLine(coords)
    sortableVecs = zip(vals, vecs)
    sortableVecs.sort()
    sortableVecs.reverse()

    from chimera import Xform, Point, cross, angle, Vector
    openState = mol.openState
    toOrigin = Point() - centroidPt
    sv1, sv2 = sortableVecs[0][1], sortableVecs[1][1]
    v1 = Vector(*sv1)
    v2 = Vector(*sv2)
    openState.globalXform(Xform.translation(toOrigin))
    # major axis onto Y
    y_axis = Vector(0.0, 1.0, 0.0)
    delta = angle(y_axis, v1)
    if abs(delta) > 0.001 and abs(180.0 - delta) > 0.001:
            rotAxis = cross(y_axis, v1)
            rot = Xform.rotation(rotAxis, -delta)
            #openState.globalXform(rot)
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

def orient(mdl):
    if mdl == None and chimera.selection.currentMolecules() != []:
        mdls = chimera.selection.currentMolecules()
        for mol in mdls:
            orient_run(mol)
    elif type(mdl) == int:
        mdls = openModels.list()
        for mol in mdls:
            if mol.id == mdl:
                orient_run(mol)
    elif mdl == 'all':
        mdls = openModels.list(modelTypes=[Molecule])
        for mol in mdls:
            orient_run(mol)
    else:
        print('ERROR: select model in GUI, specify model number, or enter "all" to orient models')

orient('all')
