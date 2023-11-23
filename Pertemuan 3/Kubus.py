import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    r = float(txtjari_jari.get())

    L = round (r ** 2) * 6

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjari_jari.get())

    v = round (r ** 3)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Kubus by NohanX7")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label(frame, text="Nova Subhan / 220511170 / R4")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Jari Jari
jari_jari= Label(frame, text="Jari Jari :")
jari_jari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari Jari
txtjari_jari = Entry(frame)
txtjari_jari.grid(row=1, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas : ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="Volume : ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()