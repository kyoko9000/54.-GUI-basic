# ************************** man hinh loai 2 *************************
import sys
# pip install pyqt6
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui1 import Ui_MainWindow
from qroundprogressbar import QRoundProgressBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # 1 ==============color of progressbar===================
        # 1.1 **************simple color ************************
        # self.RoundBar1 = QRoundProgressBar()
        # p1 = QPalette()
        # brush = QBrush(QColor(0, 0, 255))  # line color
        # brush.setStyle(Qt.SolidPattern)
        # p1.setColor(QPalette.Text, QColor(255, 0, 0))  # number color
        # p1.setBrush(QPalette.Active, QPalette.Highlight, brush)
        # # #
        # self.RoundBar2 = QRoundProgressBar()
        # p2 = QPalette()
        # brush = QBrush(QColor(0, 0, 255))  # line color
        # brush.setStyle(Qt.SolidPattern)
        # p2.setBrush(QPalette.AlternateBase, QColor(255, 255, 0))  # color of background
        # p2.setColor(QPalette.Text, QColor(255, 0, 0))  # number color
        # p2.setBrush(QPalette.Active, QPalette.Highlight, brush)
        # # #
        # self.RoundBar3 = QRoundProgressBar()
        # p3 = QPalette()
        # brush = QBrush(QColor(0, 0, 255))  # line color
        # brush.setStyle(Qt.SolidPattern)
        # p3.setColor(QPalette.Text, QColor(255, 0, 0))  # number color
        # p3.setBrush(QPalette.Active, QPalette.Highlight, brush)

        #     #     # 1.2 ****************multi color *******************************
        self.RoundBar1 = QRoundProgressBar()
        p1 = QPalette()
        brush = QBrush(QColor(0, 0, 255))  # line color
        brush.setStyle(Qt.SolidPattern)
        p1.setColor(QPalette.Text, QColor(0, 0, 0))  # color of number
        p1.setBrush(QPalette.Active, QPalette.Highlight, brush)

        self.RoundBar2 = QRoundProgressBar()
        p2 = QPalette()
        p2.setBrush(QPalette.AlternateBase, QColor(0, 0, 255))  # color of background
        p2.setColor(QPalette.Text, QColor(0, 0, 0))  # color of number
        # self.RoundBar2.setNullPosition(QRoundProgressBar.PositionLeft)
        gradientPoints2 = [(0, Qt.green), (0.5, Qt.yellow), (1, Qt.red)]  # color of progressbar
        self.RoundBar2.setDataColors(gradientPoints2)

        self.RoundBar3 = QRoundProgressBar()
        p3 = QPalette()
        p3.setColor(QPalette.Text, QColor(0, 0, 0))  # color of number
        # self.RoundBar3.setNullPosition(QRoundProgressBar.PositionLeft)
        gradientPoints3 = [(0, Qt.green), (0.5, Qt.yellow), (1, Qt.red)]  # color of progressbar
        self.RoundBar3.setDataColors(gradientPoints3)
        #     #     #
        #     #     # 2 ===========setup progressbar style =========================
        self.RoundBar1.setBarStyle(QRoundProgressBar.BarStyle.LINE)
        self.RoundBar1.setValue(30.23)
        self.RoundBar1.setPalette(p1)
        self.RoundBar1.setDecimals(2)
        self.RoundBar1.setOutlinePenWidth(10)  # line style
        self.RoundBar1.setDataPenWidth(8)  # line style
        # self.connectToSlider(self.RoundBar1)
        #     #
        self.RoundBar2.setBarStyle(QRoundProgressBar.BarStyle.DONUT)
        self.RoundBar2.setValue(80.58)
        self.RoundBar2.setPalette(p2)
        self.RoundBar2.setDecimals(2)
        # self.connectToSlider(self.RoundBar2)
        #     #
        self.RoundBar3.setBarStyle(QRoundProgressBar.BarStyle.PIE)
        self.RoundBar3.setValue(70.2)
        self.RoundBar3.setPalette(p3)
        self.RoundBar3.setDecimals(2)
        # self.connectToSlider(self.RoundBar3)
        # #     #
        # #     #     # 3 ===============setup layout ==================================
        lay = self.uic.verticalLayout_3
        lay.addWidget(self.RoundBar1)
        self.setLayout(lay)
        #     #
        lay = self.uic.verticalLayout_4
        lay.addWidget(self.RoundBar2)
        self.setLayout(lay)
        #     #
        lay = self.uic.verticalLayout_5
        lay.addWidget(self.RoundBar3)
        self.setLayout(lay)

    # def connectToSlider(self, bar: QRoundProgressBar):
    #     bar.setRange(self.uic.horizontalSlider.minimum(), self.uic.horizontalSlider.maximum())
    #     bar.setValue(self.uic.horizontalSlider.value())
    #     self.uic.horizontalSlider.valueChanged.connect(bar.setValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
