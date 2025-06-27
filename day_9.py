import numpy as np
#=np.array([1,2,3,4])
list=[1,2,3,4]

#ist1+1=1

#rint(f"a:{a}")
#rint(f"list1:{list1}")

"""
a=np.array([1,2,3])
b=np.zeros((2,3))
c=np.ones((3,3))
d=np.arange(0,10,2)
f=np.random.rand(2,3)

print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(f"d:{d}")
print(f"f:{f}")
"""

a=np.array([1,2,3])
b=np.array([10,20,30])
#print(f"a+b:{a+b}")
#print(f"a*b:{a*b}")

a=np.array([
    [1,2,3],
    [4,5,6]
])
#print(f"a[0]:{a[0]}")
#print(f"a[:,1]:{a[:,1]}")

import matplotlib.pyplot as plt
image = np.zeros((28,28))
#print(image.shape)

#plt.imshow(image,cmap="gray")
#plt.title('28*28 black image')
#plt.axis('off')
#plt.show()

"""
color_image = np.zeros((100,100,3))
color_image[0:50,0:50]=[0.4,0.4,0.2]
color_image[0:50,0:100]=[0,1,0]
color_image[50:100,50:100][1,1,1]
print(color_image.shape)

plt.imshow(color_image)
plt.title('100*100 color image')
plt.axis('off')
plt.show()
"""

"""
a=np.array=([1,2,3,4,5,6])
#print(a.shape)

b=a.reshape(2,3)
#print(b)

images=np.random.rand(100,28,28)
images=images.reshape(100,28,28,1)

a=np.array([[1,2,],[3,4]])
r=a.ravel()
f=a.flatten()
print(r)
print(f)
"""

"""
color_image = np.zeros((100,100,3))
color_image[0:50,0:50]=[0.4,0.4,0.2]
color_image[0:50,0:100]=[0,1,0]
color_image[50:100,50:100][1,1,1]

features=color_image[25:75,35:80]
print(features.shape)
plt.imshow(features)
plt.title('crop color image')
plt.axis('off')
plt.show()
"""

heights=np.array([160,172,185,150,177])
fileter1=heights>170
#print(heights[fileter1])

scores =np.array([80,90,85,70,100])
std = np.std(scores)
print(std)