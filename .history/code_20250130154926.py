import cv2
import os

# Pastikan nama file video sesuai dengan yang diunggah di Kaggle
video_path = "/kaggle/input/nama-file-video.mp4"  # Ganti dengan path video di Kaggle

# Buat folder untuk menyimpan gambar hasil ekstraksi
output_folder = "/kaggle/working/frames"
os.makedirs(output_folder, exist_ok=True)

# Buka video
cap = cv2.VideoCapture(video_path)

frame_count = 0
frame_interval = 30  # Ambil gambar setiap 30 frame

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Berhenti jika video selesai

    if frame_count % frame_interval == 0:  # Simpan gambar tiap 30 frame
        frame_filename = f"{output_folder}/frame_{frame_count}.jpg"
        cv2.imwrite(frame_filename, frame)
        print(f"Disimpan: {frame_filename}")

    frame_count += 1

cap.release()
print("Ekstraksi gambar selesai!")
