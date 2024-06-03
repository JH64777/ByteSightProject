# Status, MenuBar, Tab이 모두 조합이 되어 하나의 메인창을 만드는 구조

import sys
from ParentView import ParentView
from PyQt5.QtWidgets import QApplication
from MenuBar import MenuBar

class Main(ParentView): 
    def __init__(self):
        super().__init__()
    
    def ShowWindow(self):
        self.setGeometry(300, 300, 630, 600)
        self.show()

############################################ 밑에서 부터는 실행 코드

app = QApplication(sys.argv)
main = Main()
menu = MenuBar(main)
main.ShowWindow()
sys.exit(app.exec_())