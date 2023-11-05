import cv2
import numpy as  np
from matplotlib import pyplot as plt


foto = cv2.imread("cat.png",0)
cv2.imshow("cat",foto)

if foto is not None:
    Hist = np.zeros(256)
    w,h = foto.shape

for i in range (0, w):
    for j in range(0, h):
        a = foto[i,j]
        Hist[a] = Hist[a] + 1


plt.plot(Hist)
plt.show()
cv2.waitKey()

