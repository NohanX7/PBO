import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas_selimut():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    from math import pi
    ls = round (2 * pi * r * t)

    txtLuasSelimut.delete(0,END)
    txtLuasSelimut.insert(END,ls)

def hitung_luas_permukaan():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    from math import pi
    lp = round(2 * pi * r * t) + (2 * pi * r ** 2) // 1

    txtLuasPermukaan.delete(0,END)
    txtLuasPermukaan.insert(END,lp)

def hitung_volume():
    r = float(txtjarijari.get())
    t = float(txttinggi.get())

    from math import pi
    v = round(pi * r ** 2 * t)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Tabung by NohanX7")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label(frame, text="Nova Subhan / 220511170 / R4")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Jari Jari
jarijari= Label(frame, text="Jari-Jari :")
jarijari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi
tinggi= Label(frame, text="Tinggi :")
tinggi.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=1, column=1)

# Textbox Tinggi
txttinggi = Entry(frame)
txttinggi.grid(row=2, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luasselimut = Label(frame, text="Luas Selimut : ")
luasselimut.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luaspermukaan = Label(frame, text="Luas Permukaan : ")
luaspermukaan.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=4, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasPermukaan = Entry(frame)
txtLuasPermukaan.grid(row=5, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

app.mainloop()