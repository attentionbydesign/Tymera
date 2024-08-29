
def mol_select():
    sel_mols = chimera.selection.currentMolecules()
    mobj_sel = sel_mols[0]
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

def color_chain():
    chain = chain_select() #get the chain object that you want to color
    cid = chain.chainID #chain ID of that chain object
    res = chain.residues #list of residue objects in the chain
    
    color = input("Enter color: ") #you can enter the color name since the MaterialColor objects have been assigned to them at the beginning

    #Color each residue (r) in the set of all residues in the chain (res)
    for r in res:
        if r != None:   #chain.residues will sometimes include a bunch of NoneType objects corresponding to atoms that are not part of residues, such as ligands or other non-protein structures; this statement avoids the error message that comes with trying to color an 'empty' residue object.
            r.ribbonColor = color  #the color attribute for residues is .ribbonColor, not .color (as you would for Molecule or Atom objects) 

def color_by_protein():
  'Color by protein.'
  from chimera.colorTable import getColorByName
  chain_key = {}
  chain_key = r2d('cky.txt')
  color_key = {}
  color_key = r2d('clrky.txt')
  
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
          print cobj.chainID, i, similarity
          
          if similarity > 40:
              print cobj.chainID, i, similarity
              print aligned_seq1
              print aligned_seq2
              if color_key.get(i) != None:
                  #rc("color "+color_key[i]+" "+str(cobj.molecule)+":."+cobj.chainID)
                  res = cobj.residues
                  color = getColorByName(color_key[i])
                  for r in res:
                      if r != None:
                          r.ribbonColor = color
color_by_protein()
