from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
from celcius import Fahrenheitgui

class FrmFahrenheit:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='Fahrenheit:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celsius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)

        self.txtFahrenheit = Entry(mainFrame)
        self.txtFahrenheit.grid(row=0, column=1, padx=5, pady=5)

        self.txtCelsius = Entry(mainFrame)
        self.txtCelsius.grid(row=2, column=1, padx=5, pady=5)

        self.txtReamur = Entry(mainFrame)
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5)

        self.txtKelvin = Entry(mainFrame)
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def onHitung(self):
        F = Fahrenheit(float(self.txtFahrenheit.get()))

        # Suhu dalam Celsius
        C = F.get_celsius()
        self.txtCelsius.delete(0, END)
        self.txtCelsius.insert(END, str(C))

        # Suhu dalam Reamur
        R = F.get_reamur()
        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))

        # Suhu dalam Kelvin
        K = F.get_kelvin()
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END, str(K))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = FrmFahrenheit(root, "Program Konversi Suhu Fahrenheit")
    root.mainloop()
