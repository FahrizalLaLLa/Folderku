import cv2

# Baca gambar
image = cv2.imread('wajah.jpg')

# Konversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inisialisasi detektor wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Deteksi wajah
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Gambar persegi di sekitar wajah
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Menampilkan gambar dengan wajah terdeteksi
cv2.imshow('Deteksi Wajah', image)
cv2.waitKey(0)
cv2.destroyAllWindows()