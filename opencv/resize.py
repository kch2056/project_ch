import cv2

file_path = input()
file_path = "opencv\\" + file_path

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

width = int(input('width? '))
height = int(input('height? '))
resized_img = cv2.resize(img, (width, height))


cv2.imshow('file', img)
cv2.imshow('resized', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
