# 물리융합 코딩 예제

## cv2 모듈 불러오기

> 📝 cv2을 import하는 코드

```python
import cv2
```

</br>

## 이미지 경로 추출

> 📝 이미지 경로를 추출하는 코드

```python
file_path1 = "opencv\Lenna.png"
file_path2 = "opencv\dog.jpg"
file_path3 = "opencv\wolf.jpg"
file_path4 = "opencv\hyena.jpg"
```

</br>

## 이미지 설정

> 📝 4개의 이미지를 흑백으로 설정하는 코드

```python
img1 = cv2.imread(file_path1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(file_path2, cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread(file_path3, cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread(file_path4, cv2.IMREAD_GRAYSCALE)
```

</br>

## 이미지 행

> 📝 4개의 이미지의 행을 출력하는 코드

```python
print(img1)
print(img2)
print(img3)
print(img4)
```

</br>

## 이미지 출력

> 📝 4개의 이미지를 출력하는 코드

```python
cv2.imshow('Lenna', img1)
cv2.imshow('dog', img2)
cv2.imshow('wolf', img3)
cv2.imshow('hyena', img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
```