from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QScrollArea, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class GuideWindow(QDialog):  # 가이드 창을 위한 클래스
    def __init__(self):
        super().__init__()
        self.MakeWindow()
    
    def MakeWindow(self):
        explainText = """<h1 style="text-align:center;font-weight : bold;">ByteSight에 오신 것을 환영합니다!</h1><hr>
        <div style="font-weight:bold; font-size:18px">&lt;소개&gt;</div><br>
        ByteSight는 파일/디스크 분석 프로그램으로 파일 속에 숨겨져있는 파일을 찾거나 훼손된 파일/디스크를 복구하는 데에 사용되는 분석 툴입니다.<br>
        해당 프로그램은 보안을 공부하고 싶어하는 초심자들을 위해 만들어진 프로그램입니다.<br>
        이곳에서 제공하는 각종 연습 시나리오들과 답지를 통해서 기초적인 파일 분석 방법에 대해 공부하고 익숙해지시길 바랍니다!<br>
        <div style="font-weight:bold; font-size:18px">&lt;사용방법&gt;</div><br>
        <img src="View/photo/Basic.png"/><br>
        본 프로그램은 위와 같이 3가지 버튼이 기본으로 구성되어 있습니다.
        <ol><li>파일 : 파일을 불러와 파일의 hex값을 직접 분석해볼 수 있으며 이를 활용하여 훼손된 파일 복구 및 숨겨진 파일 등을 추출할 수 있습니다.</li>
        <li>설정 : 글자 크기나 분석할때 도움이 되는 기능들에 대해 on/off를 할 수 있습니다.</li>
        <li>가이드라인 : 해당 프로그램의 전반적인 사용 방법과 파일 분석을 연습해볼 수 있는 시나리오 등을 제공합니다.</li></ol><br>
        <img src="View/photo/FileButton.png"/><br>
        파일메뉴를 조금 더 자세히 보자면 파일 불러오기, 저장하기, 다른 이름으로 저장과 같은 기본적인 파일 편집 기능을 제공합니다.<br>
        <img src="View/photo/GuideLineButton.png"/><br>
        가이드라인 메뉴를 조금 더 자세히 보자면 현재 보고 있는 창인 가이드 북 뿐만 아니라 초심자들을 위한 연습 문제 또한 제공합니다.<br>
        <br>
        저희 프로그램은 더 심도 있는 공부 환경을 제공하기 위해 커뮤니티를 만들었습니다.<br>
        더 많은 연습 문제와 질문을 통해 서로 정보를 주고 받고 싶으시다면 아래 링크를 클릭해주세요!<br>
        """
        
        explain = QLabel()  # 설명에 대한 객체
        explain.setText(explainText)
        explain.setStyleSheet("font-size: 15px; font-family: Arial; text-align : justify;")
        explain.setWordWrap(True)  # 텍스트 줄 바꿈 설정
        
        link_label = QLabel()  # 링크를 만들기 위한 코드
        link = "http://localhost:8080/"
        link_label.setText(f'<a href="{link}">ByteSight Community</a>')  # URL 생성
        link_label.setStyleSheet("font-size:20px;font-family: Arial;")
        link_label.setOpenExternalLinks(True)  # 외부 링크 열기 활성화
        
        layV = QVBoxLayout()
        layV.addWidget(explain)  # 설명 위젯 추가
        layV.addWidget(link_label)  # 레이아웃 안에 URL링크 위젯 추가
        
        content_widget = QWidget()
        content_widget.setLayout(layV)
        
        scroll_area = QScrollArea()
        scroll_area.setWidget(content_widget)
        scroll_area.setFixedSize(620, 400)  # 스크롤 영역의 크기를 고정
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        
        self.setWindowTitle("GuideBook")  # 해당 윈도우의 제목
        self.setWindowIcon(QIcon('View\\photo\\book.png')) # 아이콘 지정
        self.setLayout(main_layout)  # 레이아웃 추가
        self.setWindowModality(Qt.NonModal)  # 해당 윈도우가 생성이 되고난 뒤에 다른 윈도우 창들과 상호작용이 가능한지에 대한 코드(현재 상호작용 가능함)
        self.setGeometry(300, 300, 400, 350)  # 윈도우의 위치와 크기
        
    def ShowWindow(self):
        self.show()