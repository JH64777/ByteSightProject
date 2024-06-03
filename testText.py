import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtCore import Qt

class HexEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hex Data Editor")
        
        self.text_edit = QTextEdit()
        self.text_edit.setAcceptRichText(False)
        self.text_edit.textChanged.connect(self.enforce_formatting)
        
        # 파일 열기 버튼
        open_button = QPushButton("Open File")
        open_button.clicked.connect(self.load_file)
        
        # 레이아웃 구성
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout()
        layout.addWidget(open_button)
        layout.addWidget(self.text_edit)
        central_widget.setLayout(layout)
        
    def load_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Hex Data File", "", "All Files (*);;Text Files (*.txt)", options=options)
        if file_name:
            with open(file_name, "r") as f:
                data = f.read()
                formatted_data = self.format_hex_data(data)
                self.text_edit.setPlainText(formatted_data)

    def format_hex_data(self, data):
        # 문자열을 두 글자 단위로 나누고 빈 칸으로 구분
        hex_pairs = re.findall(r'\w{2}', data)  # 두 글자 단위로 자르기
        formatted_text = ' '.join(hex_pairs)   # 공백으로 구분
        return formatted_text

    def enforce_formatting(self):
        # 사용자가 편집 중 공백이 사라지지 않도록 보장
        cursor = self.text_edit.textCursor()
        current_text = self.text_edit.toPlainText()
        formatted_text = self.format_hex_data(current_text.replace(" ", ""))  # 공백 제거 후 다시 포맷팅
        self.text_edit.blockSignals(True)  # 무한 루프 방지
        self.text_edit.setPlainText(formatted_text)
        self.text_edit.setTextCursor(cursor)  # 커서 위치 복원
        self.text_edit.blockSignals(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = HexEditor()
    editor.show()
    sys.exit(app.exec_())