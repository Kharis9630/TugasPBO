# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume silinder")

import math

def hitung_luas_permukaan(radius, tinggi):
    luas_permukaan = 2 * math.pi * radius * (radius + tinggi)
    return luas_permukaan

def hitung_volume(radius, tinggi):
    volume = math.pi * radius**2 * tinggi
    return volume

def main():
    # Input radius dan tinggi
    radius = float(input("Masukkan panjang jari-jari silinder: "))
    tinggi = float(input("Masukkan tinggi silinder: "))

    # Hitung luas permukaan dan volume
    luas_permukaan = hitung_luas_permukaan(radius, tinggi)
    volume = hitung_volume(radius, tinggi)

    # Hasil
    print("Luas Permukaan Silinder:", luas_permukaan)
    print("Volume Silinder:", volume)

if __name__ == "__main__":
    main()


