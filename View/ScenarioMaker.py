from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import functools

class ScenarioMaker(QDialog):
    def __init__(self, width, height):
        super().__init__()
        self.w = width
        self.h = height

    def Scenario(self, name, URL):
        layH = QHBoxLayout()
        layV = QVBoxLayout()
        link_label = QLabel() # 링크를 만들기 위한 코드
        explanation = QLabel() # 설명을 위한 코드
        submit_button = QPushButton("답안 제출") # 제출 버튼
        answer_input = QLineEdit() # 답안 입력란

        explainText = """<h1>ByteSight연습 시나리오에 오신 것을 환영합니다!</h1><br>아래 링크를 통해 연습 자료와 시나리오를 받아 파일 분석의 기초를 배워보세요!<br>
        <ul style="text-align:left;"><li>밑의 링크를 클릭하여 시나리오와 문제가 들어있는 zip파일을 다운받습니다.</li>
        <li>압축을 풀고 문제를 풀어서 나온 코드를 아래 입력창에 입력하고 결과를 봅니다.</li></ul>"""

        explanation.setText(explainText) # 설명
        explanation.setAlignment(Qt.AlignCenter)
        explanation.setStyleSheet("font-size: 18px; font-family: Arial; margin-bottom: 20px;")

        link_label.setText(f'<a href="{URL}">{name} Data</a>') # 파일 다운로드 링크
        link_label.setOpenExternalLinks(True) # 외부 링크 열기 활성화
        link_label.setStyleSheet("text-decoration: none; color: blue; font-size: 20px;")
        link_label.setAlignment(Qt.AlignCenter)
        
        submit_button.clicked.connect(functools.partial(self.AnsewerCheck, answer_input)) # 제출 버튼
        submit_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px 20px; border: none;")

        
        answer_input.setPlaceholderText("여기에 답을 입력하세요") # 답안 입력란
        answer_input.setStyleSheet("margin-top: 18px; padding: 10px; border: 1px solid #ccc;")

        layV.addWidget(explanation)
        layV.addWidget(link_label)
        layV.addWidget(answer_input)
        layV.addWidget(submit_button)

        layH.addStretch(1)
        layH.addLayout(layV)
        layH.addStretch(1)

        self.setWindowTitle(name) # 해당 윈도우의 제목
        self.setLayout(layH) # 레이아웃 추가
        self.setWindowModality(Qt.NonModal) # 해당 윈도우가 생성이 되고난 뒤에 다른 윈도우 창들과 상호작용이 가능한지에 대한 코드(현재 상호작용 가능함)
        self.setGeometry(300, 300, self.w, self.h) # 윈도우의 위치와 크기
        self.show()

    def AnsewerCheck(self, answer_input):
        answer = answer_input.text() # 답 가져오기
        print(answer)
        # 밑에 나머지 연산 처리할 것