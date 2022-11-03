from .Quest_10 import * 
 

class Quest_9(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("How many schools are in Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("3")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("5")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("4")

        self.next = QPushButton("Question 9", self)
        self.next.setToolTip("CLick to get to the next question")
        self.next.clicked.connect(self.NextFunc)

        layout = QVBoxLayout()
        layout.addWidget(self.quest)
        layout.addWidget(self.answer1)
        layout.addWidget(self.answer2)
        layout.addWidget(self.answer3)
        layout.addWidget(self.next)

        self.setGeometry(200, 200, 300, 350)
        self.setWindowTitle("Question 9")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() == False and self.answer2.isChecked()  and self.answer3.isChecked() == False: 
            dial = Correct_Window("That's correct, very good!")
            self.score += 1
            self.close() 
        else: 
            dial = False_Window("That's not correect, correct answer would be: 5")
            self.close() 

        dial = Quest_10(self.score) 
