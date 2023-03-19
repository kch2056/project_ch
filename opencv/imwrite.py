import cv2

file_path = "opencv\Lenna.png"

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

print(img)

cv2.imshow('Lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('opencv\gray.png', img)
