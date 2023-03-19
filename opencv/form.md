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
file_path = "opencv\Lenna.png"
```

</br>

## 이미지 설정

> 📝 이미지를 흑백으로 설정하는 코드

```python
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
```

</br>

## 이미지 행

> 📝 이미지의 행을 출력하는 코드

```python
print(img)
```

</br>

## 이미지 출력

> 📝 이미지를 출력하는 코드

```python
cv2.imshow('Lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

</br>

## 이미지 저장

> 📝 출력된 이미지를 저장하는 코드

```python
cv2.imshow('Lenna', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
