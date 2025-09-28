from PyQt6.QtWidgets import (
    QMessageBox,
)

class AboutDialog(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About")

        content = """
        This app was created for practise 
        """
        self.setText(content)