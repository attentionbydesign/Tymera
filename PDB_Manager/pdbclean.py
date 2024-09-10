import chimera
from tymera.ModelManager.openfilelocation import *

#NOTE: this overwrites the original file
def remove_lines_with_pattern(file_path, pattern):
    # Read the file and filter out lines containing the pattern
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter lines that do not contain the pattern
    filtered_lines = [line for line in lines if pattern not in line]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)

def init_cleancopy(specpath=False):
    input_file_path = find_model_path(True)
    base, ext = os.path.splitext(input_file_path)
    output_file_path = "{}-CLEAN{}".format(base,ext)

    #Read lines from original
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    #Write original lines into cleancopy (i.e., copy the lines over)
    with open(output_file_path, 'w') as file:
        file.writelines(lines)
        
    return output_file_path

##def remove_lines_with_pattern(input_file_path, pattern):
##    # Create the new file path with "-cleaned" suffix
##    base, ext = os.path.splitext(input_file_path)
##    output_file_path = f"{base}-cleaned{ext}"
##
##    # Read the file and filter out lines containing the pattern
##    with open(input_file_path, 'r') as file:
##        lines = file.readlines()
##
##    # Filter lines that do not contain the pattern
##    filtered_lines = [line for line in lines if pattern not in line]
##
##    # Write the filtered lines to the new file
##    with open(output_file_path, 'w') as file:
##        file.writelines(filtered_lines)
##
##    print(f"Processed file saved as: {output_file_path}")

def rm_badlines(specpath=False):

    cleancopy_path = init_cleancopy()

    filterout=[
        'HELIX',
        'SHEET',
        'ENDMDL',
        'MDL',
        'MODEL',
        'CONECT',
        'REMARK',
        'DBREF',
        'SEQRES'
    ]

    for pattern in filterout:
        remove_lines_with_pattern(cleancopy_path, pattern)

    chimera.openModels.open(cleancopy_path)

if __name__ == '__main__':
    rm_badlines()

    
