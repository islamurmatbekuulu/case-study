import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('your_image.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sobel kenar dedektörü
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
edges_sobel = cv2.magnitude(sobelx, sobely)

# Sonuçları göster
plt.imshow(edges_sobel, cmap='gray')
plt.title('Sobel Kenar Dedektörü')
plt.axis('off')

# Çıktıyı kaydet
output_filename = 'edges_sobel.jpg'
cv2.imwrite(output_filename, edges_sobel)
plt.show()