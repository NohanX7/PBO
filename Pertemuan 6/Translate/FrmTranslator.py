from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x00")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Bahasa Indonesia :').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Bahasa Thailand :').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Bahasa Jepang :').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Bahasa Korea :').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=2, column=1, padx=5, pady=5)

        self.txtHasil1 = Entry(mainFrame, width=50) 
        self.txtHasil1.grid(row=3, column=1, padx=5, pady=5)
        
        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate Thai',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=0, padx=5, pady=5)
        # Pasang Button 2
        self.btnTranslate = Button(mainFrame, text='Translate Jpn',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5)
        # Pasang Button 3
        self.btnTranslate = Button(mainFrame, text='Translate Korea',
            command=self.onTranslate)
        self.btnTranslate.grid(row=1, column=2, padx=5, pady=5)   

    def onTranslate(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest='th')
        hasil1 = penterjemah.translate(self.txtSumber.get(), src='id', dest='ja')
        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='ko')  
       
        # menampilkan hasil terjemahan
        self.txtHasil.insert(END,hasil.text)
        self.txtHasil1.insert(END,hasil1.text)
        self.txtHasil2.insert(END,hasil2.text)


    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 