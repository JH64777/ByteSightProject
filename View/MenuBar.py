import sys, os
import functools
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from GuideWindow import GuideWindow
from Operation.FileManager import FileManager
from ParentView import ParentView
from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtGui import QIcon
from Tab import TabGenerator
from ScenarioMaker import ScenarioMaker
from Search import SearchWindow

class MenuBar(ParentView):
    def __init__(self, instance): # 인스턴스를 받음으로 Main에서 메뉴바를 생성할 수 있게끔 설정
        super().__init__()
        self.instance = instance
        self.guidewin = GuideWindow() # 가이드 창을 생성하기 위한 인스턴스
        self.tabmaker = TabGenerator()
        self.search = SearchWindow()
        self.path = None
        self.scenario = None
        self.CreateMenuBar()
    
    def CreateMenuBar(self):
        
        loadFile = QAction(QIcon(None), "파일 불러오기", self.instance) # 파일 불러오기 항목
        loadFile.triggered.connect(self.OpenFile) # 해당 항목이 선택될 시 OpenFile 호출
        saveFile = QAction(QIcon(None), "파일 저장", self.instance)
        saveFile.triggered.connect(self.Save) # 해당 항목이 선택될 시 Save호출
        saveasFile = QAction(QIcon(None), "다른 이름으로 저장", self.instance)
        saveasFile.triggered.connect(self.SaveAs) # 해당 항목이 선택될 시 Save호출

        bringGuide = QAction(QIcon(None), "가이드 북", self.instance) # 가이드 북 창 열기
        scenario1 = QAction(QIcon(None), "연습용 시나리오1", self.instance) # 연습 시나리오 창 1
        scenario2 = QAction(QIcon(None), "연습용 시나리오2", self.instance) # 연습 시나리오 창 2
        bringGuide.triggered.connect(self.BringGuide) # 해당 항목 선택될 시 Bring Guide 호출
        scenario1.triggered.connect(functools.partial(self.BringScenario, 1))
        scenario2.triggered.connect(functools.partial(self.BringScenario, 2))

        searchFunc = QAction(QIcon(None), "검색", self.instance) # 검색하는 버튼 생성
        searchFunc.triggered.connect(self.Search) # 검색 하는 함수와 연결

        menubar = self.instance.menuBar() # 메뉴바에 대한 객체 생성
        menubar.setNativeMenuBar(False) # 기본으로 PyQt에서 제공하는 메뉴바 사용 안함(사용자 지정으로 사용할 것임을 의미)
        
        filemenu = menubar.addMenu('파일') # 메뉴바 파일 버튼 생성
        filemenu.addAction(loadFile) # 파일 불러오기 액션 추가
        filemenu.addAction(saveFile) # 파일 저장 액션 추가
        filemenu.addAction(saveasFile) # 파일 다른 이름으로 저장
        
        guide = menubar.addMenu('가이드라인') # 메뉴바 가이드라인 버튼 생성
        guide.addAction(bringGuide) # 가이드 북 액션 추가
        guide.addAction(scenario1) # 가이드 시나리오1 추가
        guide.addAction(scenario2) # 가이드 시나리오2 추가

        menubar.addAction(searchFunc) # 메뉴바에 버튼 적용

    def OpenFile(self): # 파일 찾기 코드
        fname = QFileDialog.getOpenFileName(self.instance) # 파일 탐색기를 통해 파일을 선택할 수 있게 하는 코드
        self.path = fname[0].replace("/", "//") # 경로
        if fname[0] and self.path not in self.tabmaker.openedFiles: # 파일 경로가 선택되고 동일한 파일이 열려있지 않다면 실행함
            self.fileManager = FileManager(self.path)
            data, name = self.fileManager.ReadData() # hex데이터, 파일 이름
            self.tabmaker.CreateTab(name, data) # 텝 생성
            self.instance.setCentralWidget(self.tabmaker)

    
    def Save(self): # 파일 저장
        if self.path != None: # 기존에 존재하는 파일을 새롭게 저장하고자 한다면.
            newData = self.tabmaker.GetData() # 현재까지 작업한 파일 데이터 가져오기
            self.fileManager.SaveData(newData, None) # 파일 저장
        else: # 완전히 새로운 파일을 저장하는 경우
            self.SaveAs()

    def SaveAs(self): # 파일 다른 이름으로 저장
        try:
            newData = self.tabmaker.GetData() # 현재까지 작업한 파일 데이터 가져오기
            fname = QFileDialog.getSaveFileName(self, "Save File", "", "All Files (*)") # GUI형식으로 파일 저장
            self.fileManager.SaveData(newData, fname[0]) # 파일 최신 데이터랑 저장 경로
        except Exception as e: # 파일을 열지도 않고 저장할 시
            print("여기다가 에러 표시창 만들 것")
    
    def BringGuide(self): # 가이드 창 가져오기
        self.guidewin.ShowWindow() # 창 열기

    def BringScenario(self, num):
        self.scenario = ScenarioMaker(600, 580)
        match num:
            case 1:
                self.scenario.Scenario("Scenario1", "http://localhost:8080/scenario/1")
            case 2:
                self.scenario.Scenario("Scenario2", "http://localhost:8080/scenario/2")
            case _:
                pass
    
    def Search(self):
        self.search.MakeWindow()