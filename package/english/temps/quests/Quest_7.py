from .Quest_8 import * 



class Quest_7(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)
        
        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Name the two partner citys of Buchloe:")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Cesson (France) and Köszeg (Hungary)")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Amsterdam(Netherlands) and Lorgues(France)")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Besancon(France) and Reykjavìk(Iceland)")

        self.next = QPushButton("Next Question", self)
        self.next.setToolTip("Click to get to the next question")
        self.next.clicked.connect(self.NextFunc)

        layout = QVBoxLayout()
        layout.addWidget(self.quest)
        layout.addWidget(self.answer1)
        layout.addWidget(self.answer2)
        layout.addWidget(self.answer3)
        layout.addWidget(self.next)

        self.setGeometry(200, 200, 300, 350)
        self.setWindowTitle("Question 7")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("That's correct, very good!")
            self.score += 1 
            self.close() 
        else: 
            dial = False_Window("That's not correct, correct answer would be: Cesson (France) und Köszeg(Hungary)")
            self.close() 

        dial = Quest_8(self.score) 