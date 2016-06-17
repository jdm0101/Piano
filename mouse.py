import os
import sys
from PySide import QtCore, QtGui

class MDialogWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Mouse Piano")
        self.setGeometry(300, 200, 200, 200)
        vbox = QtGui.QVBoxLayout(self)

        buttongroup = QtGui.QButtonGroup()

        self.radiobuttonD1 = QtGui.QRadioButton("Do", self)
        self.radiobuttonD1.setObjectName("buttonD1")
        buttongroup.addButton(self.radiobuttonD1)
        vbox.addWidget(self.radiobuttonD1)

        self.radiobuttonRe = QtGui.QRadioButton("Re", self)
        self.radiobuttonRe.setObjectName("buttonRe")
        buttongroup.addButton(self.radiobuttonRe)
        vbox.addWidget(self.radiobuttonRe)

        self.radiobuttonM = QtGui.QRadioButton("Mi", self)
        self.radiobuttonM.setObjectName("buttonM")
        buttongroup.addButton(self.radiobuttonM)
        vbox.addWidget(self.radiobuttonM)
        
        self.radiobuttonF = QtGui.QRadioButton("Fa", self)
        self.radiobuttonF.setObjectName("buttonF")
        buttongroup.addButton(self.radiobuttonF)
        vbox.addWidget(self.radiobuttonF)

        self.radiobuttonSo = QtGui.QRadioButton("Sol", self)
        self.radiobuttonSo.setObjectName("buttonSo")
        buttongroup.addButton(self.radiobuttonSo)
        vbox.addWidget(self.radiobuttonSo)

        self.radiobuttonRa = QtGui.QRadioButton("Ra", self)
        self.radiobuttonRa.setObjectName("buttonRa")
        buttongroup.addButton(self.radiobuttonRa)
        vbox.addWidget(self.radiobuttonRa)

        self.radiobuttonS = QtGui.QRadioButton("Si", self)
        self.radiobuttonS.setObjectName("buttonS")
        buttongroup.addButton(self.radiobuttonS)
        vbox.addWidget(self.radiobuttonS)

        self.radiobuttonD2 = QtGui.QRadioButton("Do", self)
        self.radiobuttonD2.setObjectName("buttonD2")
        buttongroup.addButton(self.radiobuttonD2)
        vbox.addWidget(self.radiobuttonD2)

        self.button = QtGui.QPushButton("Play", self)
        self.button.setObjectName("play")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.clicked)

        self.resize(350,200)

    def clicked(self):
        if self.radiobuttonD1.isChecked():
            os.system("aplay /var/www/DO1.WAV")

        elif self.radiobuttonRe.isChecked():
            os.system("aplay /var/www/RE.WAV")

        elif self.radiobuttonM.isChecked():
            os.system("aplay /var/www/MI.WAV")

        elif self.radiobuttonF.isChecked():
            os.system("aplay /var/www/FA.WAV")

        elif self.radiobuttonSo.isChecked():
            os.system("aplay /var/www/SOL.WAV")

        elif self.radiobuttonRa.isChecked():
            os.system("aplay /var/www/RA.WAV")

        elif self.radiobuttonS.isChecked():
            os.system("aplay /var/www/SI.WAV")

        elif self.radiobuttonD2.isChecked():
            os.system("aplay /var/www/DO2.WAV")
    
if __name__ == "__main__":
            app = QtGui.QApplication(sys.argv)
            bw = MDialogWindow()     
            bw.show()
            sys.exit(app.exec_())
