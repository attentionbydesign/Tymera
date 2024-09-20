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





#------------------------------------------------------------------
# flip model across any cardinal axis of the global coordinates
# i.e., rotate 180 about a vector orthogonal to said axis
# USAGE
#   axis : string of x, y, or z

#returns global cardinal axis in chimera.Vector format for a given string input
def get_cardax(ax_str):
    if ax_str in ['x','y','z']:
        from chimera import Vector
        axes = {
            'x' : Vector(1,0,0),
            'y' : Vector(0,1,0),
            'z' : Vector(0,0,1)
        }
        axis = axes[ax_str]
        return axis
    else:
        print("ERROR: expected 'x', 'y', or 'z' (str) for axis argument.")

#flips model across specified cardinal axis entered as a lowercase single character string
def flip_mdl(mdl, ax_str):
    from chimera import Xform
    
    axrots = {
        'x' : get_cardax('y'),
        'y' : get_cardax('z'),
        'z' : get_cardax('x'),
    }
    
    rotax = axrots[ax_str]

    angle = 180
    mdos = mdl.openState
    mdos.globalXform(Xform.rotation(rotax,angle))

#flips selected model across specified axis
def flip_sel(ax_str):
    from tymera.commonfunctions import current_selection
    cursel = current_selection()
    for m in cursel:
        flip_mdl(m, ax_str)


    
