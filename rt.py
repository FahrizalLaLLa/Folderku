import cv2

# Baca gambar
image = cv2.imread('gambar.jpg')

# Menampilkan gambar
cv2.imshow('Gambar', image)
cv2.waitKey(0)
cv2.destroyAllWindows()