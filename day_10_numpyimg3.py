import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('images.png').convert('RGB')
img_np = np.array(img)

flipped=img_np[:,::-1,:]

plt.subplot(1,2,1)
plt.title("original")
plt.imshow(img_np)

plt.subplot(1,2,2)
plt.title("flipped")
plt.imshow(flipped)
plt.show()
