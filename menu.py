# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from gui2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.popup = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.menu = QMenu()
        self.menu.setStyleSheet("QMenu { \n""background-color: rgb(0, 255, 0);\n""border-radius: 20px;\n""}")
        self.uic.pushButton.setMenu(self.menu)
        self.menu.triggered.connect(lambda x: self.receive_data(x))

        self.menu.addSeparator()

        menu_1 = self.menu.addMenu("hello")
        self.menu.addSeparator()
        menu_1.setIcon(QIcon("icons/cil-4k.png"))
        menu_1.setStyleSheet("background-color: rgb(104, 104, 104)")

        button_action_1 = QAction(QIcon("icons/cil-3d.png"), "hello 1", self)
        menu_1.addAction(button_action_1)
        # menu_1.addAction("hello 1")

        menu_1.addSeparator()

        button_action_2 = QAction(QIcon("icons/cil-arrow-circle-top.png"), "hello 2", self)
        menu_1.addAction(button_action_2)
        # menu_1.addAction('hello 1', self.Action1)
        # menu_1.addAction('hello 2', self.Action2)

        menu_2 = self.menu.addMenu("list")
        menu_2.setIcon(QIcon("icons/cil-voice-over-record.png"))
        menu_2.setStyleSheet("background-color: rgb(4, 40, 104)")
        button_action_3 = QAction(QIcon("icons/cil-wifi-signal-off.png"), "list 1", self)
        menu_2.addAction(button_action_3)
        # menu_2.addAction("list 1")

        menu_2.addSeparator()

        button_action_4 = QAction(QIcon("icons/cil-x-circle.png"), "list 2", self)
        font = QtGui.QFont()
        font.setPointSize(20)
        button_action_4.setFont(font)
        menu_2.addAction(button_action_4)
        # menu_2.addAction("list 2")
        # menu_2.addAction('list 1', self.Action1)
        # menu_2.addAction('list 2', self.Action2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            width = self.uic.frame_2.width()
            height = self.uic.frame_2.height()
            Pos = event.pos()
            frame_pos = self.uic.frame_2.pos()
            if frame_pos.x() < Pos.x() < (frame_pos.x() + width) and \
                    frame_pos.y() < Pos.y() < (frame_pos.y() + height):
                self.popup = self.menu.popup(self.mapToGlobal(QPoint(frame_pos.x() + width - 10, frame_pos.y() - 70)))
                # self.menu.exec_(frame_pos)
            else:
                self.uic.frame_2.setStyleSheet("background-color: rgb(104, 104, 104)")

    def receive_data(self, x):
        self.uic.frame_2.setStyleSheet("background-color: rgb(104, 104, 104)")
        if x.text() == "hello 1":
            print("hello 1")
        elif x.text() == "hello 2":
            print("hello 2")
        elif x.text() == "list 1":
            print("list 1")
        elif x.text() == "list 2":
            print("list 2")

    # def Action1(self):
    #     print('You selected hello 1')
    #
    # def Action2(self):
    #     print('You selected hello 2')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
