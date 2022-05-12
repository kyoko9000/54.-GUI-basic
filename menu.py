# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from gui2 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.popup = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.menu = QMenu()
        self.uic.pushButton.setMenu(self.menu)
        self.menu.triggered.connect(lambda x: self.receive_data(x))

        menu_action1 = self.menu.addMenu("hello")
        menu_action1.addAction("hello 1")
        menu_action1.addAction("hello 2")
        # menu_action1.addAction('hello 1', self.Action1)
        # menu_action1.addAction('hello 2', self.Action2)

        menu_action2 = self.menu.addMenu("list")
        menu_action2.addAction("list 1")
        menu_action2.addAction("list 2")
        # menu_action2.addAction('list 1', self.Action1)
        # menu_action2.addAction('list 2', self.Action2)

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         width = self.uic.frame_2.width()
    #         height = self.uic.frame_2.height()
    #         Pos = event.pos()
    #         frame_pos = self.uic.frame_2.pos()
    #         if frame_pos.x() < Pos.x() < (frame_pos.x() + width) and \
    #                 frame_pos.y() < Pos.y() < (frame_pos.y() + height):
    #             self.popup = self.menu.popup(self.mapToGlobal(QPoint(frame_pos.x() + width, frame_pos.y() - 50)))
    #             # self.menu.exec_(frame_pos)

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
