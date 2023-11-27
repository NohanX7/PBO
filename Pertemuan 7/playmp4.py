import cv2
import numpy as np

# Buka video file
video_path = 'video1.mp4'
cap = cv2.VideoCapture(video_path)

# Periksa apakah video berhasil dibuka
if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

# Dapatkan informasi video (lebar, tinggi, frame per detik)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Tentukan skala pengurangan untuk menampilkan jendela
scale_percent = 40
scaled_width = int(width * scale_percent / 100)
scaled_height = int(height * scale_percent / 100)

# Buat jendela dengan ukuran yang diubah
cv2.namedWindow('Video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Video', scaled_width, scaled_height)

while True:
    # Baca frame dari video
    ret, frame = cap.read()

    # Periksa apakah berhasil membaca frame
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Perbesar frame sesuai dengan skala yang ditentukan
    scaled_frame = cv2.resize(frame, (scaled_width, scaled_height))

    # Tampilkan frame yang diubah di jendela
    cv2.imshow('Video', scaled_frame)

    # Hentikan pemutaran video jika tombol 'q' ditekan
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

# Tutup video dan jendela ketika selesai
cap.release()
cv2.destroyAllWindows()
