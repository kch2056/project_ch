import cv2

file_path = "opencv\Lenna.png"

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

print(img)

resized_img = cv2.resize(img, (600, 600))


cv2.imshow('Lenna', img)
cv2.imshow('resized', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
