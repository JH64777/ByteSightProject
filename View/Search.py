from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt

class SearchWindow(QDialog):
    def __init__(self):
        super().__init__()

    def MakeWindow(self):
        self.setWindowTitle("Search")  # 윈도우의 제목 설정

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 검색 키워드 입력 레이블과 라인 에디트
        keyword_layout = QHBoxLayout()
        keyword_label = QLabel("검색 키워드")
        self.line_edit = QLineEdit()
        keyword_layout.addWidget(keyword_label)
        keyword_layout.addWidget(self.line_edit)

        # 검색 옵션 라디오 버튼
        self.frontRadio = QRadioButton("앞에서 부터")
        self.backRadio = QRadioButton("뒤에서 부터")
        self.allRadio = QRadioButton("전체에서")
        self.frontRadio.setChecked(True)  # 기본 선택

        # 라디오 버튼 그룹
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.frontRadio)
        radio_layout.addWidget(self.backRadio)
        radio_layout.addWidget(self.allRadio)

        # 라디오 버튼 그룹화 (단일 선택을 강제하기 위해 QButtonGroup 사용)
        self.radio_group = QButtonGroup()
        self.radio_group.addButton(self.frontRadio)
        self.radio_group.addButton(self.backRadio)
        self.radio_group.addButton(self.allRadio)

        # 검색 버튼
        search_button = QPushButton("검색")
        search_button.clicked.connect(self.SearchKeyword)  # 검색 버튼 클릭 시 호출할 함수 연결

        # 검색 버튼 레이아웃
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(search_button)

        # 메인 레이아웃에 모든 요소 추가
        layout.addLayout(keyword_layout)
        layout.addLayout(radio_layout)
        layout.addStretch(1)  # 여백 추가
        layout.addLayout(button_layout)

        # 메인 레이아웃을 다이얼로그에 설정
        self.setLayout(layout)

        # 창의 크기와 위치 설정
        self.setGeometry(300, 300, 400, 200)
        self.setWindowModality(Qt.NonModal)  # 비모달 설정
        self.show()  # 창을 화면에 표시

    def SearchKeyword(self):
        search_text = self.line_edit.text()
        search_mode = ""
        if self.frontRadio.isChecked():
            search_mode = "앞에서 부터"
        elif self.backRadio.isChecked():
            search_mode = "뒤에서 부터"
        elif self.allRadio.isChecked():
            search_mode = "전체에서"

        print(f"검색 키워드: {search_text}, 검색 모드: {search_mode}")