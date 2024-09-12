from chimera import openModels as om, selection as sl, Molecule

def activate_selected():
    allmodels = om.list()
    selected = sl.currentGraphs()
    unselected = [x for x in allmodels if x not in selected]

    for s in selected:
        om.setActive(s.id, True)
    for u in unselected:
        om.setActive(u.id, False)

def select_restofmol():
    selected = sl.currentGraphs()
    for m in selected:
        if type(m) == Molecule:
            chimera.selection.addCurrent(m)
