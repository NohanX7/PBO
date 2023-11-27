from gtts import gTTS
import os
import pygame
from tkinter import Tk, Label, Button, Text

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text to Sound")

        self.label = Label(master, text="Masukkan Teks:")
        self.label.pack()

        self.text_entry = Text(master, height=5, width=50)
        self.text_entry.pack()

        self.play_button = Button(master, text="Putar", command=self.play_text)
        self.play_button.pack()

    def play_text(self):
        text_to_speak = self.text_entry.get("1.0", "end-1c")
        if text_to_speak:
            # Simpan teks ke file suara
            tts = gTTS(text=text_to_speak, lang="id")
            tts.save("output.mp3")

            # Putar file suara menggunakan pygame
            pygame.mixer.init()
            pygame.mixer.music.load("output.mp3")
            pygame.mixer.music.play()

root = Tk()
app = TextToSpeechApp(root)
root.mainloop()