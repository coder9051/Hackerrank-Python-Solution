from itertools import permutations
word, number = input().split()
combination = list(permutations(word, int(number)))
combination.sort()
for i in combination:
    print("".join(i))
