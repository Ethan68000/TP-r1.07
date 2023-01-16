a = np.array(all_numbers)
np.savetxt('tentative1.txt', a, end=' ', fmt='%d')
a2 = np.loadtxt('tentative1.txt', dtype=int)
print(a == a2)