import chimera
from chimera import openModels, runCommand as rc
from chimera.colorTable import getColorByName

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

def color_chain():
    chain = chain_select() #get the chain object that you want to color
    cid = chain.chainID #chain ID of that chain object
    res = chain.residues #list of residue objects in the chain
    
    color = input("Enter color: ") #you can enter the color name since the MaterialColor objects have been assigned to them at the beginning

    #Color each residue (r) in the set of all residues in the chain (res)
    for r in res:
        if r != None:   #chain.residues will sometimes include a bunch of NoneType objects corresponding to atoms that are not part of residues, such as ligands or other non-protein structures; this statement avoids the error message that comes with trying to color an 'empty' residue object.
            r.ribbonColor = color  #the color attribute for residues is .ribbonColor, not .color (as you would for Molecule or Atom objects)

    
chain_key = {}
chain_key = r2d('cky.txt')
color_key = {}
color_key = r2d('clrky.txt')

while True:
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
            aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)
            similarity = calculate_similarity(aligned_seq1, aligned_seq2)
            if similarity > 52:
                print cobj.chainID, i
                if color_key.get(i) != None:
                    #rc("color "+color_key[i]+" "+str(cobj.molecule)+":."+cobj.chainID)
                    res = cobj.residues
                    color = getColorByName(color_key[i])
                    for r in res:
                        if r != None:
                            r.ribbonColor = color
