a = float(input("masukkan bilangan pertama:"))
b = float(input("masukkan bilangan kedua:"))
c = float(input("masukkan nilai ketiga:"))

if (a >= b) and (a >= c):
    terbesar = a
elif (b >= a) and (b >= c):
    terbesar = b
else:
    terbesar = c
print(f"bilangan terbear adalah:{terbesar}")