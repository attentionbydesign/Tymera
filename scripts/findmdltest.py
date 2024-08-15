from chimera import openModels, Molecule, runCommand
import os

def list_models():
    # Get all open models
    models = openModels.list(modelTypes=[Molecule])
    # Create a dictionary with model IDs as keys and file names as regular strings
    models_dict = {m.id: str(m.name) for m in models}
    return models_dict

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
        messagebox.showerror("File Not Found", "Model file corresponding to model ID {} not found.".format(old_id))
        return
    runCommand("~open #"+str(old_id))
    runCommand("open #"+str(new_id)+" "+model_path)

while True:
    models_dict = list_models()
    old_id=str(input("Enter current ID#: "))
    #file_path=find_model_file(old_id)
    #print("Model #"+old_id+" is located at: "+file_path)
    new_id=str(input("Enter NEW ID#: "))
    reassign_model_id(old_id, new_id)






