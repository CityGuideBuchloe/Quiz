from .Quest_6 import * 
 

class Quest_5(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)
        
        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Quelles 4 villes font part de la communauté administratif de Buchloe?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Buchloe, Jengen, Lamerdingen et Waal")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Dösingen, Germaringen, Westendorf et Schwabmünchen")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Wiedergeltingen, Amberg, Schwabmünchen et Türkheim")

        self.next = QPushButton("Prochaine Question", self)
        self.next.setToolTip("C'est correct, très bien.")
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
            dial = Correct_Window("C'est correct, très bien.")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("C'est faux, la réponse correct était: Buchloe, Jengen, Lamerdingen et Waal")
            self.score+=0
            self.close() 
        
        dial = Quest_6(self.score)