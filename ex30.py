a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
filtered = filter (lambda x: x % 2 == 0, a)
print(list(filtered))
maped = map (lambda x: x % 2 == 0, a)
print(list(maped))



