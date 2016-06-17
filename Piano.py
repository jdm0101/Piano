#!/var/www/pyton

import os
import sys
from PySide import QtCore, QtGui

class ButtonWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Piano")
        self.setGeometry(300, 200, 200, 200)
        vbox = QtGui.QVBoxLayout(self)

        buttongroup = QtGui.QButtonGroup()
        
        self.radiobutton1 = QtGui.QRadioButton("Mouse Piano", self)
        self.radiobutton1.setObjectName("radio1")
        buttongroup.addButton(self.radiobutton1)
        vbox.addWidget(self.radiobutton1)

        self.radiobutton2 = QtGui.QRadioButton("Ultrasonics Wave Piano", self)
        self.radiobutton1.setObjectName("radio2")
        buttongroup.addButton(self.radiobutton2)
        vbox.addWidget(self.radiobutton2)

        self.button = QtGui.QPushButton("OK", self)
        self.button.setObjectName("button")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.clicked)

        self.resize(350,200)

    def printState(self, button):
            if self.radiobutton1.isChecked():
                os.system("sudo python /var/www/mouse.py")
                   
            elif self.radiobutton2.isChecked():
                os.system("sudo python /var/www/Ultrasonices.py")
                
    def clicked(self):
            self.printState(self.radiobutton1)
            self.printState(self.radiobutton2)
    
if __name__ == "__main__":
            app = QtGui.QApplication(sys.argv)
            bw = ButtonWindow()     
            bw.show()
            sys.exit(app.exec_())
