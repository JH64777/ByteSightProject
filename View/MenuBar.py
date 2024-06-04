import sys, os
import functools
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from GuideWindow import GuideWindow
from Operation.FileManager import FileManager
from ParentView import ParentView
from PyQt5.QtWidgets import QAction, QFileDialog
from PyQt5.QtGui import QIcon
from Tab import TabGenerator
from ScenarioMaker import ScenarioFactory


class MenuBar(ParentView):
    def __init__(self, instance): # 인스턴스를 받음으로 Main에서 메뉴바를 생성할 수 있게끔 설정
        super().__init__()
        self.instance = instance
        self.guidewin = GuideWindow() # 가이드 창을 생성하기 위한 인스턴스
        self.tabmaker = TabGenerator()
        self.path = None
        self.scenario = ScenarioFactory(600, 580)
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
        scenario1.triggered.connect(functools.partial(self.scenario.Scenario, "Scenario1", "https://www.google.com"))
        scenario2.triggered.connect(functools.partial(self.scenario.Scenario, "Scenario2", "https://www.google.com"))
        

        menubar = self.instance.menuBar() # 메뉴바에 대한 객체 생성
        menubar.setNativeMenuBar(False) # 기본으로 PyQt에서 제공하는 메뉴바 사용 안함(사용자 지정으로 사용할 것임을 의미)
        
        filemenu = menubar.addMenu('파일') # 메뉴바 파일 버튼 생성
        filemenu.addAction(loadFile) # 파일 불러오기 액션 추가
        filemenu.addAction(saveFile) # 파일 저장 액션 추가
        filemenu.addAction(saveasFile) # 파일 다른 이름으로 저장

        menubar.addMenu('설정') # 메뉴바 설정 버튼 생성
        
        guide = menubar.addMenu('가이드라인') # 메뉴바 가이드라인 버튼 생성
        guide.addAction(bringGuide) # 가이드 북 액션 추가
        guide.addAction(scenario1) # 가이드 시나리오1 추가
        guide.addAction(scenario2) # 가이드 시나리오2 추가
    
    def OpenFile(self): # 파일 찾기 코드
        fname = QFileDialog.getOpenFileName(self.instance) # 파일 탐색기를 통해 파일을 선택할 수 있게 하는 코드

        if fname[0]: # 파일 경로가 선택되었다면 안되면 그냥 넘어감
            self.path = fname[0].replace("/", "//") # 경로
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
