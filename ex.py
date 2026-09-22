persen = float(input("Masukkan nilai persentase siswa: "))

if persen >= 90:
    print("luar biasa")
elif persen >= 80:
    print("sangat baik")
elif persen >= 70:
    print("baik")
elif persen >= 60:
    print("cukup")
else:
    print("kurang")

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

n = int(input("masukkan nilai n (jumlah suku fibonacci)"))

a, b = 0, 1
hitung = 0

print("deret fibonacci:")
if n <= 0:
    print("silahkan masukkan bilangan bulat positif lebih dari 0.")
elif n == 1:
    print(a)
else:
    while hitung < n:
        print(a, end=" ")
        
        suku_berikutnya = a + b
        a = b
        b = suku_berikutnya
        hitung += 1
    print()

    n = int(input("masukkan nilai n: "))

for i in range(1, n + 1):
    print((str(i) + " ") * i)