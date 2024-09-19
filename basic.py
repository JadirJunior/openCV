import cv2 as cv

img = cv.imread("photos/Rubro.jpg")

cv.imshow("Rubro", img)

# Convert to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)


# Dillating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)


# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("Resized", resized)


# Cropping
croped = img[50:200, 200:400]
cv.imshow('Cropped', croped)


cv.waitKey(0)