def delta(L):
    delta = []
    n = len(L)
    for k in range(n-1):
        d = L[k]-L[k+1]
        d = L[k+1]-L[k]
        delta.append(d)
    return delta


def minimum(L):
    min=L[0]
    for i in L:
        if min>= i:
            min = i
    return min

def maximum(L):
    max = L[0]
    for i in L:
        if max<= i:
            max = i
    return max

def moyenne(L):
    s = 0
    n = len(L)
    for k in range(n):
        s = s + L[k]
    return s/n

def variance(L):
    moy = moyenne(L)
    var= 0
    n = len(L)
    for k in range(n):
        var = var + (L[k]-moy)**2
    return np.sqrt(var/n)