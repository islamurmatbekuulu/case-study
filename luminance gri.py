import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Luminosity yöntemiyle griye dönüştürme
gray_luminosity = 0.2126 * image[:,:,2] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,0]
gray_luminosity = gray_luminosity.astype('uint8')

# Sonuçları göster
plt.imshow(gray_luminosity, cmap='gray')
plt.title('Gri Renge Dönüştürme (Luminosity)')
plt.axis('off')
plt.show()

# Kaydet
output_name = 'luminosity_gray.jpg'
cv2.imwrite(output_name, gray_luminosity)
