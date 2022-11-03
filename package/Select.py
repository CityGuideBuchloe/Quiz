from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon

from .deutsch import main_deutsch
from .english import main_english
from .francais import main_francais

from .const import CHOICE_LOGO, ENGLISH_LOGO, GERMAN_LOGO, FRENCH_LOGO

class Select(QDialog): 
    def __init__(self, parent=None): 
        super().__init__(parent)

        self.english = QPushButton("English Version", self)
        self.english.setToolTip("Click to get the Quiz in English")
        self.english.setIcon(QIcon(ENGLISH_LOGO))
        self.english.clicked.connect(self.english_func)

        self.deutsch = QPushButton("Deutsche Version", self)
        self.deutsch.setToolTip("Klicke um das Quiz in Deutsch zu starten")
        self.deutsch.setIcon(QIcon(GERMAN_LOGO))
        self.deutsch.clicked.connect(self.deutsch_func)

        self.francais = QPushButton("Version Francaise", self)
        self.francais.setToolTip("Appuis pour faire le Quiz en Francais")
        self.francais.setIcon(QIcon(FRENCH_LOGO))
        self.francais.clicked.connect(self.francais_func)

        layout = QVBoxLayout()
        layout.addWidget(self.english)
        layout.addWidget(self.deutsch)
        layout.addWidget(self.francais)
        
        self.setWindowTitle("Choice / Wahl / Choix")
        self.setWindowIcon(QIcon(CHOICE_LOGO))
        self.setGeometry(150, 150, 450, 300)
        self.setLayout(layout)
        self.exec_()



    def english_func(self):
        self.close()
        main_english() 

    def deutsch_func(self): 
        self.close()
        main_deutsch() 

    def francais_func(self):
        self.close()
        main_francais()