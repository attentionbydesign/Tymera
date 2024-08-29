import chimera
from chimera import runCommand as rc, openModels as om


mdls = om.list()
j=0
for m in mdls:
    if m.name == '5jmy':
        j+=1

if j == 0:
    rc('open 5jmy')

mdls = om.list()
for m in mdls:
    if m.name == '5jmy':
        mid = m.id

        commands = [
            'delete #{} & solvent'.format(mid),
            'color byelement #{} & ~main'.format(mid),
            'represent sphere #{} & ions'.format(mid),
            'represent bs #{} & ligand & ~ions'.format(mid),
            'color byhet #{}:807'.format(mid),
            'color dim gray #{}:807 & C'.format(mid),
            'label offset 0,0,0 #{} & ions'.format(mid),
            'labelopt info %(element)s',
            'color green,al #{} & ions'.format(mid),
            'color tan #{}:.A & main'.format(mid),
            'color sienna #{}:.B & main'.format(mid),
            'color byhet #{} & main'.format(mid),
            'aromatic circle #{} & ligand'.format(mid),
            'transparency 50,r #{} & main'.format(mid),
            ]

        rc('; '.join(commands))
      
