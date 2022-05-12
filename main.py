# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # hide window hint
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.menu = 0
        self.setting = 0
        self.max_normal_window = 0

        # menu bar show and hide
        self.uic.pushButton_4.clicked.connect(self.show_menu)

        # setting bar show and hide
        self.uic.frame_16.setMaximumSize(QtCore.QSize(0, 16777215))
        self.uic.pushButton_9.clicked.connect(self.show_setting)

        # stackWidget show screen
        self.uic.pushButton_5.clicked.connect(self.show_screen)
        self.uic.pushButton_6.clicked.connect(self.show_screen)
        self.uic.pushButton_7.clicked.connect(self.show_screen)
        self.uic.pushButton_8.clicked.connect(self.show_screen)

        # close window button
        self.uic.pushButton_3.clicked.connect(self.closeEvent)
        self.uic.pushButton_2.clicked.connect(self.Window_Restore)
        self.uic.pushButton.clicked.connect(lambda: self.showMinimized())
    #
    def show_menu(self):
        if self.menu == 0:
            self.uic.frame_9.setMaximumSize(QtCore.QSize(210, 16777215))
            self.menu = 1
        elif self.menu == 1:
            self.uic.frame_9.setMaximumSize(QtCore.QSize(40, 16777215))
            self.menu = 0

    def show_setting(self):
        if self.setting == 0:
            self.uic.frame_16.setMaximumSize(QtCore.QSize(150, 16777215))
            self.setting = 1
        elif self.setting == 1:
            self.uic.frame_16.setMaximumSize(QtCore.QSize(0, 16777215))
            self.setting = 0

    def show_screen(self):
        # take signal from button
        click_signal = self.sender()
        button_name = click_signal.objectName()
        # set current screen
        if button_name == "pushButton_5":
            self.uic.stackedWidget.setCurrentWidget(self.uic.page)
        elif button_name == "pushButton_6":
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
        elif button_name == "pushButton_7":
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_3)
        elif button_name == "pushButton_8":
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_4)

    def closeEvent(self, event):
        self.close()

    def Window_Restore(self):
        if self.max_normal_window == 0:
            self.showMaximized()
            self.max_normal_window = 1
        elif self.max_normal_window == 1:
            self.showNormal()
            self.max_normal_window = 0

    # move app
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.startPos = event.pos()

    def mouseMoveEvent(self, event):
        width = self.uic.frame.width()
        height = self.uic.frame.height()
        if self.startPos.x() <= width and self.startPos.y() <= height \
                and self.isFullScreen() == False:
            self.move(self.pos() + (event.pos() - self.startPos))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
