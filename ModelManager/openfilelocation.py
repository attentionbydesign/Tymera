###Opens location of selected model's file in OS's default file explorer


import chimera, tymera, os, platform, subprocess
from tymera.commonfunctions import current_selection
tymera_path = os.path.dirname(tymera.__file__)

def nameofselection():
    cursel = current_selection('Gr',verbose=False,menu=False)
    model = cursel[0]
    return model.name

##def setRoot():
##    from Tkinter import *
##    import tkFileDialog as filedialog
##    default = os.path.dirname(chimera.__file__)
##    filepath = filedialog.askopenfilename(initialdir = default,
##                                          title = "Select Root Path")
##    return filepath

def find_model_file():
    model_name = nameofselection()
    directory = "/"
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == model_name:
                file_path = os.path.join(root, file)
                return file_path

#rootpath = os.path.dirname(setRoot())

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

def openfilepath():
    file_location = os.path.dirname(find_model_file())
    open_directory(file_location)

if __name__ == '__main__':
    openfilepath()

