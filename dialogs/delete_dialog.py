from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QLabel, QGridLayout
import db
import sqlite3

class DeleteDialog(QDialog):
    def __init__(self, parent=None, student_id=None):
        super().__init__(parent)

        # Basix setting on window
        self.setWindowTitle("Delete Student Data")

        # Keeping parent reference
        self.parent = parent
        self.student_id = student_id

        layout = QGridLayout()

        confirmation = QLabel("Are you sure you want to delete this student?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2);
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout);

        yes.clicked.connect(self.delete_student)
        no.clicked.connect(self.reject)

        self.close()
        confirmation_widget = QMessageBox("");
        confirmation_widget.setWindowTitle("Success");
        confirmation_widget.setText("The records was deleted successfully");
        confirmation_widget.exec();

    def delete_student(self):
        try:
            db.delete_student(self.student_id)
        except Exception as e:
            QMessageBox.critical(self, "Error during process", f"Not successfully deleting: {e}")
            return

            # Refresh the table in parent
        try:
            if self.parent and hasattr(self.parent, "loadData"):
                self.parent.loadData()
        except Exception:
            pass

