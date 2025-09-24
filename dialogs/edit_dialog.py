from PyQt6.QtWidgets import QDialog, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QMessageBox
import db

class EditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Edit Student Data")
        self.setFixedSize(300, 250)