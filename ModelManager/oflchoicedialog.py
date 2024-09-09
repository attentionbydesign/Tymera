import Tkinter as tk
import tkFileDialog as filedialog
import tkMessageBox as messagebox
import subprocess
import os

def open_file(file_path):
    """Open the file with the default application."""
    if os.name == 'nt':  # For Windows
        os.startfile(file_path)
    elif os.name == 'posix':  # For Unix-based systems
        subprocess.call(['xdg-open', file_path])

def open_file_location(file_path):
    """Open the file location in the file explorer."""
    directory = os.path.dirname(file_path)
    if os.name == 'nt':  # For Windows
        subprocess.call(['explorer', '/select,', file_path])
    elif os.name == 'posix':  # For Unix-based systems
        subprocess.call(['xdg-open', directory])

def choose_action(file_path):
    """Show a dialog asking the user what they want to do."""
    def on_open_file():
        open_file(file_path)
        root.quit()

    def on_open_location():
        open_file_location(file_path)
        root.quit()

    root = tk.Tk()
    root.withdraw()  # Hide the root window

    response = messagebox.askquestion(
        "Choose Action",
        "Do you want to open the file or open its location?",
        icon='question',
        type=messagebox.YESNO
    )

    if response == 'yes':
        on_open_file()
    else:
        on_open_location()

def main():
    # Open file dialog to choose a file
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*")]
    )

    if file_path:
        choose_action(file_path)
    else:
        print "No file selected."

if __name__ == "__main__":
    main()
