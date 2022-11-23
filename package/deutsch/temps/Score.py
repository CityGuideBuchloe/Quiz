from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon


from ...const import MAIN_LOGO, WEB_LOGO, INSTA_LOGO

import webbrowser

class Finish_Window(QDialog): 
    def __init__(self,score,parent=None): 
        super().__init__(parent)

        self.text = QLabel(f"""Sie haben den Test vollständig durchlaufen.
        \nPunktzahl: {score}/10.
        \nBesuchen sie uns auf Instgram oder auf unserer Website:\n""")

        self.insta = QPushButton("Instagram", self)
        self.insta.setIcon(QIcon(INSTA_LOGO))
        self.insta.setToolTip("Klicken zum öffnen unserer Instagram-Seite.")
        self.insta.clicked.connect(self.open_instagram)

        self.site = QPushButton("Website", self)
        self.site.setIcon(QIcon(WEB_LOGO))
        self.site.setToolTip("Klicken zum öffnen unserer Website.")
        self.site.clicked.connect(self.open_website)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.insta)
        self.h_layout.addWidget(self.site)

        self.root_layout = QVBoxLayout()
        self.root_layout.addWidget(self.text)
        self.root_layout.addLayout(self.h_layout)

        self.setGeometry(200, 200, 275, 150)
        self.setWindowTitle("Abgeschlossen")
        self.setLayout(self.root_layout)
        self.setWindowIcon(QIcon(MAIN_LOGO))
        self.exec_()

    def open_instagram(self):
        webbrowser.open_new_tab("https://www.instagram.com/unterwegs_inbuchloe/")

    def open_website(self):
        webbrowser.open_new_tab("https://cityguidebuchloe.github.io/")
