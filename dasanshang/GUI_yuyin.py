import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from yuyin import (FILEPATH, my_record, get_audio, speech2text, getToken,HOST)
from translate import translate
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('语音识别及翻译')
        self.resize(600, 500)
        layout = QVBoxLayout()
        self.audio_button = QPushButton('录音', self)
        self.audio_button.clicked.connect(self.on_audio_clicked)
        self.speech2text_button = QPushButton('识别', self)
        self.speech2text_button.clicked.connect(self.on_speech2text_clicked)
        self.translate_button = QPushButton('翻译', self)
        self.translate_button.clicked.connect(self.on_translate_clicked)
        self.output_line_edit = QLineEdit(self)
        self.output_line_edit.setReadOnly(True)
        self.output_line_edit2 = QLineEdit(self)
        self.output_line_edit2.setReadOnly(True)
        layout.addWidget(self.audio_button)
        layout.addWidget(self.speech2text_button)
        layout.addWidget(self.output_line_edit)
        layout.addWidget(self.translate_button)
        layout.addWidget(self.output_line_edit2)
        self.setLayout(layout)
    def on_audio_clicked(self):
        my_record()
    def on_speech2text_clicked(self):
        self.speech2text_text = speech2text(get_audio(FILEPATH), getToken(HOST), 1537)
        self.output_line_edit.setText(self.speech2text_text)
    def on_translate_clicked(self):
        translated_text=translate(self.speech2text_text)
        self.output_line_edit2.setText(translated_text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())