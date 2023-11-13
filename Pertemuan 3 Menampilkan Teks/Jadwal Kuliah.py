import tkinter as tk
from tkinter import filedialog, Label, W

# Fungsi untuk menambahkan jadwal kuliah ke daftar
def tambahkan_jadwal():
    hari = hari_entry.get()
    jam = jam_entry.get()
    kelas = kelas_entry.get()
    matakuliah = matakuliah_entry.get()
    jadwal = f"Hari : {hari}, Jam : {jam}, Kelas : {kelas}, Matakuliah : {matakuliah}\n"
    jadwal_text.insert(tk.END, jadwal)

# Fungsi untuk menyimpan jadwal ke file
def simpan_jadwal():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(jadwal_text.get('1.0', tk.END))

# Fungsi untuk membuka jadwal dari file
def buka_jadwal():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            jadwal = file.read()
            jadwal_text.delete('1.0', tk.END)
            jadwal_text.insert(tk.END, jadwal)

# Membuat jendela tkinter
root = tk.Tk()
root.title("Jadwal Kuliah")

# Mengatur ukuran jendela
lebar = 360
tinggi = 500
root.geometry(f"{lebar}x{tinggi}")

# Mengubah warna latar belakang menjadi merah
root.configure(bg='grey')

# Membuat entri untuk hari
hari_label = tk.Label(root, text="Hari :")
hari_label.grid(row=0, column=0)
hari_entry = tk.Entry(root)
hari_entry.grid(row=0, column=1)

# Membuat entri untuk jam
jam_label = tk.Label(root, text="Jam :")
jam_label.grid(row=1, column=0)
jam_entry = tk.Entry(root)
jam_entry.grid(row=1, column=1)

# Membuat entri untuk kelas
kelas_label = tk.Label(root, text="Kelas :")
kelas_label.grid(row=2, column=0)
kelas_entry = tk.Entry(root)
kelas_entry.grid(row=2, column=1)

# Membuat entri untuk nama mata kuliah
matakuliah_label = tk.Label(root, text="Mata Kuliah :")
matakuliah_label.grid(row=3, column=0)
matakuliah_entry = tk.Entry(root)
matakuliah_entry.grid(row=3, column=1)

# Tombol untuk menambahkan jadwal
tambah_button = tk.Button(root, text="Tambah Jadwal", command=tambahkan_jadwal)
tambah_button.grid(row=4, column=0, columnspan=2)

# Area teks untuk menampilkan jadwal
jadwal_text = tk.Text(root, height=20, width=40)
jadwal_text.grid(row=5, column=0, columnspan=2)

# Label Nama
nama= Label(root, text="Nova Subhan / 220511170 / R4")
nama.grid(row=5, column=0, sticky=W, padx=5, pady=5)

# Tombol untuk menyimpan jadwal ke file
simpan_button = tk.Button(root, text="Simpan Jadwal", command=simpan_jadwal)
simpan_button.grid(row=6, column=0, columnspan=2)

# Tombol untuk membuka jadwal dari file
buka_button = tk.Button(root, text="Buka Jadwal", command=buka_jadwal)
buka_button.grid(row=7, column=0, columnspan=2)

root.mainloop()
