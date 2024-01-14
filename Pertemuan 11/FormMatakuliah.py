import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from matakuliah import matakuliah

class FormMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode MK :').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtKodemk = Entry(mainFrame) 
        self.txtKodemk.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodemk.bind("<Return>",self.onCari) # menambahkan event Enter key 

        Label(mainFrame, text='Nama MK :').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNamamk = Entry(mainFrame) 
        self.txtNamamk.grid(row=1, column=1, padx=5, pady=5)

        Label(mainFrame, text='SKS :').grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.txtSks = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 5, textvariable = self.txtSks) 
        Cbo.grid(row=2, column=1, padx=5, pady=5)
        Cbo['values'] = ('2','3','4')
        Cbo.current()      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'kodemk', 'namamk','sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='KodeMk')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # set tree position
        self.tree.place(x=0, y=150)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKodemk.delete(0,END)
        self.txtKodemk.insert(END,"")
        self.txtNamamk.delete(0,END)
        self.txtNamamk.insert(END,"")       
        self.txtSks.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        mk = matakuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kodemk = self.txtKodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtKodemk.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKodemk.get()
        mk = matakuliah()
        res = mk.getBykodemk(kodemk)
        self.txtKodemk.delete(0,END)
        self.txtKodemk.insert(END,mk.kodemk)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtKodemk.get()
        namamk = self.txtNamamk.get()
        sks = self.txtSks.get()
        
        mk = matakuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if(self.ditemukan==True):
            res = mk.updateBykodemk(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKodemk.get()
        mk = matakuliah()
        mk.kodemk = kodemk
        if(self.ditemukan==True):
            res = mk.deleteBykodemk(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop() 