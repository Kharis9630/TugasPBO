# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume kubus")

def hitung_luas_kubus(sisi):
    return 6 * sisi**2

def hitung_volume_kubus(sisi):
    return sisi**3

def main():
    # Input panjang sisi
    sisi = float(input("Masukkan panjang sisi kubus: "))

    # Hitung luas kubus
    luas_kubus = hitung_luas_kubus(sisi)

    # Hitung volume kubus
    volume_kubus = hitung_volume_kubus(sisi)

    # Hasil
    print("Luas Kubus:", luas_kubus)
    print("Volume Kubus:", volume_kubus)

if __name__ == "__main__":
    main()
