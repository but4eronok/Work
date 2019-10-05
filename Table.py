from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtCore import QSize, Qt
from docxtpl import DocxTemplate
import subprocess


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(600, 80))
        self.setWindowTitle("Данные титульника")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(2)
        table.setRowCount(6)
        table.setHorizontalHeaderLabels(["Наименование", "Значение"])

        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")

        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignCenter)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)

        table.setItem(0, 0, QTableWidgetItem("Номер лабы"))
        table.setItem(1, 0, QTableWidgetItem("Тема лабы"))
        table.setItem(2, 0, QTableWidgetItem("Группа"))
        table.setItem(3, 0, QTableWidgetItem("Студент №1"))
        table.setItem(4, 0, QTableWidgetItem("Студент №2"))
        table.setItem(5, 0, QTableWidgetItem("Преподаватель"))

        button = QPushButton('Сформировать', self)
        button.setToolTip('Формирование документа')
        button.move(200, 10)
        button.clicked.connect(lambda: self.create_doc(table))

    def create_doc(self, table):
        doc = DocxTemplate("Templates/Laba_3.docx")
        context = {'номер_лабы': QTableWidget.item(table, 0, 1).text(), 'тема': QTableWidget.item(table, 1, 1).text(),
                   'группа': QTableWidget.item(table, 2, 1).text(), 'студент_1': QTableWidget.item(table, 3, 1).text(),
                   'студент_2': QTableWidget.item(table, 4, 1).text(), 'преподаватель': QTableWidget.item(table, 5, 1).text()}
        doc.render(context)
        doc.save("Templates/Laba_3-final.docx")

        subprocess.call(['open', 'Templates/Laba_3-final.docx'])


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
