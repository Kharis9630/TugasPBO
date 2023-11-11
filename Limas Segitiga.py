# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk
from math import sqrt

def hitung():
    alas = float(entry_alas.get())
    tinggi_alas = float(entry_tinggi_alas.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    luas_permukaan = alas * tinggi_alas + 0.5 * alas * sqrt((tinggi_limas**2) - (tinggi_alas**2))
    volume = (1/3) * (alas**2) * tinggi_limas

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")


window = tk.Tk()
window.title("Limas Segitiga")
window.configure(background="teal")
window.geometry("400x200")

label_alas = tk.Label(window, text="Alas Segitiga:")
label_alas.pack()

entry_alas = tk.Entry(window)
entry_alas.pack()

label_tinggi_alas = tk.Label(window, text="Tinggi Alas:")
label_tinggi_alas.pack()

entry_tinggi_alas = tk.Entry(window)
entry_tinggi_alas.pack()

label_tinggi_limas = tk.Label(window, text="Tinggi Limas:")
label_tinggi_limas.pack()

entry_tinggi_limas = tk.Entry(window)
entry_tinggi_limas.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()


window.mainloop()
