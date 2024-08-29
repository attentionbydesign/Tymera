import subprocess

# Function to input model number
def input_model_number():
    model_number = raw_input("Enter model number: ")
    return model_number

# Function to input atom specifier statement
def input_atom_spec(model_number):
    atom_spec = raw_input("Enter atom specifier statement for model {}: ".format(model_number))
    return "#{0}: {1}".format(model_number, atom_spec)

# Function to update model number
def update_model_number(current_model_number):
    print "Current model number:", current_model_number
    new_model_number = raw_input("Enter new model number: ")
    return new_model_number

# Function to update atom specifier statement
def update_atom_spec(current_atom_spec):
    print "Current atom specifier statement:", current_atom_spec
    choice = raw_input("Enter new atom specifier statement to update (or press Enter to keep it unchanged): ")
    if choice:
        if choice.startswith("~"):
            choice = choice[1:]
            atoms_to_remove = choice.split(",")
            for atom in atoms_to_remove:
                atom = atom.strip()
                if '-' in atom:
                    range_part, chain_part = atom.split('.')
                    start, end = range_part.split('-')
                    try:
                        start_range = int(start)
                        end_range = int(end)
                        current_atom_spec = ",".join([r for r in current_atom_spec.split(",") if not (int(r.split('-')[0].split('.')[0]) >= start_range and int(r.split('-')[1].split('.')[0]) <= end_range and r.split('-')[1].split('.')[1] == chain_part)])
                    except ValueError:
                        print("Invalid range format:", atom)
                        continue
                else:
                    current_atom_spec = current_atom_spec.replace(atom, "")
        else:
            current_atom_spec += ", " + choice
    return current_atom_spec


# Function to run commands on selected atoms
def run_commands_on_atoms(atom_spec):
    # Example commands to run on selected atoms
    commands = [
        "color red " + atom_spec,
        "show " + atom_spec
        # Add more commands as needed
    ]
    for command in commands:
        subprocess.run(["chimera", "--nogui", "--script", "-"], input=command, encoding='utf-8')

def main():
    current_model_number = input_model_number()
    current_atom_spec = input_atom_spec(current_model_number)
    while True:
        print "\n1. Update model number"
        print "2. Update atom specifier statement"
        print "3. Run commands on selected atoms"
        print "4. Exit"

        choice = raw_input("Enter your choice: ")

        if choice == '1':
            current_model_number = update_model_number(current_model_number)
            current_atom_spec = input_atom_spec(current_model_number)
        elif choice == '2':
            current_atom_spec = update_atom_spec(current_atom_spec)
        elif choice == '3':
            run_commands_on_atoms(current_atom_spec)
        elif choice == '4':
            break
        else:
            print "Invalid choice. Please enter a valid option."

if __name__ == "__main__":
    main()
