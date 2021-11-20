import sys
import random

from PyQt5.QtGui import QPen, QPainter, QBrush
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


    def paintEvent(self, paint_event):
        a = random.randint(1,100)
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow))
        painter.drawEllipse(QPoint(250, 250), a, a)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
