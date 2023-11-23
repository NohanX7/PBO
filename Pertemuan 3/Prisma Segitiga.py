import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas_selimut():
    s1 = float(txtsisi1.get())
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())
    T = float(txttegakprisma.get())

    ls = round(s1 + s2 + s3) * T

    txtLuasSelimut.delete(0,END)
    txtLuasSelimut.insert(END,ls)

def hitung_luas_permukaan():
    s1 = float(txtsisi1.get())
    s2 = float(txtsisi2.get())
    s3 = float(txtsisi3.get())
    T = float(txttegakprisma.get())
    a = float(txtalas.get())
    t = float(txttinggiprisma.get())
    
    lp = round(s1 + s2 + s3) * T + (a + t) 

    txtLuasPermukaan.delete(0,END)
    txtLuasPermukaan.insert(END,lp)

def hitung_volume():
    T = float(txttegakprisma.get())
    a = float(txtalas.get())
    t = float(txttinggiprisma.get())

    v = round(a * t * T / 2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas_selimut()
    hitung_luas_permukaan()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Prisma Segitiga by NohanX7")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label(frame, text="Nova Subhan / 220511170 / R4")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 1
sisi1= Label(frame, text="Sisi 1 :")
sisi1.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 2
sisi2= Label(frame, text="Sisi 2 :")
sisi2.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Label Sisi 3
sisi3= Label(frame, text="Sisi 3 :")
sisi3.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Label Tegak Prisma
tegakprisma= Label(frame, text="Tegak Prisma :")
tegakprisma.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Label Tinggi Prisma
tinggiprisma= Label(frame, text="Tinggi Prisma :")
tinggiprisma.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Label Alas
alas= Label(frame, text="Alas :")
alas.grid(row=6, column=0, sticky=W, padx=5, pady=5)

# Textbox Sisi 1
txtsisi1 = Entry(frame)
txtsisi1.grid(row=1, column=1)

# Textbox Sisi 2
txtsisi2 = Entry(frame)
txtsisi2.grid(row=2, column=1)

# Textbox Sisi 3
txtsisi3 = Entry(frame)
txtsisi3.grid(row=3, column=1)

# Textbox Tegak Prisma
txttegakprisma = Entry(frame)
txttegakprisma.grid(row=4, column=1)

# Textbox TInggi Prisma
txttinggiprisma = Entry(frame)
txttinggiprisma.grid(row=5, column=1)

# Textbox Alas
txtalas = Entry(frame)
txtalas.grid(row=6, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas Selimut
luas = Label(frame, text="Luas Selimut : ")
luas.grid(row=8, column=0, sticky=W, padx=5, pady=5)

# Output Label Luas Permukaan
luas = Label(frame, text="Luas Permukaan : ")
luas.grid(row=9, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=10, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas Selimut
txtLuasSelimut = Entry(frame)
txtLuasSelimut.grid(row=8, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Luas Permukaan
txtLuasPermukaan = Entry(frame)
txtLuasPermukaan.grid(row=9, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=10, column=1, sticky=W, padx=5, pady=5)

app.mainloop()