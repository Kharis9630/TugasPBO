# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume kerucut")

import math

def hitung_luas_kerucut(jari_jari, garis_pelukis):
    luas = math.pi * jari_jari * (jari_jari + garis_pelukis)
    return luas

def hitung_volume_kerucut(jari_jari, tinggi):
    volume = (1/3) * math.pi * jari_jari**2 * tinggi
    return volume

def main():
    # Input jari-jari dan tinggi kerucut
    jari_jari = float(input("Masukkan jari-jari dasar kerucut: "))
    tinggi = float(input("Masukkan tinggi kerucut: "))

    # Menghitung garis pelukis kerucut
    garis_pelukis = math.sqrt(jari_jari**2 + tinggi**2)

    # Hitung luas kerucut
    luas_kerucut = hitung_luas_kerucut(jari_jari, garis_pelukis)

    # Hitung volume kerucut
    volume_kerucut = hitung_volume_kerucut(jari_jari, tinggi)

    # Hasil
    print("Luas Kerucut:", luas_kerucut)
    print("Volume Kerucut:", volume_kerucut)

if __name__ == "__main__":
    main()

