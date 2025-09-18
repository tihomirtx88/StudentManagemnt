import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, \
    QGridLayout, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtGui import QAction
import sqlite3

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

        self.table = QTableWidget();
        self.table.setColumnCount(4);
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"));
        self.table.verticalHeader().setVisible(False);
        self.setCentralWidget(self.table);

    def loadData(self):
        connection = sqlite3.connect("database.db");
        result = connection.execute("SELECT * FROM students");
        self.table.setRowCount(0);

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number);
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)));

        connection.close();

app = QApplication(sys.argv)
calculator = MainWindow()
calculator.show()
calculator.loadData();
sys.exit(app.exec())