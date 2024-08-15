from chimera import runCommand as rc

ref=input("Reference model #: ")
mov=input("Moving model #: ")

refc=rc("measure center #"+str(ref))
movc=rc("measure center #"+str(mov))
    
from chimera import dialogs
print(dialogs.find('reply'))

