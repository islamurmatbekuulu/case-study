import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplacian kenar dedektörü
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Sonuçları göster
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Kenar Dedektörü')
plt.axis('off')
plt.show()

# Çıktıyı kaydet
output_filename = 'edges_output2.jpg'
cv2.imwrite(output_filename, laplacian)
