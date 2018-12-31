from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import sys

import motorlib

class GraphWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        loadUi("MainWindow.ui", self)

        self.loadDefaultMotor()

        self.setupMenu()

        self.show()

    def setupMenu(self):
        self.actionRunSimulation.triggered.connect(self.runSimulation)

    def runSimulation(self):
        print("Running a sim!")
        t, k, p, f, m_flow, m_flux = self.motor.runSimulation()
        print(t)
        self.graphWidget.showData(t, [k, [motorlib.convert(pr, 'mpa', 'psi') for pr in p]])

    def loadDefaultMotor(self):
        self.motor = motorlib.motor()
        bg = motorlib.batesGrain()
        bg.setProperties({'diameter':0.083058, 
                  'length':0.1397, 
                  'coreDiameter':0.03175, 
                  'inhibitedEnds':0,
                  'prop':{
                    'density': 1690, 
                    'a': 3.517054143255937e-05, 
                    'n': 0.3273, 
                    't': 2770, 
                    'm': 23.67, 
                    'k': 1.21}})
        self.motor.grains.append(bg)
        self.motor.nozzleThroat = 0.0102616
        self.motor.nozzleExit = 0.015


#import matplotlib
#matplotlib.use('Qt4Agg')

"""from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

tm = motorlib.motor()

bg = motorlib.batesGrain()
bg.setProperties({'diameter':0.083058, 
                  'length':0.1397, 
                  'coreDiameter':0.03175, 
                  'inhibitedEnds':0,
                  'prop':{
                    'density': 1690, 
                    'a': 3.517054143255937e-05, 
                    'n': 0.3273, 
                    't': 2770, 
                    'm': 23.67, 
                    'k': 1.21}})

bg2 = motorlib.batesGrain()
bg2.setProperties({'diameter':0.083058, 
                  'length':0.1397, 
                  'coreDiameter':0.03175, 
                  'inhibitedEnds':0,
                  'prop':{
                    'density': 1690, 
                    'a': 3.517054143255937e-05, 
                    'n': 0.3273, 
                    't': 2770, 
                    'm': 23.67, 
                    'k': 1.21}})

bg3 = motorlib.batesGrain()
bg3.setProperties({'diameter':0.083058, 
                  'length':0.1397, 
                  'coreDiameter':0.05, 
                  'inhibitedEnds':0,
                  'prop':{
                    'density': 1890, 
                    'a': 0.000101, 
                    'n': 0.319, 
                    't': 1720, 
                    'm': 41.98, 
                    'k': 1.133}})

tm.grains.append(bg)
tm.grains.append(bg2)
#tm.grains.append(bg3)
tm.nozzleThroat = 0.0102616
tm.nozzleExit = 0.015
#tm.nozzle = 0.01428

#print(tm.calcKN([0]))
#print(tm.calcIdealPressure([0]))

t, k, p, f, m_flow, m_flux = tm.runSimulation()
plt.plot(t, f)
plt.plot(t, [pr/6895 for pr in p])
plt.plot(t, k)
plt.show()

for g in m_flow:
    plt.plot(t, g)
plt.show()

for g in m_flux:
    plt.plot(t, g)
plt.show()"""

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = GraphWindow()
    sys.exit(app.exec_())