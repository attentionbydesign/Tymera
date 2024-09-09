import chimera, os
from chimera import openModels

tymera_path = os.path.dirname(os.path.dirname(__file__))

#---------------------------------------------------

def color_by_seq():
    from tymera.ColorBySeq.colorbyseq import color_by_seq
    color_by_seq()

#---------------------------------------------------

def active_select():
    from tymera.ModelManager.active_state import activate_selected
    activate_selected()

#---------------------------------------------------

def shoToggl():
    from tymera.ModelManager.display_toggler import show_toggle
    show_toggle()

#---------------------------------------------------

def vox_set():
    from chimera import openModels as om
    from VolumeViewer import volume

    vols = om.list(modelTypes=[volume.Volume])
    #v.name[len(v.name)-3:len(v.name)] will get you the file extension - if it's 'dat' then set the step_size?

    for v in vols:
        box_dim = v.data.size
        step_size = v.data.step
        x,y,z = box_dim
        if x == y == z:
            print("Volume #{} is a cube of {}px^3".format(v.id,x))
            
            sf = 396 / x
            vs = 1.356 * sf
            step = (vs,vs,vs)
            v.data.set_step(step)
            v.show()
        else:
            print("Volume #{} dimensions: {}px x {}px x {}px".format(v.id,x,y,z))
            ogs = v.data.original_step
            print("Original step: {}".format(ogs))
            v.data.set_step(ogs)
            v.show()

#---------------------------------------------------

def orientmdls():
    from tymera import OrientMdls
    OrientMdls.orient_all()

#---------------------------------------------------

def default_tbc():
    from chimera import openModels as om,runCommand as rc
    from VolumeViewer import volume
    vols = om.list(modelTypes=[volume.Volume])

    for v in vols:
        rc("volume #{} transparency 0.3 brightness 0.7".format(v.id))

#---------------------------------------------------
#Open selected molecule in default text editor
def openMolText():
    from tymera.ModelManager.openfilelocation import *
    open_mdlfile()

#Open the directory containing selected model in default file explorer
def openMdlDir():
    from tymera.ModelManager.openfilelocation import *
    open_mdldir()

#---------------------------------------------------
#---------------------------------------------------

def register_accelerators():

  from Accelerators import standard_accelerators
  standard_accelerators.register_accelerators()

  from Accelerators import add_accelerator
  add_accelerator('om','Orient models to global Y-axis and origin', orientmdls)
  add_accelerator('cb', 'Color chains of selected model by protein type', color_by_seq)
  add_accelerator('as', 'Activate only selected model', active_select)
  add_accelerator('sw', 'Toggle show only selected model / show all', shoToggl)
  add_accelerator('vx', 'Set voxelSize of all volumes based on box dimensions', vox_set)
  add_accelerator('vd', 'Custom volume display transparency and brightness', default_tbc)
  add_accelerator('of', 'Open file location of selected model', openMolText)
  add_accelerator('od', 'Open file location of selected model', openMdlDir)

register_accelerators()

