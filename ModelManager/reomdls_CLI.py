from chimera import openModels, Molecule, runCommand
import os

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
    
def reo_byname(models_dict):
    reo_dict={}
    idls = [mid for mid in models_dict]
    mdls = [models_dict[mid] for mid in models_dict]
    mdls.sort()
    for m in mdls:
        reo_dict[idls[mdls.index(m)]] = m
    return reo_dict
    

def find_model_file(old_id):
    model_name = models_dict.get(int(old_id))
    directory = "C:\PROJECTS\\"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == model_name:
                file_path = os.path.join(root, file)
                return file_path

def reassign_model_id(old_id, new_id):
    model_path = find_model_file(old_id)
    if model_path is None:
        print("File Not Found", "Model file corresponding to model ID {} not found.".format(old_id))
        return
    runCommand("~open #"+str(old_id))
    runCommand("open #"+str(new_id)+" "+model_path)

def reoIDbyName():

    # Sample dictionaries
    dict1 = list_models()
    dict2 = reo_byname(dict1)

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
        file_path=find_model_file(old_id)
        print("Model #"+old_id+" is located at: "+file_path)
        new_id=raw_input("Enter NEW ID#: ")
        if new_id == 'en':
            break
        reassign_model_id(old_id, new_id)
