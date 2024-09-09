###Opens location of selected model's file in OS's default file explorer


import chimera, tymera, os, platform, subprocess
from tymera.commonfunctions import current_selection
tymera_path = os.path.dirname(tymera.__file__)

##def setRoot():
##    from Tkinter import *
##    import tkFileDialog as filedialog
##    default = os.path.dirname(chimera.__file__)
##    filepath = filedialog.askopenfilename(initialdir = default,
##                                          title = "Select Root Path")
##    return filepath

def find_model_path(filepath=False):
    model = current_selection()[0]
    file_path = model.openedAs[0]
    dir_path_raw = str(os.path.dirname(file_path))
    dir_path = dir_path_raw.replace('\\','/')
    
    if os.path.exists(dir_path) == False:
        searchpattern = os.path.basename(dir_path)
        dirls = os.listdir(os.path.dirname(dir_path))
        matchls = [ name for name in dirls if searchpattern in name ]
        truname = matchls[0]
        dir_path = dir_path.replace(searchpattern,truname)
    #print('{} is located at: {}'.format(model.name,dir_path))

    if filepath == True :
        return str('{}/{}'.format(dir_path, model.name))
    else:
        return str(dir_path)

def open_directory(directory_path):
    # Normalize the path for the current OS
    if platform.system() == 'Windows':
        # For Windows
        subprocess.call(['explorer', os.path.abspath(directory_path)])
    elif platform.system() == 'Darwin':
        # For macOS
        subprocess.call(['open', os.path.abspath(directory_path)])
    elif platform.system() == 'Linux':
        # For Linux
        try:
            # Try common file managers in order
            subprocess.call(['nautilus', os.path.abspath(directory_path)])
        except FileNotFoundError:
            try:
                subprocess.call(['dolphin', os.path.abspath(directory_path)])
            except FileNotFoundError:
                try:
                    subprocess.call(['thunar', os.path.abspath(directory_path)])
                except FileNotFoundError:
                    # Fallback to xdg-open
                    subprocess.call(['xdg-open', os.path.abspath(directory_path)])
    else:
        raise OSError('Unsupported operating system')
    
def open_file(file_path):
    # Normalize the path for the current OS
    abs_path = os.path.abspath(file_path)
    
    if platform.system() == 'Windows':
        # For Windows
        os.startfile(abs_path)
    elif platform.system() == 'Darwin':
        # For macOS
        subprocess.call(['open', abs_path])
    elif platform.system() == 'Linux':
        # For Linux
        try:
            # Try common text editors in order
            subprocess.call(['xdg-open', abs_path])
        except FileNotFoundError:
            raise OSError('No suitable file opener found for Linux')
    else:
        raise OSError('Unsupported operating system')


def open_mdldir():
    mdir_path = find_model_path(False)
    open_directory(mdir_path)

def open_mdlfile():
    mfile_path = find_model_path(True)
    open_file(mfile_path)

if __name__ == '__main__':
    open_mdldir()

