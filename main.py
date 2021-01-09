import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot 
import pyqtgraph as pg
import sys 
import os 

from pendulum import Pendulum 


class MainWindow(qtw.QWidget): 
    def __init__(self): 
        super().__init__() 
        self.setWindowTitle('Pendulums')
        self.setLayout(qtw.QVBoxLayout()) 
        self.plot_pendulums()

        self.timer= QtCore.QTimer()
        self.timer.setInterval(1) 
        self.timer.timeout.connect(self.update_plot) 
        self.timer.start()

        self.show() 
    
    def create_pendulum(self): 
        self.pendulum = Pendulum()

    def plot_pendulums(self): 
        self.container = pg.PlotWidget() 
        self.container.showGrid(x=True, y=True) 
        self.container.hideAxis('bottom')
        self.container.hideAxis('left') 

        self.create_pendulum()
        self.container.setRange(xRange=[(self.pendulum.l1 + self.pendulum.l2)*-1.3, (self.pendulum.l1 + self.pendulum.l2)*1.3])
        self.container.setRange(yRange=[(self.pendulum.l1 + self.pendulum.l2)*-1.3, (self.pendulum.l1 + self.pendulum.l2)*1.3])
        #self.pendulum.update() 


        hour = [0,self.pendulum.x1, self.pendulum.x2] 
        temperature = [0,self.pendulum.y1, self.pendulum.y2]

        self.list_x = [] + [hour[2]]
        self.list_y = [] + [temperature[2]]

        self.second_plot = self.container.plot(self.list_x,self.list_y, pen=None ,symbol='o', symbolSize=1) 
        self.plot = self.container.plot(hour,temperature, symbol='o', symbolSize=5) 

        self.layout().addWidget(self.container)
    
    def update_plot(self):
        self.pendulum.update()

        hour = [0,self.pendulum.x1, self.pendulum.x2] 
        temperature = [0,self.pendulum.y1, self.pendulum.y2]

        self.list_x += [hour[2]]
        self.list_y += [temperature[2]]

        self.plot.setData(hour, temperature) 
        self.second_plot.setData(self.list_x, self.list_y) 


    

    


app = qtw.QApplication([]) #keeps track of things under the hood. 
mw = MainWindow() 
app.exec_() 