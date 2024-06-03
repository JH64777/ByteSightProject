from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class GuideWindow(QDialog): # 가이드 창을 위한 클래스
    def __init__(self):
        super().__init__()
        self.MakeWindow()
    
    def MakeWindow(self):
        layV = QVBoxLayout()
        layH = QHBoxLayout()
        link_label = QLabel() # 링크를 만들기 위한 코드

        link = "https://www.naver.com"
        link_label.setText(f'<a href="{link}">Test Link</a>') # URL 생성
        link_label.setOpenExternalLinks(True) # 외부 링크 열기 활성화
        layV.addStretch(1)
        layV.addWidget(link_label) # 레이아웃 안에 URL링크 위젯 추가
        layV.addStretch(1)

        layH.addStretch(1)
        layH.addLayout(layV)
        layH.addStretch(1)

        self.setWindowTitle("GuideBook") # 해당 윈도우의 제목
        self.setLayout(layH) # 레이아웃 추가
        self.setWindowModality(Qt.NonModal) # 해당 윈도우가 생성이 되고난 뒤에 다른 윈도우 창들과 상호작용이 가능한지에 대한 코드(현재 상호작용 가능함)
        self.setGeometry(300, 300, 400, 350) # 윈도우의 위치와 크기
        
    def ShowWindow(self):
        self.show()