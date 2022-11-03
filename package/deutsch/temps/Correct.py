from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

from ...const import CORRECT_LOGO

class Correct_Window(QMessageBox): 
    def __init__(self, correction,parent=None): 
        super().__init__(parent)

        self.setText(correction)

        self.setGeometry(200, 200, 450, 500)
        self.setWindowTitle("Korrekt")
        self.setWindowIcon(QIcon(CORRECT_LOGO))
        self.exec_()
