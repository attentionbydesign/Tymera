import chimera
from chimera import openModels, runCommand as rc
from chimera.colorTable import getColorByName

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

def identify_seq(cobj,calcsim=False):
    chain_key = {}
    chain_key = r2d('../ref/chain_key.txt')
    seq1 = str(cobj)
    match_rank = {}

    for sname in chain_key:
        seq2 = chain_key[sname]
        if len(seq1) > len(seq2):
            short_sequence = seq2
            long_sequence = seq1
        else:
            short_sequence = seq1
            long_sequence = seq2

        ###FLANKING SEQUENCE BUFFER###
        long_buff_length = int(float(len(short_sequence)) * 0.05) 
        for count in range(long_buff_length):
            long_sequence = 'X' + long_sequence + 'X'
        ###------------------------###

        aligned_seq1, aligned_seq2 = align_sequences(short_sequence, long_sequence)

        similarity = calculate_similarity(aligned_seq1, aligned_seq2)

        match_rank[similarity] = sname
    max_similarity = max(match_rank)
    best_match = match_rank[max_similarity]

    #print best_match, max_similarity
    if calcsim == True:
        return max_similarity
    else:
        return best_match

def color_by_seq():
    color_key = {}
    color_key = r2d('../ref/color_key.txt')

    mols_seld = chimera.selection.currentMolecules()

    if mols_seld == []:
        print "Please select model to color."
    else:
        print "ID",'\t','MATCH','\t','SIMILARITY (%)','\t','COLOR','\n======================================='
        for mol in mols_seld:
            chain_objs = mol.sequences()
            for cobj in chain_objs:
                bestname = identify_seq(cobj)
                if color_key[bestname] != None:
                    resids = cobj.residues
                    color = getColorByName(color_key[bestname])
                    for res in resids:
                        if res != None:
                            res.ribbonColor = color
                maxsim = identify_seq(cobj,True)
                print cobj.chain,'\t',bestname,'\t',maxsim,'\t', color.name()
