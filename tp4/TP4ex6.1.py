L1 = [5, 2, 4, 8, 1, 3]
def tri_insertion(L1):
    L = list(L1)
    N = len(L)
    for n in range(1, N):
        cle = L[n]
        j = n - 1
        while j >= 0 and L[j] > cle:
            L[j + 1] = L[j]
            j = j - 1
        L[j + 1] = cle
    return L


for k in range(10):
    liste_triee = tri_insertion(L1)

print(L1)
print(liste_triee)
