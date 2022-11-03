from .Quest_7 import * 
 

class Quest_6(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Comment s'appelle le parc de loisir près de Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Europapark")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Skyline Park")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Legoland")

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
        self.setWindowTitle("Question 6")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() == False and self.answer2.isChecked() and self.answer3.isChecked() == False: 
            dial = Correct_Window("C'est correct, très bien.")
            self.score += 1
            self.close() 
        else: 
            dial = False_Window("C'est faux, la réponse correct était: Skyline Park")
            self.close() 
        
        dial = Quest_7(self.score) 