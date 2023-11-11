# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk
from math import sqrt

def hitung():
    alas = float(entry_alas.get())
    tinggi_alas = float(entry_tinggi_alas.get())
    tinggi_prisma = float(entry_tinggi_prisma.get())

    luas_permukaan = 2 * (alas * tinggi_alas) + (alas * 3 * tinggi_prisma)
    volume = (1/2) * alas * tinggi_alas * tinggi_prisma

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")

window = tk.Tk()
window.title("Prisma Segitiga")
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

label_tinggi_prisma = tk.Label(window, text="Tinggi Prisma:")
label_tinggi_prisma.pack()

entry_tinggi_prisma = tk.Entry(window)
entry_tinggi_prisma.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()
