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