import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, \
    QGridLayout, QPushButton, QMainWindow
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("Student Managment System");

        file_menu_item = self.menuBar().addMenu("&File");
        help_menu_item = self.menuBar().addMenu("&Help");

        add_student_action = QAction("Add student", self);
        file_menu_item.addAction(add_student_action);

        about_action = QAction("About", self);
        help_menu_item.addAction(about_action);

app = QApplication(sys.argv)
calculator = MainWindow()
calculator.show()
sys.exit(app.exec())