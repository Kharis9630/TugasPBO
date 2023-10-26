# Nama: Kharismajaya Pradana
# Nim : 220511006
# Kelas : TI22K

print("menghitung luas dan volume limas segiempat")

def hitung_luas_alas_segiempat(sisi):
    return sisi**2

def hitung_keliling_alas_segiempat(sisi):
    return 4 * sisi

def hitung_luas_limas_segiempat(sisi, tinggi_limas):
    keliling_alas = hitung_keliling_alas_segiempat(sisi)
    luas_limas = (1/2) * keliling_alas * tinggi_limas
    return luas_limas

def hitung_volume_limas_segiempat(sisi, tinggi_limas):
    luas_alas = hitung_luas_alas_segiempat(sisi)
    volume_limas = (1/3) * luas_alas * tinggi_limas
    return volume_limas

def main():
    # Input panjang sisi dan tinggi
    sisi = float(input("Masukkan panjang sisi alas segiempat: "))
    tinggi_limas = float(input("Masukkan tinggi limas segiempat: "))

    # Hitung luas
    luas_limas = hitung_luas_limas_segiempat(sisi, tinggi_limas)

    # Hitung volume
    volume_limas = hitung_volume_limas_segiempat(sisi, tinggi_limas)

    # Hasil
    print("Luas Limas Segiempat:", luas_limas)
    print("Volume Limas Segiempat:", volume_limas)

if __name__ == "__main__":
    main()
