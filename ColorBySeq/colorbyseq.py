import os,chimera
tymera_path = os.path.dirname(os.path.dirname(__file__))
from tymera.commonfunctions import r2d, current_selection
from tymera.ColorBySeq.sequence_identifier import *

def color_chain(color_str):
    chain_objs = current_selection('Ch') #get the chain objects that you want to color
    for chain in chain_objs:
        cid = chain.chainID #chain ID of that chain object
        res = chain.residues #list of residue objects in the chain
        
        color = chimera.colorTable.getColorByName(color_str)

        #Color each residue (r) in the set of all residues in the chain (res)
        for r in res:
            if r != None:   #chain.residues will sometimes include a bunch of NoneType objects corresponding to atoms that are not part of residues, such as ligands or other non-protein structures; this statement avoids the error message that comes with trying to color an 'empty' residue object.
                r.ribbonColor = color  #the color attribute for residues is .ribbonColor, not .color (as you would for Molecule or Atom objects)

def cled_out():
    from chimera.coloreditor import Editor
    import time
    
    cled = Editor()
    time.sleep(1)
    if cled.isVisible() == False:          
        return cled.rgba
        

def color_by_seq():
    from chimera.colorTable import getColorByName
    color_key = {}
    color_key = r2d(tymera_path+'/ref/color_key.txt')

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

##if __name__ == '__main__':
##    color_by_seq()
