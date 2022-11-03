from .Quest_8 import * 



class Quest_7(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)
        
        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Nenne die beiden Partnerstädte von Buchloe:")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Cesson (Frankreich) und Köszeg(Ungarn)")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Amsterdam(Holland) und Lorgues(Frankreich)")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Besancon(Frankreich) und Reykjavìk(Island)")

        self.next = QPushButton("Nächste Frage", self)
        self.next.setToolTip("Klicke um die zur nächsten Frage zu wechseln...")
        self.next.clicked.connect(self.NextFunc)

        layout = QVBoxLayout()
        layout.addWidget(self.quest)
        layout.addWidget(self.answer1)
        layout.addWidget(self.answer2)
        layout.addWidget(self.answer3)
        layout.addWidget(self.next)

        self.setGeometry(200, 200, 300, 350)
        self.setWindowTitle("Frage 7")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("Das ist richig, sehr gut.")
            self.score += 1 
            self.close() 
        else: 
            dial = False_Window("Das ist nicht richtig, die richtige Anwtort wäre Cesson (Frankreich) und Köszeg(Ungarn)")
            self.close() 

        dial = Quest_8(self.score) 