import random
from PyQt5.QtGui import QPen, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QWidget

class CirclePainter(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

    def paintEvent(self, paint_event):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.randint(1, 100)
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        painter.setBrush(QBrush(QColor(r, g, b)))
        painter.drawEllipse(QPoint(250, 250), a, a)
        painter.end()