import chimera
from chimera import openModels, Molecule, runCommand
from tymera.commonfunctions import getKoD

def list_models(printls=False):
    # Get all open models
    models = openModels.list()
    # Create a dictionary with model IDs as keys and file names as regular strings
    models_dict = {m.id: str(m.name) for m in models}
    if printls == True:
        for mid in models_dict:
            print("{}\t{}".format(str(mid), models_dict[mid]))
    else:
        return models_dict
    
def sortbyname(models_dict):
    reo_dict={}
    idls = [mid for mid in models_dict]
    mdls = [models_dict[mid] for mid in models_dict]
    mdls.sort()
    for m in mdls:
        reo_dict[idls[mdls.index(m)]] = m
    return reo_dict

def get_reassignments():
    current_order = list_models()
    mdlnames = [current_order[mid] for mid in current_order]
    sorted_order = sortbyname(current_order)

    reassignments = []
    for mn in mdlnames:
        old_key = getKoD(current_order,mn) 
        new_key = getKoD(sorted_order,mn)
        if old_key != new_key:
            print("{} reassigned from #{} to #{}".format(mn, old_key, new_key))  
            reassignments.append((old_key,new_key))
    return reassignments

def reassignIDsByName():
    reassignments = get_reassignments()
    for old,new in reassignments:
        reassign_model_id(old,new)


def find_model_path(old_id):
    allmdls = chimera.openModels.list()
    mdlobj = [m for m in allmdls if m.id == old_id][0]
    return mdlobj.openedAs[0]

def reassign_model_id(old_id, new_id):
    model_path = find_model_path(old_id)
    if model_path is None:
        print("File Not Found", "Model file corresponding to model ID {} not found.".format(old_id))
        return
    runCommand("~open #"+str(old_id))
    runCommand("open #"+str(new_id)+" "+model_path)

def reoIDbyName():

    # Sample dictionaries
    dict1 = list_models()
    dict2 = sortbyname(dict1)

    # Step 1: Get the keys and values
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    values1 = list(dict1.values())
    values2 = list(dict2.values())

    # Step 2: Create a mapping from keys of dict1 to keys of dict2 based on values
    mapping = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 == value2:
                mapping[key1] = key2
                break

    # Step 3: Create a new dictionary with reassigned keys
    new_dict = {mapping[key]: dict1[key] for key in dict1}

    print("Reassigned Dictionary:", new_dict)
   

def changeModelID():
    while True:
        models_dict = list_models()
        old_id=raw_input("Enter CURRENT ID#: ")
        if old_id == 'en':
            break
        file_path=find_model_path(old_id)
        print("Model #"+old_id+" is located at: "+file_path)
        new_id=raw_input("Enter NEW ID#: ")
        if new_id == 'en':
            break
        reassign_model_id(old_id, new_id)
