# Kharismajaya Pradana
# 220511006
# TI22K

import tkinter as tk

def hitung():
    sisi = float(entry_sisi.get())
    volume = sisi ** 3
    luas_permukaan = 6 * (sisi ** 2)

    label_hasil.config(text=f"Volume: {volume:.2f}\nLuas Permukaan: {luas_permukaan:.2f}")


window = tk.Tk()
window.title("Kubus")
window.configure(background="teal")
window.geometry("400x200")

label_sisi = tk.Label(window, text="Panjang Sisi:")
label_sisi.pack()

entry_sisi = tk.Entry(window)
entry_sisi.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()


window.mainloop()
