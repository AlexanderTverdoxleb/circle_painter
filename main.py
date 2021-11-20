import sys

from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.sp()

    def sp(self):
        self.draw_button.clicked.connect(self.update)
        self.radius_edit.setText('0')


    def paintEvent(self, paint_event):
        a = int(self.radius_edit.text())
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        painter.drawEllipse(QPoint(250, 250), a, a)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
