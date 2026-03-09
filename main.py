import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import makeSpam

#Ui파일 가져오기
form_class = uic.loadUiType(".\\ui\\Spammer1_1.ui")[0]

#Ui Class 선언
class WindowClass(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #PyQt 시그널 vvvvvvvvvv
        self.inputText_button.clicked.connect(self.generateButtonFunction)
        self.inputText_lineEdit.returnPressed.connect(self.generateButtonFunction)
        self.copyToClipboard_button.clicked.connect(self.copyToClipboard)

    #PyQt 메서드 vvvvvvvvvv
    def generateButtonFunction(self):
        input_string = self.inputText_lineEdit.text()
        input_breaklineThreshold = self.inputText_brThreshold.value()
        input_breaklineSensitivity = self.inputText_brSensitivity.value()
        input_maxRow = self.inputText_maxRow.value()
        input_usage = self.inputText_usage.currentText()
        if input_string == "":
            return

        string = makeSpam.make_spam_string(
            input_string,
            input_breaklineThreshold,
            input_breaklineSensitivity,
            input_maxRow,
            input_usage
        )
        self.outputText_plain.setPlainText(string)
        self.outputText_markdown.setMarkdown(string)

    def copyToClipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.outputText_plain.toPlainText())





if __name__ == "__main__":
    #프로그램을 실행시켜 주는 클래스
    app = QApplication(sys.argv)

    #WindowClass 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면 띄우기
    myWindow.show()

    #프로그램을 이벤트루프로 진입
    app.exec()









