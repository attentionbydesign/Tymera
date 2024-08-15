import chimera
from chimera import runCommand as rc

mn=raw_input("Enter model number (w/o #): ")
rn=raw_input("Enter residue numbers: ")

asmn="#{}: ".format(mn)
aspec=asmn+rn

#display atoms for the given atom-spec
dsp_str="display {}".format(aspec)
dsp=rc(dsp_str)

#add residue labels in black for the given atom-spec
opt="labelopt resinfo %(1-letter code)s%(number)s"
rlss="rlabel {}".format(aspec)
clb="color black,rl {}".format(aspec)

rc(opt)
rc(rlss)
rc(clb)

