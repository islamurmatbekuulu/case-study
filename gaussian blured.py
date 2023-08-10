import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)

# Gaussian bulanıklaştırma
blurred_gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# Sonuçları göster
plt.imshow(cv2.cvtColor(blurred_gaussian, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Bulanıklaştırma')
plt.axis('off')
plt.show()


# Çıktıyı kaydet
output_filename = 'gaussian_blurred_output.jpg'
cv2.imwrite(output_filename, blurred_gaussian)