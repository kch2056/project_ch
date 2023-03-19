import cv2

file_path1 = "opencv\Lenna.png"
file_path2 = "opencv\dog.jpg"
file_path3 = "opencv\wolf.jpg"
file_path4 = "opencv\hyena.jpg"

img1 = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(file_path3, cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread(file_path4, cv2.IMREAD_GRAYSCALE)

print(img1)
print(img2)
print(img3)
print(img4)

cv2.imshow('Lenna', img1)
cv2.imshow('dog', img2)
cv2.imshow('wolf', img3)
cv2.imshow('hyena', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
