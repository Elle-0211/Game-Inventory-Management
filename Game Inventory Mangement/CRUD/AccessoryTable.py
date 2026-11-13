#Accessory Table

from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from database import DatabaseManager


class AccessoryTable(QDialog):
    def __init__(self, db_manager):
        super().__init__()
        loadUi('AccessoryProductTable.ui', self)
        self.db_manager = db_manager
        self.tableProduct = self.findChild(QTableWidget, 'tableWidget')
        self.load_data()
    
    def load_data(self):
        try: 
            if self.db_manager.connect():
                query = "SELECT * FROM tblGameAccessoryProduct"
                results = self.db_manager.execute_query(query)
                self.tableProduct.setRowCount(0)
                for row in results:
                    rowPosition = self.tableProduct.rowCount()
                    self.tableProduct.insertRow(rowPosition)
                    for column, item in enumerate(row):
                        self.tableProduct.setItem(rowPosition, column, QTableWidgetItem(str(item)))
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error loading table: {e}")