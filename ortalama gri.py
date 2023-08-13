import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Griye dönüştürme (Ortalama Değer Yöntemi)
gray_avg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sonuçları göster
plt.imshow(gray_avg, cmap='gray')
plt.title('Gri Renge Dönüştürme (Ortalama Değer)')
plt.axis('off')
plt.show()

#Kaydet
output_name ='ortalama_gray.jpg'
cv2.imwrite(output_name,gray_avg)

