from .Quest_3 import * 


class Quest_2(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("What's the name of the castle in Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("There is none")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Castle Neuschwanstein")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Castle Rio")

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
        self.setWindowTitle("Question 2")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() == False and self.answer2.isChecked() == False and self.answer3.isChecked(): 
            dial = Correct_Window("That's right, very good!")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("That's not right, the correct answer would be Schloss Rio.")
            self.score+=0
            self.close() 
        
        dial = Quest_3(self.score)  