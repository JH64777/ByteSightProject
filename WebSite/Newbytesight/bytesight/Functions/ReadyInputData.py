import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

def ReadyXdata(file): # 입력 데이터 준비
    print(file)
    with open(file, 'rb') as f:
        hdata = list(f.read())
        count, length, patches = plt.hist(hdata, bins=256, range=(0, 255)) # 히스토그램 값 반환
        plt.clf()

        fileSize = os.path.getsize(file) # 사진의 용량
        print(f"사진 정보 : {file}")
        img = cv2.imread(file) # 사진의 총 픽셀 값을 구하기 위해 읽기
        count = np.append(count, abs(fileSize - len(img) * len(img[0])) / 1024) # (사진의 용량 - 사진의 총 픽셀 값) 추가
        count = np.log1p(count) # 로그 변환 (로그 함수로 만드는 작업, 한쪽으로 편향되지 않게끔 정규화 하는 것)
        return np.array([count])