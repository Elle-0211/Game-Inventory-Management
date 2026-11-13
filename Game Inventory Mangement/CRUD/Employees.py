#Employees Record

from PyQt6.QtWidgets import QDialog, QPushButton, QLineEdit, QComboBox, QMessageBox
from PyQt6.uic import loadUi
from database import DatabaseManager

class Employee(QDialog):
    def __init__(self, db_manager, parent=None):
        super(Employee, self).__init__(parent)
        try:
            loadUi('EmployeesUI.ui', self)
        except Exception as e:
            print(f"Error loading UI file: {e}")
            return
        
        self.db_manager = db_manager

        try:
            self.Search = self.findChild(QPushButton, 'SearchButton')
            self.Add = self.findChild(QPushButton, 'AddButton')
            self.Delete = self.findChild(QPushButton, 'DeleteButton')
            self.Edit = self.findChild(QPushButton, 'EditButton')
            self.EmployeeID = self.findChild(QLineEdit, 'IDEdit')
            self.FName = self.findChild(QLineEdit, 'FnameEdit')
            self.LName = self.findChild(QLineEdit, 'LnameEdit')
            self.comboBox = self.findChild(QComboBox, 'comboBox')

            self.fillComboBox()

            self.Search.clicked.connect(self.on_SearchButton_clicked)
            self.Add.clicked.connect(self.on_AddButton_clicked)
            self.Delete.clicked.connect(self.on_DeleteButton_clicked)
            self.Edit.clicked.connect(self.on_EditButton_clicked)
            self.comboBox.currentTextChanged.connect(self.comboBox_changed)
        except Exception as e:
            print(f"Error initializing Employee dialog: {e}")

    def fillComboBox(self):
        try:
            if self.db_manager.connect():
                query = "SELECT EmployeeID FROM tblEmployees"
                results = self.db_manager.execute_query(query)
                self.comboBox.clear()
                self.comboBox.addItem("--ID--")
                for row in results:
                    self.comboBox.addItem(row[0])
        except Exception as e:
            print(f"Error filling combo box: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()

    def on_SearchButton_clicked(self):
        try:
            employee_id = self.EmployeeID.text()
            if self.db_manager.connect():
                query = "SELECT * FROM tblEmployees WHERE EmployeeID = %s"
                result = self.db_manager.execute_query(query, (employee_id,))
                if result:
                    row = result[0]
                    self.FName.setText(row[1])
                    self.LName.setText(row[2])
                else:
                    self.FName.clear()
                    self.LName.clear()
        except Exception as e:
            print(f"Error in search button clicked: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()

    def comboBox_changed(self):
        try:
            employee_id = self.comboBox.currentText()
            if employee_id == "--ID--":  #
                self.clearFields()
                return
            if self.db_manager.connect():
                query = "SELECT * FROM tblEmployees WHERE EmployeeID = %s"
                result = self.db_manager.execute_query(query, (employee_id,))
                if result:
                    row = result[0]
                    print(f"Query result: {row}")  
                    self.EmployeeID.setText(row[0])
                    self.FName.setText(row[1])
                    self.LName.setText(row[2])
                else:
                    self.clearFields()
        except Exception as e:
            print(f"Error in combo box changed: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()

    def on_AddButton_clicked(self):
        try:
            employee_id = self.EmployeeID.text()
            first_name = self.FName.text()
            last_name = self.LName.text()
            if self.db_manager.connect():
                query = "INSERT INTO tblEmployees (EmployeeID, Fname, Lname) VALUES (%s, %s, %s)"
                self.db_manager.execute_query(query, (employee_id, first_name, last_name), fetch=False)
                self.db_manager.connection.commit()
                QMessageBox.information(self, "Success", "Record added successfully!")
        except Exception as e:
            print(f"Error in add button clicked: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()
            self.clearFields()
            self.fillComboBox()

    def on_DeleteButton_clicked(self):
        try:
            employee_id = self.EmployeeID.text()
            if self.db_manager.connect():
                query = "DELETE FROM tblEmployees WHERE EmployeeID = %s"
                self.db_manager.execute_query(query, (employee_id,), fetch=False)
                self.db_manager.connection.commit()
                QMessageBox.information(self, "Success", "Record deleted successfully!")
        except Exception as e:
            print(f"Error in delete button clicked: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()
            self.clearFields()
            self.fillComboBox()

    def on_EditButton_clicked(self):
        try:
            employee_id = self.EmployeeID.text()
            first_name = self.FName.text()
            last_name = self.LName.text()
            if self.db_manager.connect():
                query = "UPDATE tblEmployees SET Fname = %s, Lname = %s WHERE EmployeeID = %s"
                self.db_manager.execute_query(query, (first_name, last_name, employee_id), fetch=False)
                self.db_manager.connection.commit()
                QMessageBox.information(self, "Success", "Record edited successfully!")
        except Exception as e:
            print(f"Error in edit button clicked: {e}")
        finally:
            if self.db_manager.connection and self.db_manager.connection.is_connected():
                self.db_manager.close_connection()
            self.clearFields()
            self.fillComboBox()

    def clearFields(self):
        self.EmployeeID.clear()
        self.FName.clear()
        self.LName.clear()
