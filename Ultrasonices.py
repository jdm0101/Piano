import os
import sys
from PySide import QtGui, QtCore

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self). __init__()
        self.initUI()

    def initUI(self):
        self.rad1 = QtGui.QRadioButton("Start", self)
        self.rad1.move(50, 50)

        self.rad2 = QtGui.QRadioButton("exit", self)
        self.rad2.move(170, 50)

        self.btn = QtGui.QPushButton("OK", self)
        self.btn.move(90, 100)

        self.btn.clicked.connect(self.button1Clicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 200)
        self.setWindowTitle('Ultrasonices')
        self.show()
        
    def button1Clicked(self):
        if self.rad1.isChecked():
            os.system("sudo python /var/www/distance.py")

        elif self.rad2.isChecked():
            QtCore.QCoreApplication.instance().quit()


def main() :
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
