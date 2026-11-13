# EmplpoyeesTable

from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi
from database import DatabaseManager

class EmployeeTable(QDialog):
    def __init__(self, db_manager):
        super(EmployeeTable, self).__init__()
        loadUi('EmployeesTable.ui', self)
        self.db_manager = db_manager

        self.tableEmployees = self.findChild(QTableWidget, 'tableWidget')
        self.load_data()

    def load_data(self):
        if self.db_manager.connect():
            query = "SELECT * FROM tblEmployees"
            results = self.db_manager.execute_query(query)
            self.tableEmployees.setRowCount(0)
            for row in results:
                rowPosition = self.tableEmployees.rowCount()
                self.tableEmployees.insertRow(rowPosition)
                for column, item in enumerate(row):
                    self.tableEmployees.setItem(rowPosition, column, QTableWidgetItem(str(item)))
            self.db_manager.close_connection()