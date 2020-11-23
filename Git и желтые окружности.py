import sys

from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush, QPainterPath



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Git и желтые окружности.ui', self)  # Загружаем дизайн

        self.pushButton.clicked.connect(self.da)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        self.qp = QPainter()
        self.path = QPainterPath()
        # Начинаем процесс рисования
        self.qp.begin(self)
        self.draw_flag()
        # Завершаем рисование
        self.qp.end()

    def draw_flag(self):
        a = randint(5, 450)
        self.qp.setBrush(QColor('yellow'))
        # Рисуем прямоугольник заданной кистью
        self.qp.drawEllipse(250 - a / 2, 275 - a / 2, a, a)

    def da(self):
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())