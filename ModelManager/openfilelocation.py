import chimera
from tymera.commonfunctions import current_selection

def nameofselection():
    cursel = current_selection('Gr',verbose=False,menu=False)
    model = cursel[0]
    return model.name

def find_model_file():
    model_name = nameofselection()
    directory = "C:\PROJECTS\\"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == model_name:
                file_path = os.path.join(root, file)
                return file_path
