from chimera import openModels as om, runCommand as rc, Molecule
from VolumeViewer import volume

mdls=[]
mdls=om.list()
mols = om.list(modelTypes=[Molecule])
vols = om.list(modelTypes=[volume.Volume])


def rng():
    import random
    return int(100 * (round(random.random(),2)))

def xl2cofr():
    rc('cofr view')
    for m in mdls:
        rc('move cofr models #{}'.format(m.id))
    rc('cofr models')



def globfit(m_id):

    v = vols[0]
    m = mdls[m_id]

    #rc('fitmap #{} #{} search 1 clusterAngle 1'.format(m.id,v.id))
    rc('fitmap #{}:@CA #{} listFits true gridStepMax 1 search 15 clusterAngle 1 inside 0.6 moveWholeMolecules  true'.format(m.id,v.id))

def scramble(m_id):
    axes = ['x','y','z']
    for ax in axes:
        rc('move {} {} models #{}'.format(ax,rng(),m_id))
        rc('turn {} {} models #{}'.format(ax,rng(),m_id))

def voltrans():
    for v in vols:
        rc('transparency 40 #{}'.format(str(v.id)))
        


scramble(1)

raw_input('Hit ENTER to continue')
xl2cofr()
raw_input('Hit ENTER to continue')
globfit(1)
