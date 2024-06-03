from PyQt5.QtWidgets import QTextEdit, QApplication
from PyQt5.QtGui import QTextCharFormat, QTextCursor
import sys

class ChangedQTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

    def setLetterSpacingForSelection(self, start, end, spacing):
        cursor = self.textCursor()  # 현재 커서 위치 가져오기
        cursor.setPosition(start)  # 시작 위치로 커서 이동
        cursor.setPosition(end, QTextCursor.KeepAnchor)  # 끝 위치까지 텍스트 선택
        format = QTextCharFormat()  # 문자 포맷 객체 생성
        format.setFontLetterSpacing(spacing)  # 글자 사이의 자간 설정
        cursor.setCharFormat(format)  # 선택된 텍스트에 포맷 적용

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ChangedQTextEdit()
    editor.setText("Hello World")  # 텍스트 설정
    editor.setLetterSpacingForSelection(6, 11, 200)  # "World" 부분의 글자 사이의 자간을 2로 설정
    editor.show()
    sys.exit(app.exec_())