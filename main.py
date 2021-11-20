import sys
import random
from PyQt5.QtGui import QPen, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sp()

    def sp(self):
        self.setGeometry(200, 200, 800, 800)
        self.draw_button = QPushButton("нарисовать круг", self)
        self.draw_button.setGeometry(10, 100, 150, 50)
        self.draw_button.clicked.connect(self.update)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
