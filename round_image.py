from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        url_image = 'pics/1-162018936.jpg'

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

        self.pPic = QtWidgets.QLabel()
        self.pPic.setPixmap(output)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.pPic, alignment=QtCore.Qt.AlignCenter)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
