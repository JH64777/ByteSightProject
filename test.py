import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QTabWidget, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit
from PyQt5.QtGui import QFont
from Operation.ChangedTextEdit import ChangedQTextEdit, ChangedQTextEdit2

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.masterTab = QTabWidget()
        self.monospaced_font = QFont("Courier", 12) # 글자 폰트, 크기 지정
        self.offsetList = QListWidget()
        self.makeoffset()
        self.initUI()
    
    def makeLabel(self, content):
        label = QLabel(content)
        label.setStyleSheet("color:blue;")
        label.setFont(self.monospaced_font) # 지정한 형식으로 글자 형태 설정
        return label
    
    def makeoffset(self):
        self.offsetList.setMaximumWidth(100)
        self.offsetList.setStyleSheet("border-style:none; color: blue;")
        self.offsetList.setFont(self.monospaced_font)
        self.addoffset(0)

    def addoffset(self, num):
        data = "00000000"
        self.offsetList.insertItem(num, data)

    
    def makeTab(self, name):
        tab = QWidget()
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()
        self.hexline = ChangedQTextEdit(self)
        self.textline = ChangedQTextEdit2(self)

        self.hexline.setStyleSheet("border-style:none;")
        self.textline.setStyleSheet("border-style:none;")

        self.hexline.setFont(self.monospaced_font)
        self.textline.setFont(self.monospaced_font)

        hbox.addLayout(grid)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(3)
        tab.setLayout(vbox)

        grid.addWidget(self.makeLabel("offset(h)"), 0, 0)
        grid.addWidget(self.makeLabel("00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F"), 0, 1)
        grid.addWidget(self.makeLabel("Decode text"), 0, 2)

        grid.addWidget(self.offsetList, 1, 0, 1, 0)
        grid.addWidget(self.hexline, 1, 1, 1, 2)
        grid.addWidget(self.textline, 1, 2, 1, 1)

        self.masterTab.addTab(tab, name)

    def initUI(self):
        vbox = QVBoxLayout()
        self.makeTab("test1")
        vbox.addWidget(self.masterTab)
        self.setLayout(vbox)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    
    def Notify(self):
        self.hexline
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

    