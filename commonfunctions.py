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


#-----------------------------------------------------------------


#Select whole chains, INCLUDING items not connected (e.g., ligands)
def select_chains():
    #Get unique molecule:chain pairs in current selection
    def get_uniq_mcps():
        mcps = []
        for r in current_selection('Re'):
            mcstr = str(r.molecule.id) + ":" +str(r.id.chainId)
            mcps.append(mcstr)
        uniq_mcps = list(set(mcps))
        return uniq_mcps

    #Get chain objects of unique pairs
    def get_chainz():
        chainz = []
        for mol in current_selection('Mo'):
            for chain in mol.sequences():
                molc = str(mol.id)+':'+chain.chainID
                if molc in get_uniq_mcps():
                    print chain.molecule,chain.name
                    chainz.append(chain)
        return chainz

    #Select the chains of unique pairs; must be done via substituent residues, as chains (i.e., sequence objects) do not have a defined oslLevel.  That is, the oslLevel hierarchy is
        # Molecule    1
        # Residue     2
        # Atom        3 
    # (There is nothing between 1 and 2 for Chains/Sequences)
    chains = get_chainz()
    residues = []
    for c in chains:
        for r in c.molecule.residues:
            if r.id.chainId == c.chainID and r.molecule.id == c.molecule.id:
                residues.append(r)
    chimera.selection.setCurrent(residues)
    

#-----------------------------------------------------------------

def current_selection(level='Gr',verbose=False,menu=False):
    from chimera import selection

    pattern = 'current'

    options = [item 
        for item in dir(selection) 
        if pattern in item
        ]    #all methods of chimera.selection that contain "current" in their name

    optdict = {}
    for o in options:
        if '_' not in o:
            psi = o.find(pattern)
            c1 = psi + len(pattern)
            abbrev = o[c1:c1+2]
            optdict[abbrev] = o + '()'
    
    #Option to show menu items & their abrreviations
    if menu == True:
        for abbr in optdict:
            print abbr, optdict[abbr]
    
    else:
        method = optdict[level]
        csel = eval('selection.'+method)

        if verbose == True:
            print("Returned list of {} in current selection:\n".format(method[len(pattern):len(method)-2]))
            
        return csel
