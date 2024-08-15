mdls = chimera.selection.currentGraphs()
mdl = mdls[0]
coords = numpyArrayFromAtoms(mol.atoms, xformed=True)
from StructMeasure import bestLine
centroidPt, majorVec, centroidArray, majorArray, centered, vals, vecs = \
                bestLine(coords)
print centroidPt
