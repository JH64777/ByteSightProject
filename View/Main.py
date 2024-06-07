# Status, MenuBar, Tab이 모두 조합이 되어 하나의 메인창을 만드는 구조

import sys
from ParentView import ParentView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from MenuBar import MenuBar
from GuideWindow import GuideWindow

class Main(ParentView):
    def __init__(self):
        super().__init__()
        self.firstguide = GuideWindow()
    
    def ShowWindow(self):
        self.setWindowIcon(QIcon('View\\photo\\Blogo.png'))
        self.setWindowTitle("ByteSight")
        self.setGeometry(300, 300, 630, 600)
        self.show()
        self.firstguide.ShowWindow()
        # Enable high DPI scaling

############################################ 밑에서 부터는 실행 코드

app = QApplication(sys.argv)
main = Main()
menu = MenuBar(main)
main.ShowWindow()
sys.exit(app.exec_())