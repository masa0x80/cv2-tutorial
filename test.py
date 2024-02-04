import cv2

# imreadの第二引数に `cv2.IMREAD_GRAYSCALE` を使用すると、
# OpenCVではなくコーデックによる変換になるので、
# 画素値を厳密に計算したい場合は別途 `cvtColor` するのが良い。
#
# ref. https://note.nkmk.me/python-opencv-numpy-color-to-gray/#cv2imread
img = cv2.imread("images/sample.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, img_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

cv2.imshow("Display window", img_otsu)
k = cv2.waitKey(0)
