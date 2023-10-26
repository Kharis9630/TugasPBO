# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("Menghitung luas dan volume prisma segitiga")

import math

def hitung_luas_prisma_segitiga(alas, tinggi, panjang_prisma):
    luas = alas * tinggi + 3 * 0.5 * alas * panjang_prisma
    return luas

def hitung_volume_prisma_segitiga(alas, tinggi, panjang_prisma):
    luas_alas = 0.5 * alas * tinggi
    volume = luas_alas * panjang_prisma
    return volume

def main():
    # Input alas, tinggi, dan panjang
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    panjang_prisma = float(input("Masukkan panjang prisma segitiga: "))

    # Hitung luas
    luas = hitung_luas_prisma_segitiga(alas, tinggi, panjang_prisma)

    # Hitung volume
    volume = hitung_volume_prisma_segitiga(alas, tinggi, panjang_prisma)

    # Hasil
    print("Luas Prisma Segitiga:", luas)
    print("Volume Prisma Segitiga:", volume)

if __name__ == "__main__":
    main()

