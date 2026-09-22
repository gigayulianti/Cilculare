n = int(input("masukkan batas nilai n: "))

print(f"bilangan ganjil sampai dengan {n}:")

for i in range(1, n + 1, 2):
    print(i, end=" ")
print()