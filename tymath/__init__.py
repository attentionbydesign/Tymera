# custom math functions

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

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

def factor_pairs(apositiveint):
    factors = []
    for i in range(1, int(apositiveint**0.5)+1):
        if apositiveint % i == 0:
            factors.append((i, apositiveint / i))
    return factors