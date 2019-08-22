import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import *
import winsound

import time
from os import listdir
from os.path import isfile, join
import subprocess

from playsound import playsound

from math import sqrt

class mainFormDlg(QWidget) :

    def refresh(self):
        self.close()
        subprocess.call("python" + " soundboard.py", shell=True)




    def buttonPress(self, button):
        # self.audioDirectory+"/"+a.text()
        try:
            index = self.soundButtons.id(button)
            index = index * index
            print(index)
            index = int(sqrt(index)-2)
            print(index)
            print("clicked",button.text())
            print(self.soundButtons.id(button))
            print(self.soundButtons.button(self.soundButtons.id(button)))
            print(self.files[index])
            # winsound.PlaySound(self.audioDirectory+"/"+a.text(),winsound.SND_FILENAME)
            playsound(self.audioDirectory+"/"+button.text(),False)
        except Exception as e:
            msg = QMessageBox()
            msg.setText("Failed to play sound")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            # msg.setDetailedText(str(e))
            msg.setStandardButtons(QMessageBox.Ok)
            # msg.buttonClicked.connect(self.ok)
            msg.exec_()

    def centerOnScreen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
        (resolution.height() / 2) - (self.frameSize().height() / 2))

    def __init__(self, parent= None) :
        super(mainFormDlg, self).__init__(parent)
        timer = time.process_time()
        self.setGeometry(0, 0, 300, 100)
        self.setWindowIcon(QIcon('images/icon.png'))
        self.setWindowTitle('dnd app')
        self.centerOnScreen()
        # C:/Users/Otto/Documents/git/soundboard/soundboard/sounds
        self.audioDirectory = "./sounds"
        self.files = []
        try:
            self.files = [f for f in listdir(self.audioDirectory) if f[-3:]=="mp3" and isfile(join(self.audioDirectory, f))]
        except Exception as e:
            msg = QMessageBox()
            msg.setText("No sound directory")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Sound directory not found")
            # msg.setDetailedText(str(e))
            msg.setStandardButtons(QMessageBox.Ok)
            # msg.buttonClicked.connect(self.ok)
            msg.exec_()
        self.buttons = []
        for i in range(0, len(self.files)):
            a = QPushButton(self.files[i])
            self.buttons.append(QPushButton(self.files[i]))
        self.setStyleSheet("""
        QPushButton{
            border-radius: 2px;
            padding: 0.2em 0.2em 0.3em 0.2em;
            border: 1px solid rgb(100, 100, 100);
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #deffe9, stop:0.1 #80e0a0, stop:1  #57a972);
            color: white;
            min-width: 140;
            min-height: 70px;
        }
        """)
        self.mainLayout = QGridLayout()
        # background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f4f4f4, stop:0.1 #8F8F8F, stop:1  #7B7B7B);
        self.soundButtons = QButtonGroup()
        self.soundButtons.setExclusive(True)
        self.soundButtons.buttonClicked.connect(self.buttonPress)

        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #faf0f0, stop:0.1 #e2a9a9, stop:1  #c85b5b);")
        self.refreshButton.clicked.connect(self.refresh)
        x=0
        y=0
        for i in range(0, len(self.buttons)):
            self.buttons[i].setAutoDefault(False)
            self.mainLayout.addWidget(self.buttons[i],y,x)
            x+=1
            if(x==10):
                x=0
                y+=1

            self.soundButtons.addButton(self.buttons[i])
        self.mainLayout.addWidget(self.refreshButton)
        self.setLayout(self.mainLayout)

        # leave this at the end
        # self.splash.finish(self)
        print(time.process_time() - timer, "seconds loading time")

if __name__ == "__main__":
    print("start program")
    app = QApplication([])
    mainWindow = mainFormDlg()
    mainWindow.show()
    sys.exit(app.exec_())
