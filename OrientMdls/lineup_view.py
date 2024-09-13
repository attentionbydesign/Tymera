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
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, value / i))
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
        bbdim = v.subregion()[1]
        x,z,y = bbdim
        yvals.append(y)
    aveY = sum(yvals) / len(yvals)
    return aveY

def get_aveXZ(sel):
    xzvals = []
    for v in sel:
        bbdim = v.subregion()[1]
        x,z,y = bbdim
        xzvals.append(x)
        xzvals.append(z)
    aveXZ = sum(xzvals) / len(xzvals)
    return aveXZ

def lineup_models():
    import chimera
    from chimera import Xform
    
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
       dim_pairs = factor_pairs(n)
       for pair in dim_pairs:
           s1,s2=pair
           print(
               "{} x {}".format(s1,s2),
               "{} x {}".format(s2,s1)
           )

    # wi_h = ave_y * nrows
    # wi_w = ave_xz * ncols
    # chimera.viewer.windowSize = (wi_w, wi_h)
    