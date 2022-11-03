from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QDialog
from PyQt5.QtGui import QIcon

from .Help import Help_Window
from .quests.Quest_1 import Quest_1

from ...const import MAIN_LOGO

class Root_Window(QDialog): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.score = 0

        self.startButton = QPushButton("Start quiz", self)
        self.startButton.setToolTip("Click to start the quiz.")
        self.startButton.clicked.connect(self.start)

        self.helpButton = QPushButton("Help", self)
        self.helpButton.setToolTip("Click to open the help.")
        self.helpButton.clicked.connect(self.help)

        self.exitButton = QPushButton("Exit", self)
        self.exitButton.setToolTip("Click to exit.")
        self.exitButton.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.startButton)
        layout.addWidget(self.helpButton)
        layout.addWidget(self.exitButton)

        self.setGeometry(150, 150, 350, 300)
        self.setWindowTitle("Buchloe Quiz")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(MAIN_LOGO))
        self.exec_()

    def start(self): 
        dial = Quest_1(self.score)

    def help(self): 
        dial = Help_Window() 