from chimera import openModels, Molecule

# Function to list models and create a dictionary with regular strings
def list_models():
    # Get all open models
    models = openModels.list(modelTypes=[Molecule])
    # Create a dictionary with model IDs as keys and file names as regular strings
    models_dict = {m.id: str(m.name) for m in models}
    return models_dict

# Get the dictionary of models
models_dict = list_models()

# Print the dictionary of models
print "Models Dictionary:"
print models_dict
