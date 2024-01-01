from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog  # Import the file dialog module
import pytesseract

# Define path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_image_to_text(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def show_text_in_window(image_path):
    # Convert image to text
    text = convert_image_to_text(image_path)

    # Create Tkinter window
    root = Tk()
    root.title("Gambar ke Teks TIF22D/NovaSubhan/220511170")

    # Create a frame with a background color for the text
    text_frame = Frame(root, bg='lightgray')
    text_frame.pack(padx=10, pady=10)

    # Display text inside the frame
    text_label = Label(text_frame, text=text, wraplength=400, justify="left", bg='lightgray')
    text_label.pack(padx=10, pady=10)

    # Display image in the window
    img = Image.open(image_path)
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)

    img_label = Label(root, image=img)
    img_label.image = img
    img_label.pack(padx=10, pady=10)

    # Run the Tkinter main loop
    root.mainloop()

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select an Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        show_text_in_window(file_path)

# Use a button to trigger the file dialog
root = Tk()
root.title("Open Image to Text")

open_button = Button(root, text="Open Image", command=open_file_dialog)
open_button.pack(padx=10, pady=10)

root.mainloop()
