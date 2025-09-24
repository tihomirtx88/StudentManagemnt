from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import db
import sqlite3

class DeleteDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)