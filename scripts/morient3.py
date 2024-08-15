
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
    print("Running get_faco(mol) for {}".format(mol.name))
    chain_key = r2d('cky.txt')
    chain_objs = mol.sequences()
    first_actin = None
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
                    break
        else:
            continue
        break
    return first_actin
    
def get_acvec(mol):
    print("Running get_acvec(mol) for {}".format(mol.name))
    
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
    print("Running actin_polcorr(mol) for {}".format(mol.name))
    from chimera import Xform
    if get_acvec(mol):
        av = get_acvec(mol)
        if av.y < 0:
            mos = mol.openState
            mos.globalXform(Xform.rotation(1,0,0,180))

def orient_run(mol):
    print("Running orient_run(mol) for {}".format(mol.name))
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


    ###ROTATION###
    
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


def orient_mols():
    from chimera import openModels, Molecule
    mols = openModels.list(modelTypes=[Molecule])
    for mol in mols:
        print ""
        print("___ORIENTING #{}: {}___".format(mol.id,mol.name))
        orient_run(mol)
        actin_polcorr(mol)
        print ""

orient_mols()
    
