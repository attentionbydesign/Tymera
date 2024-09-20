# # ###ID_Manager

# # # (Model ID) MID_manager: change ID #'s of models
# # # currently open in ModelPanel.

# #     - if a .brix file is detected, automatically assign
# # it #0.  If a different model currently occupies #0, switch places (i.e., avoid closing it)


# # (Chain ID) CID_manager: 
# #   -uses sequence identification to label
# the chains of a model, to help you identify which chains
# you want to change the ID of. 

#     - reorders the listed order of chains
# as reflected in the PDB file, so that a hierarchy
# is maintained
#         1. Sequence Similarity (i.e., Tn's, Tpm's, Actin)
#         2. Within sequence groups, go from top to bottom
# in the Y-axis position of the chain's centroid?


import CID_manager,MID_manager,pdbclean

""" Chimera's StructMeasure.bestLine(coords) method takes a set of atomic coordinates in the form of a numpy array and calculates a variety of measurements and returns them in a list in the following order:

    1. Centroid Point - coordinate location of the centroid, expressed as a chimera.Point object
    2. Major Vector - the magnitude and direction of the largest of three cardinal axes calculated from the coordinates (see 6 and 7), expressed as a float and chimera.Vector object, respectively.
    3. Centroid Array
    4. Major Array
    5. Centered
    6. Values - the magnitudes of the three cardinal axes
    7. Vectors -  the unit vectors parallel to said axes

"""

#BLquery() returns one of the above seven measurements if specified as a string.  If not specified, you get a printout of the possible strings you could pass as arguments. 
def BLquery(mol,optstr=None):
    import chimera
    from StructMeasure import bestLine
    coords = chimera.numpyArrayFromAtoms(mol.atoms, xformed=True)
    centroidPt, majorVec, centroidArray, majorArray, centered, vals, vecs = \
                    bestLine(coords)
    
    options = {
        "centroidPt": centroidPt,
        "majorVec": majorVec,
        "centroidArray": centroidArray,
        "majorArray": majorArray,
        "centered": centered,
        "vals": vals,
        "vecs": vecs
    }
    
    if optstr in options:
         return options[optstr]
    else:
        print("Enter any of the following options for 'opt=' argument:\n")
        for o in options:
            print o

#bestAxes() prints out the three cardinal axes calculated by bestLine, along with which global axes each is most closely alined with at the moment
def bestAxes(mol,listvecs=False):
    from chimera import Vector
    import numpy as np

    vals = BLquery(mol,'vals')
    vecs = BLquery(mol,'vecs')
    sv = zip(vals,vecs)
    sv.sort()
    sv.reverse()

    if listvecs == True:
        for i in range(len(sv)):
            print("Vector #{}".format(i))
            mag = sv[i][0]
            uv = sv[i][1]
            uv_rt = tuple(round(n,4) for n in uv)
            print("Magnitude: {}\nUnit Vector: {}".format(mag,uv_rt))
            axd = {0:'x',1:'y',2:'z'}
            axis = axd[np.argmax(abs(sv[i][1]))]
            print("This is most aligned with the global {}-axis.\n".format(axis.upper()))
    else:
        axl = sv[0][1]
        axv = Vector(axl[0],axl[1],axl[2])
        return axv


