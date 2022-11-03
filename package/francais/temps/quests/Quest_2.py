from .Quest_3 import * 


class Quest_2(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Comment appelle-on le chatêau à Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Il y en a aucun")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Chatêau Neuschwanstein")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Chatêau Rio")

        self.next = QPushButton("Prochaine Question", self)
        self.next.setToolTip("Appuis pour arriver à la prochaine question.")
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
            dial = Correct_Window("C'est correct, très bien.")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("C'est faux, la réponse correct était chatêau Rio.")
            self.score+=0
            self.close() 
        
        dial = Quest_3(self.score)  