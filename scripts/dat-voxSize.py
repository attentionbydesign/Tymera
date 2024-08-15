import chimera
from chimera import openModels as om
from VolumeViewer import volume

vols = om.list(modelTypes=[volume.Volume])
#v.name[len(v.name)-3:len(v.name)] will get you the file extension - if it's 'dat' then set the step_size?

for v in vols:
    box_dim = v.data.size
    step_size = v.data.step

    print box_dim
    print round(step_size[0],5)

    x=box_dim[0]

    sf = 396 / x

    vs = 1.356 * sf

    step = (vs,vs,vs)
    v.data.set_step(step)
    v.show()





