import tkinter as tk
from tkinter import Frame, Label, Entry, Button, ttk, YES, BOTH, END, messagebox
from Matakuliah import MataKuliah

class FormMatakuliah:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode MK:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKodeMK = Entry(mainFrame) 
        self.txtKodeMK.grid(row=0, column=1, padx=5, pady=5) 
        self.txtKodeMK.bind("<Return>", self.onCari)

        Label(mainFrame, text='Nama MK:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNamaMK = Entry(mainFrame) 
        self.txtNamaMK.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='SKS:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtSKS = ttk.Combobox(mainFrame, width=27) 
        self.txtSKS.grid(row=2, column=1, padx=5, pady=5)
        self.txtSKS['values'] = ('1', '2', '3', '4', '6')
        self.txtSKS.set('1')  # Default value
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # Define columns
        columns = ('id', 'kodemk', 'namamk', 'sks')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # Define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodemk', text='Kode MK')
        self.tree.column('kodemk', width="60")
        self.tree.heading('namamk', text='Nama MK')
        self.tree.column('namamk', width="200")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="30")
        # Set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtKodeMK.delete(0, END)
        self.txtKodeMK.insert(END, "")
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, "")       
        self.txtSKS.set("1")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # Get data matakuliah
        mk = MataKuliah()
        result = mk.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        matakuliahs = []
        for row_data in result:
            matakuliahs.append(row_data)

        for matakuliah in matakuliahs:
            self.tree.insert('', END, values=matakuliah)
    
    def onCari(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = MataKuliah()
        res = mk.getByKodeMK(kodemk)
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNamaMK.focus()
        return res
        
    def TampilkanData(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = MataKuliah()
        res = mk.getByKodeMK(kodemk)
        self.txtNamaMK.delete(0, END)
        self.txtNamaMK.insert(END, mk.namamk)
        self.txtSKS.set(mk.sks)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kodemk = self.txtKodeMK.get()
        namamk = self.txtNamaMK.get()
        sks = self.txtSKS.get()
        
        mk = MataKuliah()
        mk.kodemk = kodemk
        mk.namamk = namamk
        mk.sks = sks
        if self.ditemukan:
            res = mk.updateByKodeMK(kodemk)
            ket = 'Diperbarui'
        else:
            res = mk.simpan()
            ket = 'Disimpan'
            
        rec = mk.affected
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil " + ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal " + ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kodemk = self.txtKodeMK.get()
        mk = MataKuliah()
        mk.kodemk = kodemk
        if self.ditemukan:
            res = mk.deleteByKodeMK(kodemk)
            rec = mk.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if rec > 0:
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormMatakuliah(root, "Aplikasi Data Matakuliah")
    root.mainloop()
