from .Quest_7 import * 
 

class Quest_6(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Wie heißt der benachbarte Freizeitpark??")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Europa Park")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Skyline Park")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Legoland")

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
        self.setWindowTitle("Frage 6")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() == False and self.answer2.isChecked() and self.answer3.isChecked() == False: 
            dial = Correct_Window("Das ist richig, sehr gut.")
            self.score += 1
            self.close() 
        else: 
            dial = False_Window("Das ist nicht richtig, die richtige Anwtort wäre der Skyline Park")
            self.close() 
        
        dial = Quest_7(self.score) 