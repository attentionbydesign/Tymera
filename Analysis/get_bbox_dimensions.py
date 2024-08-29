from chimera import openModels as om, runCommand as rc

#Creates & updates dictionary with (model ID : model object) pairs
###def update_mdict():
models = om.list()

mdl_IDs = []
for mdl in models:
    mdl_IDs.append(mdl.id)
    
mdict = {}
j = 0
for mID in mdl_IDs:
    mdict[mID] = models[j]
    j+=1


###
for mdl in models:
    print("#"+str(mdl.id)+" "+mdl.name)
print(" ")
mID = input("Enter model ID: ")


###def get_mdl_bbx(mID):   
mdl_obj = mdict[mID]
bbx = mdl_obj.bbox() #bbox method returns a tuple with boolean and bbox_object
success, bbx_obj = bbx
if success == True:
    ll = bbx_obj.llf    #coordinates of lower left corner in _chimera.Points object
    ur = bbx_obj.urb    #coordinates of upper right corner in _chimera.Points object
    vect = ur - ll      #dimensions of bounding box in _chimera.Vector object
    x,y,z = tuple(vect) #dimensions converted to a Python tuple object and unpacked into coordinate variables
    print(mdict[mID].name+" is bounded by a "+str(int(x))+" x "+str(int(y))+" x "+str(int(z))+" box.")
else:
    print("Unable to compute bounding box for "+mdict[mID].name)


###def update_chaindict(mID):
chains = mdict[mID].sequences()

chain_IDs = []
for chain in chains:
    chain_IDs.append(chain.chainID)
    
chaindict = {}
k = 0
for cID in chain_IDs:
    chaindict[cID] = chains[k]
    k+=1

###def get_chain_bbx(cID):
###def color_by_protein(mID):
import numpy as np
for cID in chaindict:
    chain_obj = chaindict[cID]
    atoms = [atom for residue in chain_obj.residues for atom in residue.atoms]
    coordinates = np.array([atom.coord().data() for atom in atoms])
    min_coords = coordinates.min(axis=0)
    max_coords = coordinates.max(axis=0)
    dimensions = max_coords - min_coords
    x,y,z=dimensions
    hwr = z / ((x + y) / 2)
    
    if 370 < len(chaindict[cID]) < 380:
        color = 'tan'
    elif 150 < len(chaindict[cID]) < 170 and hwr < 2.5:
        color = 'red'   #TnC
    elif 69 < len(chaindict[cID]) < 79 and hwr < 1:
        color = 'cyan'  #TnT
    elif 63 < len(chaindict[cID]) < 73 and hwr > 2.5:
        color = 'cyan'  #TnT1ext
    elif 121 < len(chaindict[cID]) < 131 and hwr < 2.5:
        color = 'blue'  #TnI
    elif len(chaindict[cID]) > 90 and hwr > 2.5:
        color = 'yellow'  #Tpm
    else:
        color = 'magenta'
        
    print cID, len(chaindict[cID]), dimensions, hwr, color

    rc('color '+color+' #'+str(mID)+': .'+str(cID))


def color_by_protein(mID):
    cc = {}
    for cID in chaindict:
        dim = get_chain_bbx(cID)
        x,y,z = dim
        hwr = z / ((x + y) / 2)
        print cID, len(chaindict[cID]), dim, hwr
        if 370 < len(chaindict[cID]) < 380:
            color = 'tan'
        elif 150 < len(chaindict[cID]) < 170 and hwr < 2.5:
            color = 'red'   #TnC
        elif 69 < len(chaindict[cID]) < 79 and hwr < 1:
            color = 'cyan'  #TnT
        elif 63 < len(chaindict[cID]) < 73 and hwr > 2.5:
            color = 'cyan'  #TnT1ext
        elif 121 < len(chaindict[cID]) < 131 and hwr < 2.5:
            color = 'blue'  #TnI
        elif len(chaindict[cID]) > 90 and hwr > 2.5:
            color = 'yellow'  #Tpm
        

