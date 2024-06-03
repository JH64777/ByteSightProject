import os
import re

class FileManager:
    def __init__(self, path):
        self.path = path # "C:\\Users\\CS4_12\\Desktop\\test.hwp"
        self.name = path.split("//")
        self.file_size = os.path.getsize(path)
        self.data = None
        self.dataset = []
    
    def ReadData(self):
        self.file = open(self.path, mode="rb") # 파일 닫기
        self.data = self.file.read(self.file_size).hex() # hex값 표현방식으로 데이터 변환 후 저장
        self.file.close() # 파일 닫기
        hex_pairs = re.findall(r'\w{2}', self.data) # 정규표현식으로 2 글자씩 잘라서 리스트화
        formatdata = ' '.join(hex_pairs) # 중간 중간에 공백 문자를 넣는 방식으로 다시 문자열로 만듦
        formatdata = formatdata.upper()

        for i in range(0, len(formatdata), 48): # 16(16개의 열) * 2(16진수 두 글자) + 16(공백의 수) - 1(맨 마지막 제거할 공백)
            self.dataset.append(formatdata[i:i+47]) # 16byte 만큼씩 잘라서 리스트에 넣음

        return self.dataset, self.name[len(self.name) - 1]
    
    def SaveData(self, newData, path): # 파일을 저장하는 기능
        if path != None: # 다른이름으로 저장할 시
            self.path = path # 경로 초기화
            with open(self.path, "x") as f: # 파일 새로 생성
                f.write(" ") # 아무 글자나 쓰기

        newData = newData.replace("\n", " ") # 줄바꿈 형식을 공백문자로 변경
        newData = newData.split(" ") # 공백 문자를 기준으로 분할
        newData = bytes(list((map(lambda x: int(x, 16), newData)))) # 각 요소들을 int형(16진수 형태)으로 변경 후 리스트화 시킨 뒤 바이트문자열로 변경
        self.file = open(self.path, mode="wb") # 파일 열기
        self.file.write(newData) # 파일 덮어쓰기
        self.file.close() # 파일 닫기
