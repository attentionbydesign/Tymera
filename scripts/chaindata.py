from chimera import openModels, Molecule

while True:
    # Load your model (assuming the model is already loaded in Chimera)
    models = openModels.list()
    mID = input("Model ID#: ")
    model = models[int(mID)]

    # Specify the chain you want to analyze
    chain_id = raw_input("Chain ID: ")

    # Find the chain in the model
    chain = None
    for chain_obj in model.sequences():
        if chain_obj.chainID == chain_id:
            chain = chain_obj
            
    if chain is None:
        print("Chain "+str(chain_id)+" not found in model.")
    else:
        # Create a list to store secondary structure summary
        ss_summary = []

        current_ss_type = None
        current_ss_count = 0

        for residue in chain.residues:
            if residue.isHelix:
                ss_type = 'helix'
            elif residue.isStrand:
                ss_type = 'strand'
            else:
                ss_type = 'coil'
            
            if ss_type == current_ss_type:
                current_ss_count += 1
            else:
                if current_ss_type is not None:
                    ss_summary.append((current_ss_type, current_ss_count))
                current_ss_type = ss_type
                current_ss_count = 1
        
        # Append the last secondary structure
        if current_ss_type is not None:
            ss_summary.append((current_ss_type, current_ss_count))

        # Print the secondary structure summary
        print("N-terminus")
        helix_count = 1
        strand_count = 1
        coil_count = 1
        for ss_type, count in ss_summary:
            if ss_type == 'helix':
                print("Helix "+str(helix_count)+": "+str(count)+" residues")
                helix_count += 1
            elif ss_type == 'strand':
                print("Strand "+str(strand_count)+": "+str(count)+" residues")
                strand_count += 1
            else:
                print("Coil "+str(coil_count)+": "+str(count)+" residues")
                coil_count += 1
        print("C-terminus")
