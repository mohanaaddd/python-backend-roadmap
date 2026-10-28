f = [1, 2, 3, 4, 5]

print(f.index(5))

f.insert(1, 10)
f.insert(-1, True)
f.append(False)

print(f)

b = f.copy()

f.clear()

print(f)
print(b)

print(b.pop(1))
