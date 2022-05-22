# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QProxyStyle, QStyle
from gui2 import Ui_MainWindow


# make icon bigger
class MyProxyStyle(QProxyStyle):
    pass

    def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

        if QStyle_PixelMetric == QStyle.PM_SmallIconSize:
            return 25
        else:
            return QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.popup = None
        self.uic.pushButton.clicked.connect(self.run_menu)
        # setup menu
        self.menu = QMenu()
        # set frameless menu
        self.menu.setWindowFlag(Qt.FramelessWindowHint)
        self.menu.setAttribute(Qt.WA_TranslucentBackground)
        self.menu.setWindowOpacity(0.6)

        #  set menu style
        self.menu.setStyleSheet("""
            QMenu{
                background:rgb(40, 46, 66);
                color: rgb(0,255,0);
                border-radius: 10px;
                padding: 12px 0px 0px 1px;
            }
            QMenu::item {
                background-color: transparent;
                font-size: 25px;
                padding: 12px 80px 5px 20px;
            }
            QMenu::item:selected {
                background-color: gray;
            }
            QMenu::icon {
                padding-left: 20px;
            }
        """)

        # add menu to button
        # self.uic.pushButton.setMenu(self.menu)
        # take signal from QMenu
        self.menu.triggered.connect(lambda x: self.receive_data(x))
        #
        #     #     # add menu name hello
        self.menu_1 = self.menu.addMenu("hello")
        self.menu_1.setIcon(QIcon("icons/cil-4k.png"))
        # self.menu.addSeparator()
        #     #     # menu_1.setStyleSheet("background-color: rgb(104, 104, 104)")
        #
        #     #     # add action "hello 1" to menu name "hello"
        button_action_1 = QAction(QIcon("icons/cil-3d.png"), "hello 1", self)
        self.menu_1.addAction(button_action_1)
        #     self.menu_1.addAction("hello 1")
        #
        self.menu_1.addSeparator()
        #
        #     #     # add action "hello 2" to menu name "hello"
        button_action_2 = QAction(QIcon("icons/cil-arrow-circle-top.png"), "hello 2", self)
        self.menu_1.addAction(button_action_2)
        # self.menu_1.addAction('hello 1', self.Action1)
        # self.menu_1.addAction('hello 2', self.Action2)
        #
        #     #     # add memu name "list"
        menu_2 = self.menu.addMenu("list")
        menu_2.setIcon(QIcon("icons/cil-voice-over-record.png"))
        #     #
        #     # add "list 1" to menu name "list"
        button_action_3 = QAction(QIcon("icons/cil-wifi-signal-off.png"), "list 1", self)
        menu_2.addAction(button_action_3)
        #     # menu_2.addAction("list 1")
        #
        menu_2.addSeparator()
        #
        #     # add "list 2" to menu "list"
        button_action_4 = QAction(QIcon("icons/cil-x-circle.png"), "list 2", self)
        font = QtGui.QFont()
        font.setPointSize(20)
        button_action_4.setFont(font)
        menu_2.addAction(button_action_4)

    #
    # #     # menu_2.addAction("list 2")
    # #     # menu_2.addAction('list 1', self.Action1)
    # #     # menu_2.addAction('list 2', self.Action2)
    #
    def run_menu(self):
        frame_pos_1 = self.uic.frame.pos()
        # width = self.uic.frame.width()
        self.menu.popup(self.mapToGlobal(QPoint(frame_pos_1.x() + 20, frame_pos_1.y() - 100)))

    #
    # receive signal form QAction of QMenu
    def receive_data(self, x):
        # repaint frame_2
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


# make command out of gui
CSS = """
QMenu {
    background: rgba(98, 98, 98, 255);
    padding-top: 10px;
    }
QMenu::item{
    padding-top: 4px;
    padding-left: 15px;
    padding-right: 15px;
    padding-bottom: 4px;
    margin-left: 10px;
    }
QMenu::item:selected {
    background: rgba(0, 0, 0, 40);
    }"
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # app.setStyleSheet(CSS)

    # icon size of QMenu
    myStyle = MyProxyStyle('Fusion')
    app.setStyle(myStyle)

    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
