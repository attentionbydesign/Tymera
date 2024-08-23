import orient_mols,orient_vols

def orient_all():
    from chimera import runCommand as rc
    rc('run orient_vols.py')
    rc('run orient_mols.py')