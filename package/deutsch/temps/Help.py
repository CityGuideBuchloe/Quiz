from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import HELP_LOGO


class Help_Window(QDialog): 
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.label = QLabel(self)
        self.label.setText("""Willkommen bei dem Quiz über die Stadt Buchloe!
        \nWenn sie das Quiz starten, erwarten sie 10 Fragen über Buchloe,
        \nam Ende werden sie wissen wie gut sie das Tor zum Allgäu kennen.
        \nViel Spaß!""")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setGeometry(200, 200, 300, 150)
        self.setWindowTitle("Buchloe Quiz")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(HELP_LOGO))
        self.exec_()
