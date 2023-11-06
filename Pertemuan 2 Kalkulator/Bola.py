import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    r = float(txtjarijari.get())

    from math import pi
    L = round(4 * pi * (r ** 2) // 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    r = float(txtjarijari.get())

    from math import pi
    v = round((4/3) * pi * (r ** 3) // 1)

    txtVolume.delete(0,END)
    txtVolume.insert(END,v)

def hitung():
    hitung_luas()
    hitung_volume()

# Buat Objek Tk Inter
app = tk.Tk()

# Tambahkan Judul
app.title("Kalkulator Luas Dan Volume Bola by NohanX7")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Nama
nama= Label(frame, text="Nova Subhan / 220511170 / R4")
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Label Jari-Jari
jarijari= Label(frame, text="Jari Jari :")
jarijari.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Textbox Jari-Jari
txtjarijari = Entry(frame)
txtjarijari.grid(row=1, column=1)

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