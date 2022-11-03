from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon

from ...const import HELP_LOGO


class Help_Window(QDialog): 
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.label = QLabel(self)
        self.label.setText("""Welcome to the quiz about Buchloe!
        \nWenn you start the quiz, 10 questions will wait for you,
        \nafter finishing it you will see how good you know Buchloe. 
        \nHave fun!""")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.setGeometry(200, 200, 300, 150)
        self.setWindowTitle("Buchloe Quiz")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(HELP_LOGO))
        self.exec_()
