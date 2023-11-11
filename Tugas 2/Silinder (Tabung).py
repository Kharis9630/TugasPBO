# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk
from math import pi

def hitung():
    jari_jari = float(entry_jari_jari.get())
    tinggi = float(entry_tinggi.get())

    volume = pi * (jari_jari ** 2) * tinggi
    luas_permukaan = 2 * pi * jari_jari * (jari_jari + tinggi)

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")

window = tk.Tk()
window.title("Silinder (Tabung)")
window.configure(background="teal")
window.geometry("400x200")

label_jari_jari = tk.Label(window, text="Jari-Jari Silinder:")
label_jari_jari.pack()

entry_jari_jari = tk.Entry(window)
entry_jari_jari.pack()

label_tinggi = tk.Label(window, text="Tinggi Silinder:")
label_tinggi.pack()

entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()