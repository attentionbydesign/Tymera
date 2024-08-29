import chimera
from chimera import runCommand as rc, openModels as om

def demo():
    rc("open 3j8i")
    mdls = om.list()
    cid = 'D'
    for mol in mdls:
        if mol.name == '3j8i':
            mn = str(mol.id)
        nD = '#{} & ~#{}:.D'.format(mn,mn)
        rc("~ribbon {}; ~display {}".format(nD,nD))

        commands = [
            'color forest green #{}:1-33.{},71-145.{},337-375.{}'.format(mn,cid,cid,cid), #domain 1
            'color magenta #{}:34-70.{}'.format(mn,cid),	#domain 2
            'color yellow #{}:146-179.{},273-336.{}'.format(mn,cid,cid),	#domain 3
            'color cyan #{}:180-272.{}'.format(mn,cid), #domain 4
            'color byhet #{}:.{}'.format(mn,cid), #color by heteroatom, leaving carbon alone
            ]

        for c in commands:
            rc(c+" & protein")
            
        rc('color byelement #{}:.{} & ~protein'.format(mn,cid)) #color ligands/ions by element

if __name__ == '__main__':
    demo()
    