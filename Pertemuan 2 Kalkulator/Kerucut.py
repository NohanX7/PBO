import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    r = float(txtjari_jari.get())
    s = float(txtgarispelukis.get())
    t = float(txttinggikerucut.get())

    from math import pi

    L = round(pi * r * s) + pi * (r ** 2) // 1

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())
    s = float(txtgarispelukis.get())
    t = float(txttinggikerucut.get())

    from math import pi

    v = (1/3) * pi * (r ** 2) * t // 1

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Kerucut by NohanX7")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Jari Jari
nama= Label(frame, text="Nova Subhan / 220511170")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Jari Jari
jari_jari= Label(frame, text="Jari Jari :")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Garis Pelukis
garispelukis= Label(frame, text="Garis Pelukis :")
garispelukis.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Kerucut
tinggikerucut= Label(frame, text="Tinggi Kerucut :")
tinggikerucut.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Textbox Garis Pelukis
txtgarispelukis = Entry(frame)
txtgarispelukis.grid(row=2, column=1)

# Textbox Tinggi Kerucut
txttinggikerucut = Entry(frame)
txttinggikerucut.grid(row=3, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()