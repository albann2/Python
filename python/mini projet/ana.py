#1
def anagrame(x):
    if len(x) <= 1:
        return [x]
    elif len(x) == 2:
        return list(set([x,x[1]+x[0]]))
    else:
        return list(set([x[i] + d for i in range(len(x)) for d in anagrame(x[:i]+x[i+1:])]))
 
 #2
def trouver_anagrammes(base, lettres, mots, n_lettres):
    if n_lettres == 0:
        mots.append(base)
    else:
        for l in lettres:
            if lettres[l] > 0:
                lettres[l] -= 1
                trouver_anagrammes(base+l, lettres, mots, n_lettres-1)
                lettres[l] += 1
 
def anagrammes(mot):
    lettres = dict([(l, mot.count(l)) for l in set(mot)])
    mots = list()
    trouver_anagrammes('', lettres, mots, len(mot))
    return mots

test = input("Enter string for variable name: ")
print(anagrame(test))
print(anagrammes(test))