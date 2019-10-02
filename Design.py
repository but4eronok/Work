import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
<<<<<<< HEAD
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
=======


class Example(QMainWindow):

>>>>>>> e9dad42033a46dc27d7bc50a35e2a63e19a64f3b
    def __init__(self):
        super().__init__()
        self.title = 'Программа'
        self.left = 0
        self.top = 0
        self.width = 500
        self.height = 400
        self.initUI()
<<<<<<< HEAD
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Сформировать', self)
        button.setToolTip('Формирование документа')
        button.move(10,60)
        button.clicked.connect(self.on_click)

        button = QPushButton('Ввести данные', self)
        button.move(10,300)
        button.clicked.connect(self.on_click)
        
        self.show()

    @pyqtSlot()
    def on_click(self):
        print('Здесь типа кнопка что то делает')
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
=======

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
>>>>>>> e9dad42033a46dc27d7bc50a35e2a63e19a64f3b
