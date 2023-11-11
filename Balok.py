# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk

def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    tinggi = float(entry_tinggi.get())

    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")

def bersihkan_input():
    entry_lebar.delete(0, tk.END) 
    entry_panjang.delete(0, tk.END)
    entry_tinggi.delete(0, tk.END)
    label_hasil.config(text="Hasil")
    label_lebar.config(text="Lebar")   
    label_panjang.config(text="Panjang")
    label_tinggi.config(text="Tinggi")

window = tk.Tk()
window.title("Balok")
window.configure(background="lime")
window.geometry("400x200")

label_panjang = tk.Label(window, text="Panjang:")
label_panjang.pack()

entry_panjang = tk.Entry(window)
entry_panjang.pack()

label_lebar = tk.Label(window, text="Lebar:")
label_lebar.pack()

entry_lebar = tk.Entry(window)
entry_lebar.pack()

label_tinggi = tk.Label(window, text="Tinggi:")
label_tinggi.pack()

entry_tinggi = tk.Entry(window)
entry_tinggi.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

button_bersihkan_input = tk.Button(window, text="Bersihkan Input", command=bersihkan_input)
button_bersihkan_input.pack()

window.mainloop()
