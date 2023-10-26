# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume balok")

import math

def hitung_luas_balok(panjang, lebar, tinggi):
    luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas

def hitung_volume_balok(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def main():
    # Input panjang, lebar, dan tinggi
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))

    # Hitung luas balok
    luas_balok = hitung_luas_balok(panjang, lebar, tinggi)

    # Hitung volume balok
    volume_balok = hitung_volume_balok(panjang, lebar, tinggi)

    # Hasil
    print("Luas Balok:", luas_balok)
    print("Volume Balok:", volume_balok)

if __name__ == "__main__":
    main()



