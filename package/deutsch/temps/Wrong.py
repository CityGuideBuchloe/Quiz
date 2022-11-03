from PyQt5.QtWidgets import QMessageBox 
from PyQt5.QtGui import QIcon

from ...const import FALSE_LOGO


class False_Window(QMessageBox): 
    def __init__(self, correction,parent=None): 
        super().__init__(parent)

        self.setText(correction)

        self.setGeometry(200, 200, 450, 500)
        self.setWindowTitle("Falsch")
        self.setWindowIcon(QIcon(FALSE_LOGO))
        self.exec_()