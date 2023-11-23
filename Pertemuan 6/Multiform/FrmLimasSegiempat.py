from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmLimasSegiempat:
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
        Label(mainFrame, text='Luas Sisi 1 :').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas Sisi 2 :').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas Sisi 3 :').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas Sisi 4 :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Luas Sisi 5 :').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(mainFrame, text="Luas:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtluassisi1 = Entry(mainFrame) 
        self.txtluassisi1.grid(row=0, column=1, padx=5, pady=5)
        self.txtluassisi2 = Entry(mainFrame) 
        self.txtluassisi2.grid(row=1, column=1, padx=5, pady=5)
        self.txtluassisi3 = Entry(mainFrame) 
        self.txtluassisi3.grid(row=2, column=1, padx=5, pady=5)
        self.txtluassisi4 = Entry(mainFrame) 
        self.txtluassisi4.grid(row=3, column=1, padx=5, pady=5)
        self.txtluassisi5 = Entry(mainFrame) 
        self.txtluassisi5.grid(row=4, column=1, padx=5, pady=5)
        
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=5, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        ls1 = int(self.txtluassisi1.get())
        ls2 = int(self.txtluassisi2.get())
        ls3 = int(self.txtluassisi3.get())
        ls4 = int(self.txtluassisi4.get())
        ls5 = int(self.txtluassisi5.get())
        luas = round(ls1 + ls2 + ls3 + ls4 + ls5)
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmLimasSegiempat(root, "Program Luas Limas Segiempat")
    root.mainloop() 