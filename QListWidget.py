# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget, QProxyStyle, QStyle

from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entry = []
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.listWidget.setSpacing(5)
        self.uic.listWidget.setStyleSheet("""
            QListWidget {
                background:rgb(255, 255, 255);
                color: rgb(0,255,0);
                border-radius: 10px;
                padding: 12px 0px 0px 1px;
                font-size: 30px;
            }
            QListWidget::item {
                background:rgb(40, 46, 66);
                color: rgb(0,255,0);
                border-radius: 10px;
                padding: 12px 0px 0px 1px;
            }
        """)
        # data
        lists = [["sdf", "sdfa", "asdfsadf"],
                 ["12312", "1231231", "5645645"],
                 ["qqqqqqq", "ggggg", "asdfsadf"]]

        pics = [["pics/anh dep.jpg"],
                ["icons/cil-arrow-bottom.png"],
                ["pics/gai-xinh.jpg"]]

        for list, pic in zip(lists, pics):
            self.newItem = QListWidgetItem()
            self.newItem.setText(" {} \n {} \n {}".format(list[0], list[1], list[2]))
            self.newItem.setIcon(QIcon(pic[0]))
            self.newItem.setCheckState(Qt.CheckState.Unchecked)

            self.uic.listWidget.addItem(self.newItem)
            self.uic.listWidget.setIconSize(QSize(100, 100))
        self.uic.listWidget.insertItem(2, "self.newItem")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
