# ************************** man hinh loai 2 *************************
import sys
import numpy
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem


from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.list_of_tuples_item_widget = []
        self.entry = []
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.listWidget.setSpacing(1)
        self.uic.listWidget.setStyleSheet("""
            QListWidget {
                background:rgb(255, 255, 255);
                color: rgb(0,255,0);
                border-radius: 5px;
                padding: 12px 0px 0px 1px;
                font-size: 30px;
            }
            QListWidget::item {
                background:rgb(40, 46, 66);
                color: rgb(0,255,0);
                border-radius: 5px;
                padding: 5px 0px 5px 1px;
            }
            QListWidget::item::hover {
                background:rgb(0, 0, 255);
            }
        """)
        # data
        lists = [["linda", "address 0", "road 0"],
                 ["maria", "address 1", "road 1"],
                 ["eva", "address 2", "road 2"]]

        pics = [["pics/1-162018936.jpg"],
                ["pics/girl-xinh-1-480x600.jpg"],
                ["pics/gai-xinh.jpg"]]

        self.count = -1
        for list, pic in zip(lists, pics):
            self.count += 1
            self.newItem = QListWidgetItem("item {}".format(self.count))
            self.newItem.setSizeHint(QSize(0, 150))
            # self.newItem.setText(" {} \n {} \n {}".format(list[0], list[1], list[2]))
            # self.newItem.setIcon(QIcon(pic[0]))
            # self.newItem.setCheckState(Qt.CheckState.Unchecked)

            self.frame = QtWidgets.QFrame()
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_2.setSpacing(0)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.frame_3 = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
            self.frame_3.setSizePolicy(sizePolicy)
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
            self.horizontalLayout_5.setSpacing(0)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.frame_4 = QtWidgets.QFrame(self.frame_3)
            self.frame_4.setStyleSheet("")
            self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
            self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
            self.horizontalLayout_3.setSpacing(0)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_2 = QtWidgets.QLabel(self.frame_4)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
            self.label_2.setSizePolicy(sizePolicy)
            self.label_2.setMinimumSize(QtCore.QSize(0, 0))
            self.label_2.setMaximumSize(QtCore.QSize(100, 100))
            self.label_2.setStyleSheet("")
            self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
            self.label_2.setText("")

            url_image = pic[0]

            source = QtGui.QImage(url_image)
            self.resize(source.width(), source.height())

            output = QtGui.QPixmap(source.width(), source.height())
            output.fill(QtCore.Qt.transparent)

            qp = QtGui.QPainter(output)
            clipPath = QtGui.QPainterPath()
            clipPath.addRoundedRect(QtCore.QRectF(source.rect()), source.width() // 2, source.width() // 2)
            qp.setClipPath(clipPath)
            qp.drawPixmap(0, 0, QtGui.QPixmap(source))
            qp.end()

            self.label_2.setPixmap(output)
            self.label_2.setScaledContents(True)
            self.label_2.setObjectName("label_2")
            self.horizontalLayout_3.addWidget(self.label_2)
            self.horizontalLayout_5.addWidget(self.frame_4)
            self.frame_5 = QtWidgets.QFrame(self.frame_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
            self.frame_5.setSizePolicy(sizePolicy)
            self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_5.setObjectName("frame_5")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
            self.horizontalLayout_6.setContentsMargins(20, 0, 0, 0)
            self.horizontalLayout_6.setSpacing(0)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.label = QtWidgets.QLabel(self.frame_5)
            font = QtGui.QFont()
            font.setPointSize(20)
            self.label.setFont(font)
            self.label.setStyleSheet("color: rgb(255, 255, 255);")
            self.label.setText(" {} \n {} \n {}".format(list[0], list[1], list[2]))
            self.label.setObjectName("label")
            self.horizontalLayout_6.addWidget(self.label)
            self.horizontalLayout_5.addWidget(self.frame_5)
            self.horizontalLayout_2.addWidget(self.frame_3)
            self.frame_2 = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
            self.frame_2.setSizePolicy(sizePolicy)
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
            self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
            self.horizontalLayout_4.setSpacing(0)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.pushButton = QtWidgets.QPushButton(self.frame_2)
            self.pushButton.setStyleSheet("QPushButton {\n"
                                          "border: none;\n"
                                          "}\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(255, 0, 0);\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: rgb(0, 20, 163);     \n"
                                          "}")
            self.pushButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("icons/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton.setIcon(icon)
            self.pushButton.setIconSize(QtCore.QSize(25, 25))
            self.pushButton.setObjectName("pushButton_{}".format(self.count))
            self.horizontalLayout_4.addWidget(self.pushButton)
            self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignRight)
            self.pushButton.clicked.connect(self.clear_items)

            self.uic.listWidget.addItem(self.newItem)
            self.uic.listWidget.setItemWidget(self.newItem, self.frame)

            self.list_of_tuples_item_widget.append((self.newItem, self.pushButton))
            
        self.uic.listWidget.itemClicked.connect(lambda x: self.select_items(x))

        # self.uic.listWidget.setIconSize(QSize(100, 100))
        print(numpy.array(self.list_of_tuples_item_widget))

    def select_items(self, x):
        # # remove items widget ===========
        # item_Widget = self.uic.listWidget.currentItem()
        # self.uic.listWidget.removeItemWidget(item_Widget)

        # #  remove items ==================
        # item = self.uic.listWidget.currentRow()
        # self.uic.listWidget.takeItem(item)

        # items name ==================
        if x.text() == "item 0":
            print("item 0 selected")
        elif x.text() == "item 1":
            print("item 1 selected")
        elif x.text() == "item 2":
            print("item 2 selected")

    def clear_items(self):
        item = None
        pointer_to_widget = self.sender()
        print("sender object", pointer_to_widget)
        for list_item in self.list_of_tuples_item_widget:
            if list_item[1] == pointer_to_widget:
                item = list_item[0]
        print('item is {}'.format(item))
        row = self.uic.listWidget.row(item)
        print('row={}'.format(row))
        self.uic.listWidget.takeItem(row)

        # button = self.sender()
        # if button.objectName() == "pushButton_0":
        #     print("pushbutton 0")
        # elif button.objectName() == "pushButton_1":
        #     print("pushbutton 1")
        #     print(button.pos())
        # elif button.objectName() == "pushButton_2":
        #     print("pushbutton 2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
