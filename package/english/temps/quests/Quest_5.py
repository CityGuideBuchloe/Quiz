from .Quest_6 import * 
 

class Quest_5(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)
        
        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Which 4 villages are part of the management community Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Buchloe, Jengen, Lamerdingen and Waal")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Dösingen, Germaringen, Westendorf and Schwabmünchen")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Wiedergeltingen, Amberg, Schwabmünchen and Türkheim")

        self.next = QPushButton("Next question", self)
        self.next.setToolTip("Click to get to the next question")
        self.next.clicked.connect(self.NextFunc)

        layout = QVBoxLayout()
        layout.addWidget(self.quest)
        layout.addWidget(self.answer1)
        layout.addWidget(self.answer2)
        layout.addWidget(self.answer3)
        layout.addWidget(self.next)

        self.setGeometry(200, 200, 300, 350)
        self.setWindowTitle("Question 5")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("That's right, very good!")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("That's not correct, correct answer would be: Buchloe, Jengen, Lamerdingen and Waal")
            self.score+=0
            self.close() 
        
        dial = Quest_6(self.score)