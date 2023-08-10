import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Görüntüyü bulanıklaştır
blurred = cv2.blur(image, (5, 5))

# Sonuçları göster
plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
plt.title('Görüntü Bulanıklaştırma')
plt.axis('off')
plt.show()

# Çıktıyı kaydet
output_filename = 'blurred_output.jpg'
cv2.imwrite(output_filename, blurred)