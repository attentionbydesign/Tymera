def mol_select():
    mol_objs = chimera.openModels.list()
    for mobj in mol_objs:
        print "#"+str(mobj.id), mobj.name
    mid = input("Model ID#: ")
    for mobj in mol_objs:
        if mobj.id == mid:
            mobj_sel = mobj
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