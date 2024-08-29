# Broad translational alignment probably moot point now that 
# orient_mols works, but general idea of a broad rotational 
# alignment prior to running fitmap potentially has merit


from chimera import runCommand as rc

ref=input("Reference model #: ")
mov=input("Moving model #: ")

refc=rc("measure center #"+str(ref))
movc=rc("measure center #"+str(mov))
    
from chimera import dialogs
print(dialogs.find('reply'))

