import chimera
from chimera import runCommand as rc

selected_chain_info = []

def get_selected_chain_info():
    selected_atoms = chimera.selection.currentAtoms()
    if not selected_atoms:
        print("No atoms selected.")
        return
    model_id = selected_atoms[0].molecule.id
    residue = selected_atoms[0].residue
    res_id = residue.id
    chain_id = str(res_id)[-1]
    selected_chain_info.append((model_id, chain_id))

def selection_callback(trigger, data):
    get_selected_chain_info()

chimera.triggers.addHandler('selection changed', selection_callback)

# To stop the loop and print the selected chain info
# Call the following line when you're done selecting
# chimera.triggers.deleteHandler('selection changed', selection_callback)


rc("select #"+str(model_id)+":."+chain_id)
