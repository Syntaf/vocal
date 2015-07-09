################################
#Created on Jul 9, 2015
#
#@author: nqian
###############################
from Tkinter import Toplevel
import numpy as np

from ccplot.hdf import HDF
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, \
    NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import ccplot


class ExtractDialog(Toplevel):
    """
    Displays a subplot containing the data bounded by a shape
    """

    def __init__(self, root, shape, filename, x_range, y_range):
        """
        Instantiates attributes
        
        :param: root: root Tk widget
        :param: shape: The shape that bounds the data
        :param: filename: The name of the file on display 
        """
        Toplevel.__init__(self, root)
        x_vals = [0, 3, 10, 15]
        y_vals = [232, 120, 45, 23]
        
        self.shape = shape
        self.filename = filename
        self.x_range = x_range
        self.y_range = y_range
        self.fig = Figure(figsize=(8, 5))
        self.ax = self.fig.add_subplot(1, 1, 1)
        self.plot = self.ax.plot(x_vals, y_vals, 'k-')
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Altitude (km)')
        self.ax.set_title('Horse Stable')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=0)
#         toolbar = NavigationToolbar2TkAgg(self.canvas, self)
#         toolbar.grid(row=1)
#         toolbar.update()
        self.title("Data Subplot")
        self.read_shape_data()
        
    def read_shape_data(self):
        x1 = self.x_range[0]
        x2 = self.x_range[1]
        h1 = self.y_range[0]
        h2 = self.y_range[1]
        plot = self.shape.get_plot()
        with HDF(self.filename) as product:
            time = product['Profile_UTC_Time'][x1:x2, 0]
            height = product['metadata']['Lidar_Data_Altitudes']
            dataset = product['Total_Attenuated_Backscatter_532'][x1:x2]
            
            time = np.array([ccplot.utils.calipso_time2dt(t) for t in time])
            dataset = np.ma.masked_equal(dataset, -9999)
            X = np.arange(x1, x2, dtype=np.float32)
            Z, null = np.meshgrid(height, X)
            
            print time
            print height
            print len(dataset.shape)
            print dataset[0][3]
            print X
            print Z
            print null