import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, \
    QGridLayout, QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QVBoxLayout, QComboBox

from PyQt6.QtGui import QAction
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("Student Managment System");

        file_menu_item = self.menuBar().addMenu("&File");
        help_menu_item = self.menuBar().addMenu("&Help");
        edit_menu_item = self.menuBar().addMenu("&Edit");

        add_student_action = QAction("Add student", self);

        # Add method after click button
        add_student_action.triggered.connect(self.insert);
        file_menu_item.addAction(add_student_action);

        about_action = QAction("About", self);
        help_menu_item.addAction(about_action);

        search_action = QAction("Search", self);
        edit_menu_item.addAction(search_action);
        search_action.triggered.connect(self.search);

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

    def insert(self):
        # Call InsertDialog
        dialog = InsertDialog();
        dialog.exec();

    def search(self):
        search = SearchDialog();
        search.exec();

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__();
        self.setWindowTitle("Insert Student Data");
        self.setFixedWidth(300);
        self.setFixedHeight(300);

        layout = QVBoxLayout();

        # Add student name widget
        self.student_name = QLineEdit();
        self.student_name.setPlaceholderText("Name");
        layout.addWidget(self.student_name);

        # Add combo box widjets
        self.course_name = QComboBox();
        courses = ["Biology", "Math", "Astronomy", "Geography"];
        self.course_name.addItems(courses);
        layout.addWidget(self.course_name);

        # Add mobile widgets
        self.mobile = QLineEdit();
        self.mobile.setPlaceholderText("Mobile");
        layout.addWidget(self.mobile);

        # Add submit button
        self.button = QPushButton("Register");
        self.button.clicked.connect(self.add_student);
        layout.addWidget(self.button)

        self.setLayout(layout);

    def add_student(self):
        # Get data from user input
        name = self.student_name.text();
        course = self.course_name.itemText(self.course_name.currentIndex());
        mobile = self.mobile.text();

        # Connect with database and insert data
        connection = sqlite3.connect("database.db");
        cursor = connection.cursor();
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile));
        connection.commit();
        cursor.close();
        connection.close();
        studentManagment.loadData();

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__();
        #Set title and window size
        self.setWindowTitle("Search Student");
        self.setFixedWidth(300);
        self.setFixedHeight(300);

        #Create layout and input widget
        layout = QVBoxLayout();
        self.student_name = QLineEdit();
        self.student_name.setPlaceholderText("Name");
        layout.addWidget(self.student_name);

        #Create button
        button = QPushButton("Search");
        button.clicked.connect(self.search);
        layout.addWidget(button);

        self.setLayout(layout);

    def search(self):
        name = self.student_name.text();
        connection = sqlite3.connect("database.db");
        cursor = connection.cursor();
        results = cursor.execute("SELECT * FROM students WHERE name = ?", (name,));
        rows = list(results);
        print(rows)
        items = studentManagment.table.findItems(name, Qt.MatchFlag.MatchFixedString);
        for item in items:
            studentManagment.table.item(item.row(), 1).setSelected(True);

        cursor.close();
        connection.close();


app = QApplication(sys.argv)
studentManagment = MainWindow()
studentManagment.show()
studentManagment.loadData();
sys.exit(app.exec())