from chimera import runCommand as rc

first=input("First model #: ")
last=input("Last model #: ")+1
bs=float(input("Box Size (px): "))
scale=float(input("Scale (A/px): "))
bsA=bs*scale   #box size in angstroms

rc("reset")
j=0

for i in range(first,last):
    current_mdl=str(i)
    rc("~select 0-999; select "+current_mdl)
    j+=1
    mvincr=str(j*bsA/2.5)   #EDIT DENOMINATOR PRN
    mvcmd="move x "+mvincr
    rc(mvcmd)
    print("Model #: "+current_mdl)
    print(j)

rc("select all; center #"+str(first)+"-#"+str(last)+"; focus #"+str(first)+"-#"+str(last)+"; turn x -90")
    

