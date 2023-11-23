from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Sisi 1 :').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi 2 :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sisi 3 :').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Tinggi :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtsisi1 = Entry(mainFrame) 
        self.txtsisi1.grid(row=0, column=1, padx=5, pady=5)
        self.txtsisi2 = Entry(mainFrame) 
        self.txtsisi2.grid(row=1, column=1, padx=5, pady=5)
        self.txtsisi3 = Entry(mainFrame) 
        self.txtsisi3.grid(row=2, column=1, padx=5, pady=5)
        self.txttinggi = Entry(mainFrame) 
        self.txttinggi.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=4, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        s1 = int(self.txtsisi1.get())
        s2 = int(self.txtsisi2.get())
        s3 = int(self.txtsisi3.get())
        t = int(self.txttinggi.get())
        luas = round(s1 + s2 + s3) * t
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaSegitiga(root, "Program Luas Prisma Segitiga")
    root.mainloop() 