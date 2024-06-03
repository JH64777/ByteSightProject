import sys
from PyQt5.QtWidgets import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Operation.FileManager import FileManager
import math

class Main(QWidget):
    def __init__(self):
        super().__init__()
        LD = FileManager("C:\\Users\\CS4_12\\Desktop\\진짜졸작\\Hello Test.txt")
        self.data, self.name = LD.ReadData()
        self.column = 16
        self.row = math.ceil(len(self.data) / self.column)
        
        self.main()

    def Make_Tab(self):
        tab = QWidget()
        vbox = QVBoxLayout()
        table = QTableWidget(self.row, self.column)
        # colName = []
        
        table.setShowGrid(False)
        # table.setVerticalHeaderLabels(["00000000", "00000010"])
        for k, v in self.data.items():
            table.setItem(0, k, QTableWidgetItem(v))
            table.resizeColumnToContents(k)

        table.setEditTriggers(QAbstractItemView.AllEditTriggers) # 모든 이벤트에(클릭, 더블클릭, 화살표키 등등) 편집이 가능하도록 자동으로 지정하는 것
        
        vbox.addWidget(table)
        
        tab.setLayout(vbox)
        return tab

    
    def main(self):
        tabs = QTabWidget()
        tabs.addTab(self.Make_Tab(), self.name)
        hbox = QHBoxLayout()
        hbox.addWidget(tabs)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 630, 600)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyGUI = Main()
    sys.exit(app.exec_())