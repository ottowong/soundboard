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
from playsound import playsound
import subprocess

class mainFormDlg(QWidget) :

    def refresh(self):
        self.close()
        subprocess.call("python" + " soundboard.py", shell=True)



    def buttonPress(self, a):
        # self.audioDirectory+"/"+a.text()
        try:
            print("clicked",a.text())
            # winsound.PlaySound(self.audioDirectory+"/"+a.text(),winsound.SND_FILENAME)
            playsound(self.audioDirectory+"/"+a.text(),False)
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
        files = [f for f in listdir(self.audioDirectory) if f[-3:]=="mp3" and isfile(join(self.audioDirectory, f))]
        self.buttons = []
        for file in files:
            self.buttons.append(QPushButton(file))
        self.setStyleSheet("")
        self.mainLayout = QGridLayout()
        self.soundButtons = QButtonGroup()
        self.soundButtons.setExclusive(True)
        self.soundButtons.buttonClicked.connect(self.buttonPress)

        self.refreshButton = QPushButton("Refresh")
        self.refreshButton.clicked.connect(self.refresh)
        x=0
        y=0
        for i in range(0, len(self.buttons)):

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
