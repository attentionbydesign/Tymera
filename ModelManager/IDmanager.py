from chimera import openModels, Molecule, runCommand
import os
from tymera.ModelManager import reomdls_CLI, GUI

def main():
    while True:
        choice = input("(1) Open models, (2) Reassign model IDs, (3) Exit ")
        if choice == 1:
            GUI.openFileDialog()
            
        elif choice == 2:
            reomdls_CLI.changeModelID()

        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Exiting program...")
            break

    print("Program Ended")

if __name__ == '__main__':
    main()
