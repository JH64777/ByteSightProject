from PyQt5.QtGui import QKeyEvent, QTextCursor, QTextBlockFormat, QTextCharFormat
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt

class ChangedQTextEdit(QTextEdit): # QTextEdit를 수정한 버전 (기존 글쓰는 위젯에 Key 이벤트, 글자 사이의 간격 등을 수정한 것)
    def __init__(self):
        super().__init__()
        self.allowedEdittingKey = (Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_Backspace) # 파일 편집 시 허용된 글자
        self.insertCharCount = 0 # 입력되는 글자 숫자를 세어주는 변수
        self.char_format = QTextCharFormat() # 문자를 꾸미는 기능을 위해 객체 생성
        self.setLineSpacing(150) # 줄 간격의 크기 1.5배
        # self.limitcharcount = 47 # 한 줄에 사용 가능한 글자 수

    def GetAllData(self): # 데이터 반환
        return self.toPlainText()

    def setLineSpacing(self, spacing_percent): # 현재 문서의 모든 블록에 대해 줄 간격 설정 메서드
        cursor = self.textCursor() # 줄 간격의 범위를 정하고 적용하기 위해 커서 객체 생성
        cursor.select(QTextCursor.Document) # 문서 전체를 선택
        block_format = QTextBlockFormat() # 줄 간격을 설정하기 위해 생성하는 객체
        block_format.setLineHeight(spacing_percent, QTextBlockFormat.ProportionalHeight) # 위와 아래 글자간 간격 설정(백분율 단위로)
        cursor.setBlockFormat(block_format) # 설정한 값 적용
    
    def ChangeTextColor(self, color): # 색 지정 메서드
        self.char_format.setForeground(color)

    def keyPressEvent(self, e: QKeyEvent | None) -> None: # 키보드 입력 시 호출되는 메서드
        cursor = self.textCursor() # 커서 객체 생성
        # lineLeng = len(cursor.block().text()) # 한 줄에 있는 글자들의 갯수

        
        if e.key() in self.allowedEdittingKey: # 편집 시 사용 가능한 키 제한
            # if lineLeng >= self.limitcharcount and e.key() != Qt.Key_Backspace: # 해당 줄이 한개점을 도달하되 BackSpace가 눌리지 않았을 시 검사
            #     cursor.movePosition(QTextCursor.NextBlock) # 다음 줄로 커서 설정
            #     cursor.movePosition(QTextCursor.StartOfBlock) # 다음 줄의 처음 부분으로 설정
            #     self.setTextCursor(cursor) # 설정 값 적용

            if e.text().isalpha(): # 입력된 값이 알파벳인가?
                e = QKeyEvent(e.type(), e.key(), e.modifiers(), e.text().upper()) # e변수에 대문자로 변경한 QKeyEvent객체 대입
            
        elif e.key() in (Qt.Key_Right, Qt.Key_Left, Qt.Key_Up, Qt.Key_Down): # 왼쪽 혹은 오른쪽 화살표키가 눌렸는가?
            if e.key() == Qt.Key_Left: # 왼쪽 화살표키가 눌렀는가?
                cursor.movePosition(QTextCursor.PreviousWord, QTextCursor.KeepAnchor) # 단어 단위로 커서 이동
                self.setTextCursor(cursor) # 커서 위치 지정
            elif e.key() == Qt.Key_Right: # 오른쪽 화살표키가 눌렸는가?
                cursor.movePosition(QTextCursor.NextWord, QTextCursor.KeepAnchor) # 단어 단위로 커서 이동
                self.setTextCursor(cursor) # 커서 위치 지정
            else: # 나머지 방향
                pass
        
        elif e.modifiers() == Qt.ControlModifier:  # Ctrl 키 조합(Ctrl + C, V 등등). (해당 부분만 정의를 해 놓으면 Ctrl과 조합해서 쓰는 기능이 적절하게 잘 작동함)
            pass

        else: # 나머지 경우
            e.ignore() # 키 무시
            return None # 조기 종료
            
        return super().keyPressEvent(e) # 원래 방식대로 동작하게끔 지정