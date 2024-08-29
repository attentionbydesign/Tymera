#Display ONLY SELECTED models:
def show_selected():
    from chimera import runCommand as rc, openModels as om, selection
    allmodels = om.list()
    selected = selection.currentGraphs()
    unselected = [x for x in allmodels if x not in selected]

    for s in selected:
        rc("modeldisplay #"+str(s.id))
    for u in unselected:
        rc("~modeldisplay #"+str(u.id))

#Display ALL models:
def show_all():
    from chimera import runCommand as rc, openModels as om
    allmodels = om.list()
    for model in allmodels:
        mid = model.id
        rc("modeldisplay #"+str(mid))

#Returns list of all currently displayed models
def get_displayed():
    from chimera import openModels as om
    shown = []
    allmodels = om.list()
    for m in allmodels:
        state = m.display
        print m.id, state
        if state == True:
            shown.append(m)
    return shown

#Toggles between showing ALL vs. ONLY SELECTED models:
def show_toggle():
    from chimera import openModels as om
    allmodels = om.list()
    displayed = get_displayed()
    if len(displayed) == len(allmodels):
        show_selected()
    else:
        show_all()