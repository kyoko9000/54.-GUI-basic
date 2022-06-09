#  ************************** man hinh loai 2 *************************
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QSize, QEvent, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QMenu
from gui3 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = None
        self.menu1 = None
        self.pos = None
        self.menu = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.list_item_widget = []

        lists = [["linda", "address 0", "road 0"],
                 ["maria", "address 1", "road 1"],
                 ["eva", "address 2", "road 2"]]

        pics = ["pics/1-162018936.jpg",
                "pics/girl-xinh-1-480x600.jpg",
                "pics/gai-xinh.jpg"]

        for list, pic in zip(lists, pics):
            self.newItem = QListWidgetItem()
            self.newItem.setSizeHint(QSize(0, 170))

            self.centralwidget = QtWidgets.QWidget()
            self.centralwidget.setObjectName("centralwidget")
            self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.frame = QtWidgets.QFrame(self.centralwidget)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.frame_2 = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
            self.frame_2.setSizePolicy(sizePolicy)
            self.frame_2.setMaximumSize(QtCore.QSize(150, 150))
            self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_2.setObjectName("frame_2")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.label = QtWidgets.QLabel(self.frame_2)
            self.label.setText("")

            url_image = pic

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

            self.label.setPixmap(QtGui.QPixmap(output))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.horizontalLayout_4.addWidget(self.label)
            self.horizontalLayout_2.addWidget(self.frame_2)
            self.frame_3 = QtWidgets.QFrame(self.frame)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
            self.frame_3.setSizePolicy(sizePolicy)
            self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_3.setObjectName("frame_3")
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.label_2 = QtWidgets.QLabel(self.frame_3)
            font = QtGui.QFont()
            font.setPointSize(15)
            self.label_2.setFont(font)
            self.label_2.setText(" {} \n {} \n {}".format(list[0], list[1], list[2]))
            self.label_2.setObjectName("label_2")
            self.horizontalLayout_3.addWidget(self.label_2)
            self.horizontalLayout_2.addWidget(self.frame_3)
            self.frame_4 = QtWidgets.QFrame(self.frame)
            self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame_4.setObjectName("frame_4")
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.pushButton = QtWidgets.QPushButton(self.frame_4)
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
            self.pushButton.setObjectName("pushButton")
            self.horizontalLayout_5.addWidget(self.pushButton)
            self.horizontalLayout_2.addWidget(self.frame_4)
            self.horizontalLayout.addWidget(self.frame)

            self.list_item_widget.append((self.centralwidget, self.pushButton, self.newItem))
            self.pushButton.hide()
            self.centralwidget.installEventFilter(self)
            self.pushButton.clicked.connect(self.menu_popup)

            self.uic.listWidget.addItem(self.newItem)
            self.uic.listWidget.setItemWidget(self.newItem, self.centralwidget)

        self.uic.listWidget.itemClicked.connect(self.select_items)

    def select_items(self, x):
        row = self.uic.listWidget.row(x)
        # items name ==================
        if row == 0:
            print("item 0 selected")
        elif row == 1:
            print("item 1 selected")
        elif row == 2:
            print("item 2 selected")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Leave:
            for i in self.list_item_widget:
                i[1].hide()

        elif event.type() == QEvent.Enter:
            pointer_to_widget = obj
            for list_item in self.list_item_widget:
                if list_item[0] == pointer_to_widget:
                    item = list_item[1]
                    item.show()
        return super(MainWindow, self).eventFilter(obj, event)
        # return True

    def clear_items(self):
        row = None
        pointer_to_widget = self.button
        print(pointer_to_widget)
        for list_item in self.list_item_widget:
            if list_item[1] == pointer_to_widget:
                item = list_item[2]
                row = self.uic.listWidget.row(item)
                self.uic.listWidget.takeItem(row)
        self.list_item_widget.pop(row)

    def menu_popup(self):
        self.button = self.sender()
        width = self.uic.listWidget.width()
        self.pos = self.sender().parent().parent().parent().pos()

        self.menu = QMenu()
        self.menu.addAction("option 1")
        self.menu.addAction("option 2")

        self.menu1 = self.menu.addMenu("option 3")
        self.menu1.addAction("sub 1")
        self.menu1.addAction("sub 2")

        self.menu.popup(self.mapToGlobal(QPoint(self.pos.x()+width-120, self.pos.y()+120)))
        self.menu.triggered.connect(self.menu_action)

    # def menu_action(self, x):
    #     if x.text() == "option 1":
    #         self.button.setText("option text")
    #     elif x.text() == "option 2":
    #         self.clear_items()
    #     elif x.text() == "sub 1":
    #         print("sub 1")
    #     elif x.text() == "sub 2":
    #         print("sub 2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())