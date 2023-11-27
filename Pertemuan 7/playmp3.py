import pygame
import tkinter as tk
from tkinter import ttk, W, Frame

pygame.init()

# Initialize mixer module
pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("Music Player by NohanX7")

# Load the music file
music_file = "Creep-Radiohead.mp3"
pygame.mixer.music.load(music_file)

# Function to play the music
def play_music():
    pygame.mixer.music.play()

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to unpause the music
def unpause_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# Create buttons
judul = tk.Label(window, text=music_file)
play_button = ttk.Button(window, text="Play", command=play_music)
pause_button = ttk.Button(window, text="Pause", command=pause_music)
unpause_button = ttk.Button(window, text="Unpause", command=unpause_music)
stop_button = ttk.Button(window, text="Stop", command=stop_music)

# Grid layout for buttons
judul.grid(row=0, column=0, padx=5, pady=5)
play_button.grid(row=1, column=0, padx=10, pady=10)
pause_button.grid(row=1, column=1, padx=10, pady=10)
unpause_button.grid(row=1, column=2, padx=10, pady=10)
stop_button.grid(row=1, column=3, padx=10, pady=10)

# Run the GUI
window.mainloop()
