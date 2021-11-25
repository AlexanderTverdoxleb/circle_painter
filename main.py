import sys
import random
from PyQt5.QtGui import QPen, QPainter, QBrush, QColor
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from circle_painter import CirclePainter

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sp()

    def sp(self):
        self.setGeometry(200, 200, 800, 800)
        self.draw_button = QPushButton("нарисовать круг", self)
        self.draw_button.setGeometry(10, 100, 150, 50)
        self.circle_painter = CirclePainter(self)
        self.draw_button.clicked.connect(self.circle_painter.update)
        self.circle_painter.setGeometry(200, 200, 800, 800)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
