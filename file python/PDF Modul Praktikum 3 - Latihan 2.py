#Program Menampilkan Bilangan Terbesar

angka = list()
while True:
    n = int(input("Masukan Bilangan :"))
    angka.append(n)
    if n == 0:
            break
print("Bilangan Terbesar:",max(angka) )

