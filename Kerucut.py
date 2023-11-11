# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk
from math import pi, sqrt

def hitung():
    jari_jari = float(entry_jari_jari.get())
    tinggi = float(entry_tinggi.get())

    volume = (1/3) * pi * (jari_jari ** 2) * tinggi
    sisi_miring = sqrt((jari_jari ** 2) + (tinggi ** 2))
    luas_permukaan = pi * jari_jari * (jari_jari + sisi_miring)

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")

window = tk.Tk()
window.title("Kerucut")
window.configure(background="teal")
window.geometry("400x200")

label_jari_jari = tk.Label(window, text="Jari-Jari Kerucut:")
label_jari_jari.pack()

entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack()

label_tinggi = tk.Label(window, text="Tinggi Kerucut:")
label_tinggi.pack()

entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()