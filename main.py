#!C:\Users\Me\AppData\Local\Programs\Python\Python38\python.exe

###################################
##### Main.py Kalkulator ########
###################################

import sys
from PyQt5.QtWidgets import QApplication
from MainForm import *

if __name__ == '_main_':
    a = QApplication(sys.argv)

    form = MainForm()
    form.show()

    a.exec_()