import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('images.png').convert('RGB')
img_np = np.array(img)

brighter=img_np.astype(np.int32) + 50
brigher=np.clip(brighter,0,255).astype(np.uint8)

plt.subplot(1,2,1)
plt.title("original")
plt.imshow(img_np)

plt.subplot(1,2,2)
plt.title("brighter")
plt.imshow(brighter)
plt.show()
