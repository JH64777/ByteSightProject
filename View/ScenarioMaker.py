from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class ScenarioFactory(QDialog):
    def __init__(self, width, height):
        super().__init__()
        self.w = width
        self.h = height

    def Scenario(self, name, URL):
        layV = QVBoxLayout()
        layH = QHBoxLayout()
        link_label = QLabel() # 링크를 만들기 위한 코드
        explanation = QLabel() # 설명을 위한 코드
        
        print(f'<a href="{URL}">Test Link</a>')
        explanation.setText("<h1>ByteSight에 오신 것을 환영합니다</h1><br>아래 링크를 통해 연습 자료와 시나리오를 받아 파일 분석의 기초를 배워보세요!<br>")
        link_label.setText(f'<a href="{URL}">{name} Data</a>')
        link_label.setOpenExternalLinks(True) # 외부 링크 열기 활성화
        layV.addStretch(1)
        layV.addWidget(explanation)
        layV.addWidget(link_label)
        layV.addStretch(1)

        layH.addStretch(1)
        layH.addLayout(layV)
        layH.addStretch(1)

        self.setWindowTitle(name) # 해당 윈도우의 제목
        self.setLayout(layH) # 레이아웃 추가
        self.setWindowModality(Qt.NonModal) # 해당 윈도우가 생성이 되고난 뒤에 다른 윈도우 창들과 상호작용이 가능한지에 대한 코드(현재 상호작용 가능함)
        self.setGeometry(300, 300, self.w, self.h) # 윈도우의 위치와 크기
        self.show()