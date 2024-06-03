from PyQt5.QtWidgets import QMainWindow

class ParentView(QMainWindow): # 모든 View의 부모 클래스(추상클래스) 이유는 라이브러리 한 번만 로드 하기 위해 해당 구조 채택
    def __init__(self):
        super().__init__()