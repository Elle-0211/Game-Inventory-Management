import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from database import DatabaseManager
from GameProduct import GameProduct
from GameProductTable import GameProductTable
from AccessoryProduct import AccessoryProduct
from AccessoryTable import AccessoryTable
from Employees import Employee
from EmployeesTable import EmployeeTable

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('Menu.ui', self)

        self.db = DatabaseManager(user='', password='', host='localhost', database='sales')

        self.actionGameProductRecord.triggered.connect(self.show_game_product)
        self.actionGameProductTable.triggered.connect(self.show_game_product_table)
        self.actionAccessoryProductRecord.triggered.connect(self.show_accessory_product)
        self.actionAccessoryProductTable.triggered.connect(self.show_accessory_product_table)
        self.actionEmployeeRecord.triggered.connect(self.show_employee)
        self.actionEmployeeTable.triggered.connect(self.show_employee_table)
        
    def show_game_product(self):
        pdialog = GameProduct(self.db)
        pdialog.exec()
    
    def show_game_product_table(self):
        ptabledialog = GameProductTable(self.db)
        ptabledialog.exec()
    
    def show_accessory_product(self):
        pdialog = AccessoryProduct(self.db)
        pdialog.exec()
    
    def show_accessory_product_table(self):
        ptabledialog = AccessoryTable(self.db)
        ptabledialog.exec()

    def show_employee(self):
        edialog = Employee(self.db)
        edialog.exec()
    
    def show_employee_table(self):
        etabledialog = EmployeeTable(self.db)
        etabledialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())