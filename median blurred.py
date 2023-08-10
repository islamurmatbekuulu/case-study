import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Median bulanıklaştırma
blurred_median = cv2.medianBlur(image, 5)

# Sonuçları göster
plt.imshow(cv2.cvtColor(blurred_median, cv2.COLOR_BGR2RGB))
plt.title('Median Bulanıklaştırma')
plt.axis('off')
plt.show()

# Çıktıyı kaydet
output_name='median_blurred_output.jpg'
cv2.imwrite(output_name,blurred_median)