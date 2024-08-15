from chimera import openModels as om, Molecule, UserError, numpyArrayFromAtoms, Point
from chimera import Xform, Point, cross, angle, Vector



#from chimera import Xform, Point, cross, angle, Vector

def actopen():
    from chimera import openModels as om, runCommand as rc
    if om.list() == []:
        rc('open 3j8i')
    else:
        for mdl in om.list():
            if mdl.name == '3j8i':
                #print("3j8i currently open as Model #{}".format(mdl.id))
                break
            else:
                rc('open 3j8i')
  
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

###if y component of actin axis is negative, then flip the model upside down to correct###
def ypolcorr():
    av = fav()
    if av.y < 0:
        for mol in om.list():
            if mol.name == '3j8i':
                mdl = mol
        mos = mdl.openState
        mos.globalXform(Xform.rotation(1,0,0,180))

def mol_select():
    mol_objs = chimera.openModels.list()
    for mobj in mol_objs:
        print "#"+str(mobj.id), mobj.name
    mid = input("Model ID#: ")
    for mobj in mol_objs:
        if mobj.id == mid:
            mobj_sel = mobj
    return mobj_sel

def chain_select():
    m = mol_select(mid)
    chain_objs = m.sequences()
    for cobj in chain_objs:
        print cobj.chainID, len(cobj)
    cid = raw_input("Chain ID: ")
    for cobj in chain_objs:
        if cobj.chainID == cid:
            cobj_sel = cobj
    return cobj_sel

def r2d(filename):
    result_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            columns = line.split()
            if len(columns) == 2:
                key = columns[0]
                value = columns[1]
                result_dict[key] = value
    return result_dict
    file.close()

def align_sequences(short_seq, long_seq):
    max_similarity = 0
    best_alignment = ("", "")

    short_len = len(short_seq)
    long_len = len(long_seq)

    sass={}
    for i in range(long_len - short_len + 1):
        substring = long_seq[i:i + short_len]
        similarity = sum(1 for a, b in zip(short_seq, substring) if a == b)
        sass[substring] = similarity
        
    best_substring = max(sass, key=sass.get)
    best_alignment = (short_seq, best_substring)
    
    return best_alignment

def calculate_similarity(seq1, seq2):
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = float(matches) / len(seq1) * 100
    return similarity

def get_faco(mol):
    chain_objs = mol.sequences()
    for cobj in chain_objs:
        cseq = str(cobj)
        for i in chain_key:
            s1 = cseq
            s2 = chain_key[i]
            if len(s1) > len(s2):
                short_sequence = s2
                long_sequence = s1
            else:
                short_sequence = s1
                long_sequence = s2
            aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)
            similarity = calculate_similarity(aligned_seq1, aligned_seq2)
            if similarity > 52:
                print cobj.chainID, i, similarity
                if i == "Actin":
                    first_actin = cobj
                    break #this alone only breaks out of the current loop
    ##            (for i in chain_key...etc.), not the loop it is nested
    ##            within (for cobj in chain_objs...) - adding the next 3
    ##            lines indented so it happens after the inner loop is what
    ##            stops the whole thing.
        else:
            continue
        break
    return first_actin

def fav():
    from chimera import openModels as om, Molecule, UserError, numpyArrayFromAtoms, Point
    from chimera import Xform, Point, cross, angle, Vector, openModels as om, runCommand as rc

    aos = None; mdl = None

    for mol in om.list():
        type(mol)
        if mol.name == '3j8i':
            mdl = mol

    faco = get_faco(mdl) #chain obj for first actin
    
    ma = mdl.atoms
    fac_atms=[]
    for a in ma:
        if a.residue.id.chainId == faco.chainID:
            fac_atms.append(a)

    for a in fac_atms:
        if a.residue.id.position == 44:
            natm = a
        elif a.residue.id.position == 170:
            satm = a

    np = natm.xformCoord()
    sp = satm.xformCoord()

    gav = np - sp

    return gav
    
actopen()
orient('all')
ypolcorr()
            
