from chimera import runCommand, openModels, Molecule

# Function to extract sequence from a chain
def extract_sequence(chain):
    sequence = ""
    for residue in chain.residues:
        sequence += residue.type
    return sequence

# Function to get secondary structure summary
def secondary_structure_summary(chain):
    structure_counts = {"Helix": 0, "Strand": 0, "Coil": 0}
    current_structure = None
    current_length = 0
    summary = []

    for residue in chain.residues:
        ss_type = residue.isHelix or residue.isStrand or 'C'  # Check secondary structure type
        if ss_type == 'H':  # Helix
            ss_type = "Helix"
        elif ss_type == 'S':  # Strand
            ss_type = "Strand"
        else:
            ss_type = "Coil"

        if ss_type == current_structure:
            current_length += 1
        else:
            if current_structure:
                structure_counts[current_structure] += current_length
                summary.append((current_structure, current_length))
            current_structure = ss_type
            current_length = 1

    if current_structure:
        structure_counts[current_structure] += current_length
        summary.append((current_structure, current_length))

    return summary

# List all molecules (models) in the session
models = openModels.list

# Display a list of open models and their chain IDs
print "Open Models:"
for model in models:
    print "Model ID:", model.id
    for chain in model.chains:
        print "\tChain ID:", chain.id

# Input model ID and chain ID
model_id = raw_input("Enter Model ID: ")
chain_id = raw_input("Enter Chain ID: ")

# Find the specified model and chain
model = next((m for m in models if m.id == int(model_id)), None)
chain = next((c for c in model.chains if c.id == chain_id), None)

if not chain:
    print "Chain not found."
    exit()

# Extract sequence and secondary structure summary
sequence = extract_sequence(chain)
summary = secondary_structure_summary(chain)

# Print the results
print "\nChain:", chain_id
print "Sequence:", sequence
print "Secondary Structure Summary:"
for structure, length in summary:
    print "{0}: {1} residues".format(structure, length)
