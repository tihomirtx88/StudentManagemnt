from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import db

class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Search Student")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Enter student name")
        layout.addWidget(self.student_name)

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.search)
        layout.addWidget(search_button)

        self.setLayout(layout)

    def search(self):
        name = self.student_name.text().strip()
        if not name:
            return

        # Връща редовете от базата
        results = db.search_students_by_name(name)
        parent_table = self.parent().table

        # Премахваме всички селекции
        parent_table.clearSelection()

        # Обхождаме таблицата и селектираме редовете с даденото име
        for row in range(parent_table.rowCount()):
            item = parent_table.item(row, 1)  # колоната "Name"
            if item and item.text() == name:
                parent_table.selectRow(row)

        print(f"Found rows: {results}")
        self.close()
