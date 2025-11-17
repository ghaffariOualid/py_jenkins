def delete_doublons(T):
    d=[]
    for i in T :
        if i not in d :
            d.append(i)
    return d

print( delete_doublons([1, 1, 2, 2, 3, 1]))