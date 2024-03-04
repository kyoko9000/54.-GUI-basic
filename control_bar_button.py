# ************************** man hinh loai 2 *************************
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from gui1 import Ui_MainWindow


class PreviewWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(703, 291)

        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        closeButton = QPushButton("&Close")
        closeButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(closeButton)
        self.setLayout(layout)

        self.setWindowTitle("Preview")

    def setWindowFlags(self, flags):
        super().setWindowFlags(flags)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flags = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # add button
        self.button = QPushButton(self.uic.centralwidget)
        self.button.setText("hide")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button.setFont(font)
        self.button.setGeometry(QtCore.QRect(50, 100, 211, 70))
        self.button.clicked.connect(self.hide_hint)

        self.button1 = QPushButton(self.uic.centralwidget)
        self.button1.setText("show")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.button1.setFont(font)
        self.button1.setGeometry(QtCore.QRect(350, 100, 211, 70))
        self.button1.clicked.connect(self.show_hint)

        self.previewWindow = PreviewWindow()
        pos = self.previewWindow.pos()
        pos.setX(110)
        pos.setY(110)
        self.previewWindow.move(pos)
        self.previewWindow.show()

    def hide_hint(self):
        self.flags = Qt.FramelessWindowHint
        self.updatePreview()

    def show_hint(self):
        self.flags = Qt.Window
        self.updatePreview()

    def updatePreview(self):
        self.previewWindow.setWindowFlags(self.flags)
        pos = self.previewWindow.pos()
        if pos.x() < 0:
            pos.setX(0)
        if pos.y() < 0:
            pos.setY(0)
        self.previewWindow.move(pos)
        self.previewWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
