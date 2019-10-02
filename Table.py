from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt

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
     
     
if __name__ == "__main__":
    import sys
     
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())