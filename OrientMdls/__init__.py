import orient_mols,orient_vols, chimera

def orient_all():
    orient_mols.run_om()
    orient_vols.run_ov()
    chimera.viewer.viewAll(resetCofrMethod=False) #equivalent to standard accelerator 'va'

# NOTE: 'viewer' is not a module of chimera, it is actually
# an variable name for which a C++ chimera environment class
# (LensViewer or NoGuiViewer) is instantiated in the __init__.py 
# of the chimera package.  For Example:

#     from _chimera import LensViewer
#     viewer = LensViewer()   #the parentheses means an instance of the LensViewer class is created, and assigned to the 'viewer' variable.

# So 'viewer' is essentially undefined unless you import chimera itself
# so that __init__.py will be run.  This is why 

#     from chimera.viewer import viewAll 

# does not work, because viewAll() is likely a method of one of the
# classes that would have been assigned to 'viewer', but neither
# were assigned yet.