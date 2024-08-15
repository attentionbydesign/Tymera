from chimera import openModels, Molecule
import Tkinter as tk
import tkSimpleDialog as simpledialog
import tkMessageBox as messagebox
from chimera import runCommand
import os


# Function to list models and create a dictionary with regular strings
def list_models():
    # Get all open models
    models = openModels.list(modelTypes=[Molecule])
    # Create a dictionary with model IDs as keys and file names as regular strings
    models_dict = {m.id: str(m.name) for m in models}
    return models_dict

#Function to get the path to the file corresponding with a given model name
def find_model_file(old_id):
    model_name = models_dict.get(int(old_id))
    directory = "C:\PROJECTS\\"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == model_name:
                return os.path.join(root, file)
                 
# Function to re-assign model ID
def reassign_model_id(old_id, new_id, model_path):
    if model_path is None:
        messagebox.showerror("File Not Found", "Model file corresponding to model ID {} not found.".format(old_id))
        return
    runCommand("~open #"+str(old_id))
    runCommand("open #"+str(new_id)+" "+model_path)
    
# Function to create GUI dialog
def create_gui():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    models_dict = list_models()
    models = sorted(models_dict.items())  # Sort models by ID

    if not models:
        messagebox.showinfo("No Models", "There are no open models to reassign.")
        return

    # Show the list of models and get the selected model ID
    model_ids = [str(model[0]) for model in models]
    old_id = simpledialog.askstring("Select Model", "Enter the Model ID to reassign:", initialvalue=model_ids[0])

    if old_id is None:
        return

    # Validate old ID
    old_id = int(old_id)
    if old_id not in models_dict:
        messagebox.showerror("Invalid Model ID", "The selected Model ID does not exist.")
        return

    # Get the new model ID
    new_id = simpledialog.askstring("New Model ID", "Enter the new Model ID for model #{} ({}):".format(old_id, models_dict[old_id]))

    if new_id is None:
        return

    # Validate new ID
    try:
        new_id = int(new_id)
    except ValueError:
        messagebox.showerror("Invalid Model ID", "The new Model ID must be an integer.")
        return

    # Re-assign the model ID
    model_path = find_model_file(old_id)
    reassign_model_id(old_id, new_id, model_path)
    messagebox.showinfo("Success", "Model ID reassigned from #{} to #{}.".format(old_id, new_id))

# Create the GUI
create_gui()


