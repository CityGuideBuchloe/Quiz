from .Quest_4 import *


class Quest_3(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("Welche sind die 4 Ehrenbürger der Stadt??")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("Alexander und Antonie Moksel, Horst Seehofer, Erwin Neher")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("Rudolf Fuhrmann, Leonard Becker, Til Mohry, Dr. Angela Bogner")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("Berndt-Christian Günther, Miriam Huibens, Florian Kohl, Martin Hallas")

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
        self.setWindowTitle("Frage 3")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("Das ist richig, sehr gut.")
            self.score+=1
            self.close() 
        else: 
            dial = False_Window("Das ist nicht richtig, die richtige Anwtort wäre Alexander und Antonie Moksel, Horst Seehofer und Erwin Neher")
            self.score+=0
            self.close() 
       
        dial = Quest_4(self.score) 
