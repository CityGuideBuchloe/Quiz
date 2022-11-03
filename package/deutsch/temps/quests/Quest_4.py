from .Quest_5 import * 


class Quest_4(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Wie lautet die Postleitzahl von Buchloe??")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("86807")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("12345")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("68708")

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
        self.setWindowTitle("Frage 4")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("Das ist richig, sehr gut.")
            self.score += 1
            self.close() 
        else: 
            dial = False_Window("Das ist nicht richtig, die richtige Anwtort wäre 86807")
            self.score += 0 
            self.close() 

        dial = Quest_5(self.score) 
