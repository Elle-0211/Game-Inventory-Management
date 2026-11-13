#Accessory Product Records

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QPushButton, QComboBox, QLineEdit, QMessageBox
from PyQt6.uic import loadUi
from database import DatabaseManager

class AccessoryProduct(QDialog):
    def __init__(self, db_manager):
        super(AccessoryProduct, self).__init__()
        loadUi('AccessoryRecordUI.ui', self)
        self.db_manager = db_manager

        self.Search = self.findChild(QPushButton, 'SearchButton')
        self.Add = self.findChild(QPushButton, 'AddButton')
        self.Delete = self.findChild(QPushButton, 'DeleteButton')
        self.Edit = self.findChild(QPushButton, 'EditButton')
        self.comboBox = self.findChild(QComboBox, 'comboBox')
        self.CodeEdit = self.findChild(QLineEdit, 'CodeEdit')
        self.AccessoryNameEdit = self.findChild(QLineEdit, 'NameEdit')
        self.PriceEdit = self.findChild(QLineEdit, 'PriceEdit')

        self.fillcomboBox()

        self.Search.clicked.connect(self.on_SearchButton_clicked)
        self.Add.clicked.connect(self.on_AddButton_clicked)
        self.Delete.clicked.connect(self.on_DeleteButton_clicked)
        self.Edit.clicked.connect(self.on_EditButton_clicked)
        self.comboBox.currentTextChanged.connect(self.comboBox_changed)

    def fillcomboBox(self):
        try:
            if self.db_manager.connect():
                query = "SELECT * FROM tblGameAccessoryProduct"
                results = self.db_manager.execute_query(query)
                self.comboBox.clear()
                self.comboBox.addItem("--Accessory Code--")
                for row in results:
                    self.comboBox.addItem(row[0])
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error filling combo box: {e}")

    def on_SearchButton_clicked(self):
        try:
            code = self.CodeEdit.text()
            if self.db_manager.connect():
                query = "SELECT * FROM tblGameAccessoryProduct WHERE AccessoryCode = %s"
                result = self.db_manager.execute_query(query, (code,))
                if result:
                    row = result[0]
                    self.AccessoryNameEdit.setText(row[1])
                    self.PriceEdit.setText(str(row[2]))
                else:
                    self.AccessoryNameEdit.setText("")
                    self.PriceEdit.setText("")
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error in search button clicked: {e}")

    def comboBox_changed(self):
        try:
            code = self.comboBox.currentText()
            if self.db_manager.connect():
                query = "SELECT * FROM tblGameAccessoryProduct WHERE AccessoryCode = %s"
                results = self.db_manager.execute_query(query, (code,))
                if results:
                    row = results[0]
                    self.CodeEdit.setText(row[0])
                    self.AccessoryNameEdit.setText(row[1])
                    self.PriceEdit.setText(str(row[2]))
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error in combo box changed: {e}")

    def on_AddButton_clicked(self):
        try:
            code = self.CodeEdit.text()
            name = self.AccessoryNameEdit.text()
            try:
                price = int(self.PriceEdit.text())
            except ValueError:
                QMessageBox.information(self, "Input Successful", "Record added successfully!")
                return

            if self.db_manager.connect():
                query = "INSERT INTO tblGameAccessoryProduct (AccessoryCode, AccessoryName, AccessoryPrice) VALUES (%s, %s, %s)"
                self.db_manager.execute_query(query, (code, name, price), fetch=False)
                self.db_manager.connection.commit()
                self.fillcomboBox()
                self.CodeEdit.setText("")
                self.AccessoryNameEdit.setText("")
                self.PriceEdit.setText("")
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error in add button clicked: {e}")

    def on_DeleteButton_clicked(self):
        try:
            code = self.CodeEdit.text()
            if self.db_manager.connect():
                query = "DELETE FROM tblGameAccessoryProduct WHERE AccessoryCode = %s"
                self.db_manager.execute_query(query, (code,), fetch=False)
                self.db_manager.connection.commit()
                self.CodeEdit.setText("")
                self.AccessoryNameEdit.setText("")
                self.PriceEdit.setText("")
                self.fillcomboBox()
                self.db_manager.close_connection()
        except Exception as e:
            print(f"Error in delete button clicked: {e}")

    def on_EditButton_clicked(self):
        try:
            code = self.CodeEdit.text()
            name = self.AccessoryNameEdit.text()
            try:
                price = int(self.PriceEdit.text())
            except ValueError:
                QMessageBox.information(self, "Input Successful", "Record edited successfully!")
                return

            if self.db_manager.connect():
                query = "UPDATE tblGameAccessoryProduct SET AccessoryName = %s, AccessoryPrice = %s WHERE AccessoryCode = %s"
                self.db_manager.execute_query(query, (name, price, code), fetch=False)
                self.db_manager.connection.commit()
                self.CodeEdit.setText("")
                self.AccessoryNameEdit.setText("")
                self.PriceEdit.setText("")
                self.db_manager.close_connection()
        except Exception as  e:
            print(f"Error in edit button clicked: {e}")


