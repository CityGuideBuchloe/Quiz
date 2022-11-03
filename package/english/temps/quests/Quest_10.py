from PyQt5.QtWidgets import QDialog, QLabel, QCheckBox, QPushButton, QVBoxLayout 
from PyQt5.QtGui import QIcon
  
from ..Wrong import False_Window
from ..Correct import Correct_Window
from ..Score import Finish_Window

from ....const import QUEST_LOGO


class Quest_10(QDialog): 
    def __init__(self, score, parent=None): 
        super().__init__(parent)

        self.score = score

        self.quest = QLabel(self)
        self.quest.setText("How long is the Gennach?")

        self.answer1 = QCheckBox(self)
        self.answer1.setText("47km")

        self.answer2 = QCheckBox(self)
        self.answer2.setText("30km")

        self.answer3 = QCheckBox(self)
        self.answer3.setText("24km")

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
        self.setWindowTitle("Question 10")
        self.setLayout(layout)
        self.setWindowIcon(QIcon(QUEST_LOGO))
        self.exec_()

    def NextFunc(self): 
        if self.answer1.isChecked() and self.answer2.isChecked() == False and self.answer3.isChecked() == False: 
            dial = Correct_Window("That's correct, very good!")
            self.score += 1
            self.close() 
        else: 
            dial = False_Window("That's not correct, correct answer would be: 47km")
            self.close() 

        
        Finish_Window(self.score)


