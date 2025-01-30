import cv2  

video_path = "video.mp4"  # Ganti dengan nama file videomu  
cap = cv2.VideoCapture(video_path)  

frame_number = 100  # Ganti dengan frame yang ingin diambil  
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  

ret, frame = cap.read()  
if ret:
    cv2.imwrite("output_frame.jpg", frame)  # Simpan gambar  
    print("Gambar berhasil disimpan sebagai output_frame.jpg")  
else:
    print("Gagal mengambil gambar.")  

cap.release()  
cv2.destroyAllWindows()  
