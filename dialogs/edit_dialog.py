from PyQt6.QtWidgets import (
    QDialog,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
import db


class EditDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Basix setting on window
        self.setWindowTitle("Edit Student Data")
        self.setFixedSize(320, 260)

        # Keeping parent reference
        self.parent = parent

        layout = QVBoxLayout()

        # Taking index from curren row
        index = self.parent.table.currentRow()

        if index < 0:  #
            QMessageBox.warning(self, "Error", "Please select a row to edit.")
            self.close()
            return

        #Taking all cels
        id_item = self.parent.table.item(index, 0)
        name_item = self.parent.table.item(index, 1)
        course_item = self.parent.table.item(index, 2)
        mobile_item = self.parent.table.item(index, 3)

        # Chck is it valid the cels
        if id_item is None or name_item is None:
            QMessageBox.warning(self, "Error", "The row include not valid data.")
            self.close()
            return

        #Change the id to be int
        try:
            self.student_id = int(id_item.text())
        except (ValueError, TypeError):
            QMessageBox.warning(self, "Error", "Invalid student ID.")
            self.close()
            return

        #Taking rows values
        student_name = name_item.text() or ""
        course_name = course_item.text() if course_item else ""
        mobile = mobile_item.text() if mobile_item else ""

        #craeting rows for update and adding current values
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        #Lsit with all courses
        courses = ["Biology", "Math", "Astronomy", "Geography"]
        self.course_name.addItems(courses)
        #If current course match with some of list put it like default
        if course_name in courses:
            self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)

        self.mobile = QLineEdit(mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Create button for action
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        # Taking current values
        name = self.student_name.text().strip()
        course = self.course_name.currentText().strip()
        mobile = self.mobile.text().strip()

        #Validation fields

        # Validation fields
        if not name:
            QMessageBox.warning(self, "Error", "Name is required.")
            return
        if not mobile:
            QMessageBox.warning(self, "Error", "Mobile number is required.")
            return

        try:
            db.update_student(self.student_id, name, course, mobile)
        except Exception as e:
            QMessageBox.critical(self, "Error during process", f"Not successfully updating: {e}")
            return

        # Refresh the table in parent
        try:
            if self.parent and hasattr(self.parent, "loadData"):
                self.parent.loadData()
        except Exception:
            pass

        # ✅ Close the dialog when everything is done
        self.accept()