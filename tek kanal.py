import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Griye dönüştürme (Tek Bir Kanal Seçme Yöntemi)
gray_channel = image[:, :, 2]  # Kırmızı renk kanalını seçebilirsiniz
gray_channel = gray_channel.astype('uint8')

# Sonuçları göster
plt.imshow(gray_channel, cmap='gray')
plt.title('Gri Renge Dönüştürme (Tek Bir Kanal Seçme)')
plt.axis('off')
plt.show()

# Kaydet
output_name ='channel_gray.jpg'
cv2.imwrite(output_name, gray_channel)
