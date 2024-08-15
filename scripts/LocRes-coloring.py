from chimera import runCommand as rc

l=raw_input("Model# for Local Resolution Map: ")            
p=raw_input("Model# for Postprocessing Map: ")

# Matrixcopy to align (do NOT use fitmap)
mc="matrixcopy #"+p+" #"+l
rc(mc)

# Define 15 colors
colors = [
    "#861800000000",
    "#ffff00000000",
    "#ffff6db60000",
    "#ffffb6db0000",
    "#ffffffff0000",
    "#c30bf3ce0000",
    "#9e79c30b0000",
    "#00009e790000",
    "#0000ffff8618",
    "#0000ffffffff",
    "#00008618ffff",
    "#00000000ffff",
    "#86180000ffff",
    "#ffff0000ffff",
    "#ffff8618ffff"
]

a=input("Minimum value: ")
b=input("Maximum value: ")
r=b-a

val_spec=""
val_prefix = "scolor #"+str(p)+" volume #"+str(l)+" cmap"
for i in range(15):
    val_spec += " "+str(round((float(i)/float(14)),3))+","+colors[i]
val_cmd=val_prefix+val_spec+" cmapRange full"
print(val_cmd)

print('\n')

key_spec=""
key_prefix = "colorkey 0.85,0.95 0.90,0.30"
for i in range(15):
    key_spec += " "+str(round((float(i)/float(14))*r+a,3))+" "+colors[i]
key_cmd=key_prefix+key_spec
print(key_cmd)

