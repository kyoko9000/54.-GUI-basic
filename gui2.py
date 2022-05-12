# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 396)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton:hover { \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(104, 104, 104);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("QLabel#label:hover { \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icons/cil-settings.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.actionvew_1 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.actionvew_1.setFont(font)
        self.actionvew_1.setObjectName("actionvew_1")
        self.actionview_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.actionview_2.setFont(font)
        self.actionview_2.setObjectName("actionview_2")
        self.hello_1 = QtWidgets.QAction(MainWindow)
        self.hello_1.setObjectName("hello_1")
        self.hello_2 = QtWidgets.QAction(MainWindow)
        self.hello_2.setObjectName("hello_2")
        self.my_1 = QtWidgets.QAction(MainWindow)
        self.my_1.setObjectName("my_1")
        self.my_2 = QtWidgets.QAction(MainWindow)
        self.my_2.setObjectName("my_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.action_5.setText(_translate("MainWindow", "list1"))
        self.action_6.setText(_translate("MainWindow", "list 2"))
        self.actionvew_1.setText(_translate("MainWindow", "view 1"))
        self.actionview_2.setText(_translate("MainWindow", "view 2"))
        self.hello_1.setText(_translate("MainWindow", "hello1"))
        self.hello_2.setText(_translate("MainWindow", "hello 2"))
        self.my_1.setText(_translate("MainWindow", "my 1"))
        self.my_2.setText(_translate("MainWindow", "my 2"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
