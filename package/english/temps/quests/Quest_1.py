from .Quest_2 import * 


class Quest_1(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Which rivers can you find in Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Gennach and Salach")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Rhein and Donau")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Elbe and Wertach")

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
        self.setWindowTitle("Question 1")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("That's right, very good!")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("That's not right, correct answer would be: Gennach and Salach.")
            self.score+=0
            self.close() 
        
        dial = Quest_2(self.score) 
