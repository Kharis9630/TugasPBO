# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk

def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi_limas = float(entry_tinggi_limas.get())

    luas_permukaan = panjang * lebar + 2 * (panjang * tinggi_limas + lebar * tinggi_limas)
    volume = (1/3) * panjang * lebar * tinggi_limas

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")

window = tk.Tk()
window.title("Limas Segiempat")
window.configure(background="teal")
window.geometry("400x200")

label_panjang = tk.Label(window, text="Panjang Alas:")
label_panjang.pack()

entry_panjang = tk.Entry(window)
entry_panjang.pack()

label_lebar = tk.Label(window, text="Lebar Alas:")
label_lebar.pack()

entry_lebar = tk.Entry(window)
entry_lebar.pack()

label_tinggi_limas = tk.Label(window, text="Tinggi Limas:")
label_tinggi_limas.pack()

entry_tinggi_limas = tk.Entry(window)
entry_tinggi_limas.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()
