import cv2
import matplotlib.pyplot as plt

# Görüntüyü yükle
image = cv2.imread('image1.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Kenar belirleme
edges = cv2.Canny(gray, threshold1=100, threshold2=200)

# Sonuçları göster
plt.imshow(edges, cmap='gray')
plt.title('Kenar Belirleme')
plt.axis('off')

# Çıktıyı kaydet
output_filename = 'edges_output1.jpg'
cv2.imwrite(output_filename, edges)

# Çıktı dosyasını göster
plt.savefig(output_filename)
plt.show()