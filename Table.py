from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem,  QPushButton
from PyQt5.QtCore import QSize, Qt
from docxtpl import DocxTemplate
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(480, 80))
        self.setWindowTitle("Данные титульника")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(2)
        table.setRowCount(4)
        table.setHorizontalHeaderLabels(["Наименование", "Значение"])

        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")


        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)

        button = QPushButton('Сформировать', self)
        button.setToolTip('Формирование документа')
        button.move(10, 170)
        button.clicked.connect(lambda: self.create_doc(table))

    def create_doc(self, table):
        doc = DocxTemplate("Templates/Laba_3.docx")
        context = {'номер_лабы': QTableWidget.item(table, 0, 0).text(), 'тема': 'Шаблоны в питоне', 'группа': 'ИУ10-114', 'студент_1': 'Пупа',
                   'студент_2': 'Лупа', 'преподаватель': 'бухгалтерия'}
        doc.render(context)
        doc.save("Templates/Laba_3-final.docx")

        subprocess.call(['open', 'Templates/Laba_3-final.docx'])

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())