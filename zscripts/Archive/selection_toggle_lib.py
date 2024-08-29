from chimera import openModels

##def mol_select():
##    sel_mols = chimera.selection.currentMolecules()
##    mobj_sel = sel_mols[0]
##    return mobj_sel

##def active_select():
def asel():
    mlist = chimera.openModels.list()
    slist = chimera.selection.currentMolecules()
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
    slist = chimera.selection.currentMolecules()
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
##something like this exists for toggling active
##states ('at' shortcut) but not for display states
    
            
    




