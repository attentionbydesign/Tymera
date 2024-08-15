from chimera import openModels, Molecule
import numpy as np

def list_model_chains():
    # Get all open molecule models
    models = openModels.list()#(modelTypes=[Molecule])
    
    # Iterate over each model
    for model in models:
        print("Model ID:", model.id)
        print("Model Name:", model.name)
        
        # Iterate over each chain in the model
        for chain in model.sequences():
            print("  Chain ID:", chain.chainID)
            print("  Chain Length:", len(chain))

# Call the function to list chains in all open models
#list_model_chains()

def list_model_chain_bounding_boxes():
    # Get all open molecule models
    models = openModels.list()
    
    #for model in models[5]:
        #print("Model ID:", model.id)
        #print("Model Name:", model.name)
        
    for chain in models[5].sequences():
        chain_id = chain.chainID
        #print("  Chain ID:", chain_id)
        
        # Get all atoms in the chain
        atoms = [atom for residue in chain.residues for atom in residue.atoms]
        
        if not atoms:
            print("  No atoms found in chain")
            continue
        
        # Extract coordinates of all atoms in the chain
        coords = np.array([atom.coord().data() for atom in atoms])
        
        # Calculate bounding box
        min_coords = coords.min(axis=0)
        max_coords = coords.max(axis=0)
        
        # Dimensions of the bounding box
        dimensions = max_coords - min_coords
        
        #print("    Bounding Box Min Coordinates:", min_coords)
        #print("    Bounding Box Max Coordinates:", max_coords)
        #print("    Bounding Box Dimensions (X, Y, Z):", dimensions)

        x,y,z=dimensions

        print "#",model.id, chain_id,(x,y,z)

    # Initialize variables to track the current secondary structure and its length
        current_structure = None
        current_length = 0
        structure_summary = []
        
        # Iterate over each residue in the chain
        for residue in chain.residues:
            if residue.isHelix:
                sec_structure = "Helix"
            elif residue.isStrand:
                sec_structure = "Strand"
            else:
                sec_structure = "Coil"
            
            if sec_structure == current_structure:
                current_length += 1
            else:
                if current_structure is not None:
                    structure_summary.append((current_structure, current_length))
                current_structure = sec_structure
                current_length = 1
        
        # Append the last structure segment
        if current_structure is not None:
            structure_summary.append((current_structure, current_length))
        
        # Print the summary
        for structure, length in structure_summary:
            print structure, length


# Call the function to list chains and their bounding boxes in all open models
list_model_chain_bounding_boxes()
