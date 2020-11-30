def correlation(a,b): #a, b deux listes
    num=0    
    somme_den1=0
    somme_den2=0
    xa=moyenne(a)
    yb=moyenne(b)
    for i in range(len(a)): 
        num=num+((a[i]-xa)*(b[i]-yb))
        somme_den1=somme_den1+((a[i]-xa)**2)
        somme_den2=somme_den2+((b[i]-yb)**2)
    den=(sqrt(somme_den1))*(sqrt(somme_den2))
    r=num/den
    return r