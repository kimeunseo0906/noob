import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('test.png').convert('L')
img_np = np.array(img)

inverted=255-img_np

plt.subplot(1,2,1)
plt.title("원본이미지")
plt.imshow(img_np,cmap='gray')

plt.subplot(1,2,2)
plt.title("반전이미지")
plt.imshow(inverted,cmap='gray')
plt.show()
