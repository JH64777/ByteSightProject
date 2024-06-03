from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.MenuBar()

    def MenuBar(self):
        FileMenu = QAction(QIcon(None), '파일')
        OptionMenu = QAction(QIcon(None), '설정')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menubar.addMenu('파일') # 메
        menubar.addMenu('설정')

        
        self.setGeometry(300, 300, 300, 200)
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())