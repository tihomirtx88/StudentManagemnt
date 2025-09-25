from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QToolBar, QStatusBar, QPushButton, QMessageBox
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

from dialogs.insert_dialog import InsertDialog
from dialogs.search_dialog import SearchDialog
from dialogs.edit_dialog import EditDialog
from dialogs.delete_dialog import DeleteDialog
import db  # връзка с базата

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        # Меню
        file_menu = self.menuBar().addMenu("&File")
        edit_menu = self.menuBar().addMenu("&Edit")
        help_menu = self.menuBar().addMenu("&Help")

        # Действия
        add_action = QAction(QIcon("icons/add.png"), "Add student", self)
        add_action.triggered.connect(self.insert)
        file_menu.addAction(add_action)

        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        edit_menu.addAction(search_action)

        about_action = QAction("About", self)
        help_menu.addAction(about_action)

        # Таблица
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

        # Toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(add_action)
        toolbar.addAction(search_action)

        # Status Bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        # Клик върху клетка
        self.table.cellClicked.connect(self.cell_clicked)

    def loadData(self):
        self.table.setRowCount(0)
        students = db.get_all_students()
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.table.setItem(row_number, col_number, QTableWidgetItem(str(data)))

    def insert(self):
        dialog = InsertDialog(self)
        dialog.exec()

    def search(self):
        dialog = SearchDialog(self)
        dialog.exec()

    def cell_clicked(self):
        # Динамични бутони в статус бар
        edit_btn = QPushButton("Edit Records")
        edit_btn.clicked.connect(self.edit)
        delete_btn = QPushButton("Delete Records")
        delete_btn.clicked.connect(self.delete)

        # Премахваме старите бутони
        for child in self.statusbar.findChildren(QPushButton):
            self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_btn)
        self.statusbar.addWidget(delete_btn)

    def edit(self):
        dialog = EditDialog(self)
        dialog.exec()

    def delete(self):
        index = self.table.currentRow()
        if index < 0:
            QMessageBox.warning(self, "Error", "No row selected!")
            return

        id_item = self.table.item(index, 0)
        if not id_item:
            QMessageBox.warning(self, "Error", "Invalid student ID!")
            return

        student_id = int(id_item.text())
        dialog = DeleteDialog(self, student_id)
        dialog.exec()