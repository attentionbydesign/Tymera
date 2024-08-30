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

def current_selection(level='Gr',verbose=False,menu=False):
    from chimera import selection

    pattern = 'current'

    options = [item for item in dir(selection) if pattern in item]    #all methods of chimera.selection that contain "current" in their name

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
