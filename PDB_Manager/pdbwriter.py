# more intuitive extension for saving or combining
# different molecules
# that doesn't create the ENDMDLS header or include
# secondary structure from kssdp or whatever
from tymera.commonfunctions import current_selection

def uniqchron(help=False):
    import time
    loct = time.localtime(time.time())

    if help == True:
        print loct
    else:
        uniqtpl = loct[0:6]
        uniqstr = int(''.join(map(str,uniqtpl)))
        return uniqstr

def pdbjoin():
    mdls = current_selection()
    relMdl = mdls[0] #which model to save the new PDB relative to
    
    chronID = uniqchron()
    output_name = 'JointMDL-'+str(chronID)+'.pdb'

    import os
    output_loc = os.path.dirname(mdls[0].openedAs[0])
    outpath = output_loc + '/' + output_name
    
    import Midas
    Midas.write(mdls, relMdl, outpath, selOnly=True)

    import chimera
    chimera.openModels.open(outpath,type='PDB')
