import cv2

file_path = "opencv\Lenna.png"

img = cv2.imread(file_path)

print(img)

cv2.imshow('Lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
