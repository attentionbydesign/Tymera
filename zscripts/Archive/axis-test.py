from chimera import openModels as om, runCommand as rc, Molecule
from VolumeViewer import volume
import numpy as np
import StructMeasure as sm

def mol_select():
    sel_mols = chimera.selection.currentMolecules()
    mobj_sel = sel_mols[0]
    return mobj_sel

##prints coordinates of alpha carbon of selected residue
##in the model's coordinate system (not transformed)
def scrd():
    crAs = chimera.selection.currentAtoms()
    for a in crAs:
        if a.name == 'CA':
            print a.coord()

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

    for i in range(long_len - short_len + 1):
        substring = long_seq[i:i + short_len]
        similarity = sum(1 for a, b in zip(short_seq, substring) if a == b)
        if similarity > max_similarity:
            max_similarity = similarity
            best_alignment = (short_seq, substring)

    return best_alignment

def calculate_similarity(seq1, seq2):
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    similarity = float(matches) / len(seq1) * 100
    return similarity

#transformed axis object (tuple of centroid and vector objects)
def axobj(Atoms):
    import StructMeasure as sm
    npar = chimera.numpyArrayFromAtoms(Atoms, xformed=False)
    axobj = sm.axis(npar)
    return axobj

#axis 'vector' from Atoms
def axvec(Atoms):
    pt, vec = axobj(Atoms)
    return vec

#centroid from Atoms
def axpt(Atoms):
    pt, vec = axobj(Atoms)
    return pt

#returns list of Atom objects that belong to Actin in the selected model
def actoms():
    chain_key = {}
    chain_key = r2d('C:/ProgramData/Chimera/cky.txt')
    ActinChains = []
    TpmChains = []
    m = mol_select()
    chain_objs = m.sequences()
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
              
            long_buff_length = int(float(len(short_sequence)) * 0.05)
            
            for count in range(long_buff_length):
                long_sequence = 'X' + long_sequence + 'X'
              
            aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)
            similarity = calculate_similarity(aligned_seq1, aligned_seq2)
##            print cobj.chainID, i, similarity

            if similarity > 40:
##                print cobj.chainID, i, similarity
                if i == "Actin":
                    ActinChains.append(cobj.chainID)
                if i == "Tpm":
                    TpmChains.append(cobj.chainID)
##    print ActinChains
##    print ""
##    print TpmChains

    ActinAtoms = []
    for at in m.atoms:
        acid = at.residue.id.chainId
        for ch in ActinChains: 
            if acid == ch:
                ActinAtoms.append(at)
    return ActinAtoms

#-----#

print axpt(actoms())
print axvec(actoms())
print ""




#-------------------------

mols = om.list(modelTypes=[Molecule])
vols = om.list(modelTypes=[volume.Volume])

m = mols[0]
v = vols[0]

a = m.atoms
arx = chimera.numpyArrayFromAtoms(a,xformed=True)
aro = chimera.numpyArrayFromAtoms(a,xformed=False)
#axpts = a.xformCoord()

xfax=sm.axis(arx)
ogax=sm.axis(aro)

#print ogax
pto,vaxo = ogax
pt,vax = xfax

ox,oy,oz = vaxo
tx,ty,tz = vax
d = 1
print round(ox,d),round(oy,d),round(oz,d)
print round(tx,d),round(ty,d),round(tz,d)
print ''
print pto
scrd()

            
    



