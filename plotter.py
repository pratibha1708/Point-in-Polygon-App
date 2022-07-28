from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt
from create_objects import points_object
pt_x_list = [i.get_x() for i in points_object('input.csv')]
pt_y_list = [i.get_y() for i in points_object('input.csv')]

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')
        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
        else:
            plt.plot(x, y, 'ko', label='Unclassified')

    def add_mbr(self, x, y):
        plt.plot(x, y, 'c--',label='MBR')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(), loc='lower right', bbox_to_anchor=(-.03, -.09), ncol=1, title='Legend')
        plt.title('TESTING POINTS IN POLYGON')
        plt.xlabel('X-Coordinates')
        plt.ylabel('Y-Coordinates')
        plt.grid(True)

        plt.show()
