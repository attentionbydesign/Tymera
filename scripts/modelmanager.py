from chimera import openModels, Molecule, runCommand
import os

while True:
    choice = input("(1) Open models, (2) Reassign model IDs, (3) Exit ")
    if choice == 1:
        runCommand("runscript C:/ProgramData/Chimera/GUI.py")
        
    elif choice == 2:
        runCommand("runscript C:/ProgramData/Chimera/reomdls-CLI.py")

    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Exiting program...")
        break

print("Program Ended")
