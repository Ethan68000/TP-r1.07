import random
import matplotlib as plt
import numpy as np
x = int(input("Combien voulez vous de tirage ?"))
y = int(input("Quelle est ta graine ?"))
random.seed(y)
n_sequences(y)
n_sequences = x
all_numbers = []

for i in range(n_sequences):
    sequence = random.sample(range (1, 46), 5)
    all_numbers.extend(sequence)

    #tri fusion
    def fusion(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            result += left[i:]
            result += right[j:]
            return result
        def fusion_sort(tab):
            if len(tab) < 2:
                return tab
            middle = len(tab) // 2
            left = fusion_sort(tab[:middle])
            right = fusion_sort(tab[middle:])
            return fusion(left, right)
        numbers = fusion_sort(sequence)
        print("{}: Voici les nombres de dparts: {} nombre triée : {}".format(i + 1,sequence, numbers))
