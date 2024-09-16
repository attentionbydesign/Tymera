## script for lining up similar models for comparison

""" 
e.g., 10 classes from 3D sorting

* option to toggle between superimposed/aligned
vs. line-up/spaced out views

* save state / global xforms of all models at any given
time, thereby allowing an easier option to undo movement

* keyboard shortcut to "Tools > Movement > Undo Move / Redo Move" 
"""
import chimera
from tymera.commonfunctions import current_selection

def save_current_positions():
    pass
#placeholder for now - will edit later, so you can revert back to original view

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True


def factor_pairs(apositiveint):
    factors = []
    for i in range(1, int(apositiveint**0.5)+1):
        if apositiveint % i == 0:
            factors.append((i, apositiveint / i))
    return factors


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def get_aveY(sel):
    yvals = []
    for v in sel:
        vox_size = v.data.step[1]  #assuming bbox is a cube
        bbdim = v.subregion()[1]
        x,z,y = bbdim
        ya = y * vox_size
        yvals.append(ya)
    aveY = sum(yvals) / len(yvals)
    return aveY

def get_aveXZ(sel):
    xzvals = []
    for v in sel:
        vox_size = v.data.step[1]  #assuming bbox is a cube
        bbdim = v.subregion()[1]
        x,z,y = bbdim
        xa = x * vox_size
        za = z * vox_size
        xzvals.append(xa)
        xzvals.append(za)
    aveXZ = sum(xzvals) / len(xzvals)
    return aveXZ

def lineup_models():
    import chimera
    from chimera import Xform, runCommand as rc

    cursel = current_selection()
    n = len(cursel)
    ave_y = get_aveY(cursel)
    ave_xz = get_aveXZ(cursel)

    if n < 7:
       #Single row
       j = -1
       for m in cursel:
           j += 1
           side_step = ave_xz * j
           mos = m.openState
           mos.globalXform(Xform.translation(side_step,0,0))
    elif is_square(n):
       import math
       sidelen = int(math.sqrt(n))
    elif is_prime(n) == False:
       from chimera import Vector,Xform
       dim_pairs = factor_pairs(n)
       sqrapprox = dim_pairs[len(dim_pairs)-1]
       xl,yl = sqrapprox
       target_coords = []
       for y in range(yl):
           for x in range(xl):
               target_coords.append((x,y))
       for m in cursel:
           idx = cursel.index(m)
           tc = target_coords[idx]
           nx,ny = tc

           spacer = 1.25    #adjust as needed

           tx = -spacer * nx * ave_xz
           ty = -spacer * ny * ave_y
           tlv = Vector(tx,ty,0)
           mos = m.openState
           mos.globalXform(Xform.translation(tlv))

    rc("cofr independent")

           
           

    # wi_h = ave_y * nrows
    # wi_w = ave_xz * ncols
    # chimera.viewer.windowSize = (wi_w, wi_h)
    