from PyQt5.QtWidgets import QApplication    

from .Select import Select

import sys

def main():
    app = QApplication(sys.argv)

    w = Select()

    sys.exit()