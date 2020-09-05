import cv2 as cv
import numpy as np

# 读取一张照片
original = cv.imread("/home/zx/PycharmProjects/opencv/images/s2/7.jpg")

# 在屏幕上显示照片
cv.imshow("Original", original)

# 查看图片的基本信息
print(original.shape)

# 查看某个像素点的颜色(bgr)
print(original[5, 255])

h, w = original.shape[:2]
l, r = int(w / 4), int(w * 3 / 4)
t, b = int(h / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
