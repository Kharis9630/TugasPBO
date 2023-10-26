# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume bola")

import math

def hitung_luas_bola(jari_jari):
    luas = 4 * math.pi * jari_jari**2
    return luas

def hitung_volume_bola(jari_jari):
    volume = (4/3) * math.pi * jari_jari**3
    return volume

def main():
    # Input jari-jari bola
    jari_jari = float(input("Masukkan jari-jari bola: "))

    # Hitung luas bola
    luas_bola = hitung_luas_bola(jari_jari)

    # Hitung volume bola
    volume_bola = hitung_volume_bola(jari_jari)

    # Hasil
    print("Luas Bola:", luas_bola)
    print("Volume Bola:", volume_bola)

if __name__ == "__main__":
    main()


