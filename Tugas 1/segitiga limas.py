# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume limas segitiga")

import math

def hitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def hitung_luas_limas_segitiga(alas, tinggi_alas, tinggi_limas):
    luas_alas = hitung_luas_segitiga(alas, tinggi_alas)
    luas_sisi = 3 * hitung_luas_segitiga(alas, tinggi_limas)
    luas_limas = luas_alas + luas_sisi
    return luas_limas

def hitung_volume_limas_segitiga(alas, tinggi_alas, tinggi_limas):
    luas_alas = hitung_luas_segitiga(alas, tinggi_alas)
    volume_limas = (1/3) * luas_alas * tinggi_limas
    return volume_limas

def main():
    # Input alas, tinggi alas, dan tinggi limas
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi_alas = float(input("Masukkan tinggi alas segitiga: "))
    tinggi_limas = float(input("Masukkan tinggi limas segitiga: "))

    # Hitung luas
    luas_limas = hitung_luas_limas_segitiga(alas, tinggi_alas, tinggi_limas)

    # Hitung volume
    volume_limas = hitung_volume_limas_segitiga(alas, tinggi_alas, tinggi_limas)

    # Hasil
    print("Luas Limas Segitiga:", luas_limas)
    print("Volume Limas Segitiga:", volume_limas)

if __name__ == "__main__":
    main()
