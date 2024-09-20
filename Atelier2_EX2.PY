def nb_occurence(lst, e):
    c = 0
    for elt in lst:
        if elt == e:
            c += 1
    return c

def agencement(Lobj, nbEmplacements):
    Lobj.sort()
    L = Lobj.copy()
    V1 = []
    V2 = []
    LRepetition = [0] * len(L)

    for i in range(len(L)):
        LRepetition[i] = nb_occurence(L, L[i])
  
    for j in range(len(L)):
        if LRepetition[j] > 2:
            return None
        elif LRepetition[j] == 2 and len(V1) < nbEmplacements and len(V2) < nbEmplacements:
            V1.append(L.pop(j))
            V2.append(L.pop(j))
            LRepetition.pop(j) 


    for k in range(len(L)):
        if len(V1) < nbEmplacements:
            V1.append(L[k])
        elif len(V2) < nbEmplacements:
            V2.append(L[k])
        else:
            return None


    V1.sort()
    V2.sort()
    return [V1, V2]


nbEmplacements = 4
lObjets = [1, 2, 2, 3, 4, 5, 5]

print(agencement(lObjets, nbEmplacements))
