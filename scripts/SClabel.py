import chimera
from chimera import runCommand as rc

import msvcrt

mn=raw_input("Enter model number (w/o #): ")


while True:
    if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key == '\x1b':
                    print("Exiting...")
                    break
    rn=raw_input("Enter residue numbers: ")

    asmn="#{}: ".format(mn)
    aspec=asmn+rn

    #display atoms for the given atom-spec
    dsp_str="display {}".format(aspec)
    dsp=rc(dsp_str)

    #add residue labels in black for the given atom-spec
    rlopt_str="labelopt resinfo %(1-letter code)s%(number)s" #set custom format
    rl_str="rlabel {}".format(aspec) #add residue label for given atom-spec
    clb_str="color black,rl {}".format(aspec) #set residue label color to black

    rlopt=rc(rlopt_str)
    rl=rc(rl_str)
    clb=rc(clb_str)

    dsp; rlopt; rl; clb

    
