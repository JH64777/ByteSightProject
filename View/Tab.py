import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Operation.ChangedTextEdit import ChangedQTextEdit
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class TabGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.masterTab = QTabWidget()
        self.openedFiles = [] # 동일한 파일을 열지 않게 하기 위한 파일 리스트
        self.tabobj = {} # 후에 저장을 위한 dict {name:obj}
        self.resize(680, 1000)
        self.masterTab.setContextMenuPolicy(Qt.CustomContextMenu)
        self.masterTab.tabBar().setContextMenuPolicy(Qt.CustomContextMenu)  # TabBar에만 컨텍스트 메뉴 설정
        self.masterTab.tabBar().customContextMenuRequested.connect(self.RemoveTab)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.masterTab)
        self.setLayout(self.vbox)


    def AddTab(self, name, tab):
        vbox = QVBoxLayout()
        # for name, contents in self.tabinfo.items(): # 지금까지 연 파일들을 하나의 텝으로 다 볼 수 있게 해주는 기능
        self.masterTab.addTab(tab, name)
        vbox.addWidget(self.masterTab)
        self.setLayout(vbox)

    def CreateTab(self, path, data): # 텝을 생성하고 tabinfo에 저장하는 기능
        # 여기다가 데이터 로드해서 테이블 만드는 것 하면 될듯
        tab = QWidget()
        vbox = QVBoxLayout() # 글을 수정할 수 있는 영역을 적용시키기 위해서 사용하는 공간
        tabmain = ChangedQTextEdit() # 글을 직접 수정하는 공간 (기존의 QTextEdit을 상속받아 내 방식대로 수정한 것)
        name = path.split("//")[-1]
        
        monospaced_font = QFont("Courier", 12) # 글자 폰트, 크기 지정
        tabmain.setFont(monospaced_font) # 지정한 형식으로 글자 형태 설정
        
        for i in data:
            tabmain.append(i)

        self.tabobj[name] = tabmain

        vbox.addWidget(tabmain)
        tab.setLayout(vbox)

        self.openedFiles.append(path)
        self.AddTab(name, tab)

    def GetData(self):
        tabidx = self.masterTab.currentIndex() # 선택된 탭의 번호를 가져온다.
        tabTitle = self.masterTab.tabText(tabidx) # 선택된 탭의 제목을 가져온다.
        return self.tabobj[tabTitle].GetAllData()
    
    def RemoveTab(self):
        selectedTab = self.masterTab.currentIndex()
        print(self.masterTab.tabText(selectedTab))
        self.openedFiles.pop(selectedTab) # 열린 파일 리스트에서 제거
        self.tabobj.pop(self.masterTab.tabText(selectedTab))
        self.masterTab.removeTab(selectedTab)



# 현재 문제점으로는 Tab의 크기를 마음대로 조절하지 못한다는 점이다.
# 그리고 QMainWindow의 SetCentralWidget형식에서 어떻게 Layout이 설정이 되는지 알 수 없다는 점이다.
# 오늘은 2024-04-20이다.