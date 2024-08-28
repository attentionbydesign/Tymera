import chimera, os
from chimera import openModels

tymera_path = os.path.dirname(os.path.dirname(__file__))

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
  chain_key = r2d('C:/ProgramData/Chimera/cky.txt')
  color_key = {}
  color_key = r2d('C:/ProgramData/Chimera/clrky.txt')
  
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
##          print cobj.chainID, i, similarity
          
          if similarity > 40:
##              print cobj.chainID, i, similarity
##              print aligned_seq1
##              print aligned_seq2
              if color_key.get(i) != None:
                  #rc("color "+color_key[i]+" "+str(cobj.molecule)+":."+cobj.chainID)
                  res = cobj.residues
                  color = getColorByName(color_key[i])
                  for r in res:
                      if r != None:
                          r.ribbonColor = color

def color_by_seq():
    from tymera.ColorBySeq import colorbyseq,sequence_identifier
    colorbyseq.color_by_seq()

#-----------------
def active_select():
    #from VolumeViewer import volume_list
    mlist = chimera.openModels.list()
    #slist = chimera.selection.currentMolecules()
    slist = chimera.selection.currentGraphs()
    ulist = [x for x in mlist if x not in slist]

    for s in slist:
        chimera.openModels.setActive(s.id, True)
    for u in ulist:
        chimera.openModels.setActive(u.id, False)


##----------------------------------

#Display ONLY SELECTED models:
def shoS():
    from chimera import runCommand as rc
    mlist = chimera.openModels.list()
    slist = chimera.selection.currentGraphs()
    ulist = [x for x in mlist if x not in slist]

    for s in slist:
        rc("modeldisplay #"+str(s.id))
    for u in ulist:
        rc("~modeldisplay #"+str(u.id))

#Display ALL models:
def shoA():
    from chimera import runCommand as rc
    mlist = chimera.openModels.list()
    for model in mlist:
        mid = model.id
        rc("modeldisplay #"+str(mid))

#Returns list of all currently displayed models
def get_displayed():
    shown_list = []
    mlist = chimera.openModels.list()
    for m in mlist:
        state = m.display
        print m.id, state
        if state == True:
            shown_list.append(m)
    return shown_list

#Toggles between showing ALL vs. ONLY SELECTED models:
def shoToggl():
    mlist = chimera.openModels.list()
    dlist = get_displayed()
    if len(dlist) == len(mlist):
        shoS()
    else:
        shoA()

#---------------------------------------------------

def vox_set():
    from chimera import openModels as om
    from VolumeViewer import volume

    vols = om.list(modelTypes=[volume.Volume])
    #v.name[len(v.name)-3:len(v.name)] will get you the file extension - if it's 'dat' then set the step_size?

    for v in vols:
        box_dim = v.data.size
        step_size = v.data.step
        x,y,z = box_dim
        if x == y == z:
            print("Volume #{} is a cube of {}px^3".format(v.id,x))
            
            sf = 396 / x
            vs = 1.356 * sf
            step = (vs,vs,vs)
            v.data.set_step(step)
            v.show()
        else:
            print("Volume #{} dimensions: {}px x {}px x {}px".format(v.id,x,y,z))
            ogs = v.data.original_step
            print("Original step: {}".format(ogs))
            v.data.set_step(ogs)
            v.show()

#---------------------------------------------------

def orientmdls():
    from tymera import OrientMdls
    OrientMdls.orient_all()

#---------------------------------------------------

def default_tbc():
    from chimera import openModels as om,runCommand as rc
    from VolumeViewer import volume
    vols = om.list(modelTypes=[volume.Volume])

    for v in vols:
        rc("volume #{} transparency 0.3 brightness 0.7".format(v.id))

#------------------

def register_accelerators():

  from Accelerators import standard_accelerators
  standard_accelerators.register_accelerators()

  from Accelerators import add_accelerator
  add_accelerator('om','Orient models to global Y-axis and origin', orientmdls)
  add_accelerator('cb', 'Color chains of selected model by protein type', color_by_seq)
  add_accelerator('as', 'Activate only selected model', active_select)
  add_accelerator('sw', 'Toggle show only selected model / show all', shoToggl)
  add_accelerator('vx', 'Set voxelSize of all volumes based on box dimensions', vox_set)
  add_accelerator('vd', 'Custom volume display transparency and brightness', default_tbc)
register_accelerators()

