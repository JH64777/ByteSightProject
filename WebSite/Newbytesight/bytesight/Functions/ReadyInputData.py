import numpy as np
from matplotlib.pyplot import hist, close

def PreProcessData(path): # 2024-09-27
    with open(path, "rb") as f:
        data = f.read()
        f.seek(data.find(b"\xff\xda") + 2) # JPEG파일의 SOS 영역을 찾고 Cursor를 해당 위치로 옮기는 코드
        totalLength = int.from_bytes(f.read(2), 'big') - 2 # 총 SOS의 길이 (현재 2bytes를 읽어서 커서가 2bytes만큼 이동했으므로 -2를 한 것임, JPEG는 빅 엔디안 방식으로 처리가 되도록 구성되었다고 함)
        EndOfSOS = f.seek(f.tell() + totalLength) # SOS의 마지막 부분으로 이동
        EndOfImage = data.find(b"\xff\xd9", EndOfSOS) # EOI 위치 (SOS와 EOI 사이에는 ff d9라는 값이 존재할 수 없다 판단)
        data = list(data) # 히스토그램 데이터를 위해 리스트화 시킴
        del data[EndOfSOS : EndOfImage] # SOS의 끝 부분 ~ EOI까지의 길이 (Scan Data 즉, 각 셀의 색상 정보) 삭제(RGB값이 있는 곳을 없애기 위함)
        counts, length, patches = hist(data, bins=256, range=(0, 256)) # 히스토그램 값 추출
        close()
        return counts

# 여기서 부터 인공지능 관련 코드

def RangeNormalize(data): # 1 ~ 0사이 값으로 정규화
  return data / 316542 # 316542라는 데이터는 학습 데이터 중에 나온 최대 값

def ReadyInputData(path): # 입력 데이터 만드는 함수
    X = []
    counts = PreProcessData(path)
    X.append(RangeNormalize(counts)) # Hex값에서 RGB값 제거한 데이터 정규화
    return np.array(X)