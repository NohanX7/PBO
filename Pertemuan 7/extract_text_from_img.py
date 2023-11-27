from tkinter import *
from PIL import Image, ImageTk
import pytesseract

#Define path to tessaract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_image_to_text(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def show_text_in_window(image_path):
    # Konversi gambar menjadi teks
    text = convert_image_to_text(image_path)
    
    # Membuat Windows
    root = Tk()
    root.title("Gambar ke Teks by NohanX7")

    # Menampilkan teks di dalam jendela
    text_label = Label(root, text=text, wraplength=400, justify="left")
    text_label.pack(padx=10, pady=10)

    # Menampilkan gambar di dalam jendela
    img = Image.open(image_path)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)

    img_label = Label(root, image=img)
    img_label.image = img
    img_label.pack(padx=10, pady=10)

    # Menjalankan loop utama Tkinter
    root.mainloop()

#Define path to image
gambar_path = 'gambar2.jpg'
show_text_in_window(gambar_path)
