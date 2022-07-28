from plotter import Plotter
from mbr import MinBoundRect
from rca import Rca
from create_objects import points_object, polygon_object
from read_csv import output_csv, read_from_csv

pt_x_list = [i.get_x() for i in points_object('input.csv')]
pt_y_list = [i.get_y() for i in points_object('input.csv')]
poly_x_list = polygon_object('polygon.csv').get_xs()
poly_y_list = polygon_object('polygon.csv').get_ys()

instance = MinBoundRect(pt_x_list, pt_y_list, poly_x_list, poly_y_list)
instance.mbr_func()
outside_list = instance.points_in_mbr()
mbr_out = instance.points_outside_mbr()


def main():
    plotter = Plotter()
    print('\nRead polygon.csv')

    read_from_csv('polygon.csv')
    print('Polygon objects created:--')
    print(points_object('polygon.csv'))  # To read list of x,y coordinated from csv file

    print('\nRead input.csv')
    read_from_csv('input.csv')
    print('Point objects created:--')
    print(points_object('input.csv'))

    print('\nCategorize points')
    instance_rca = Rca(pt_x_list, pt_y_list, poly_x_list, poly_y_list, mbr_out, outside_list)
    instance_rca.rca()
    instance_rca.get_outside_list()

    def func():
        res = []
        for element in instance_rca.get_outside_list():
            sub = element.split(', ')
            res.append(sub)
        return res

    list_of_output = func()

    dict1 = instance_rca.output_id_category('input.csv')
    print(dict1)

    print('\nWrite output.csv')
    print(output_csv(filepath='out.csv', dictionary=dict1))

    print('\nPlot polygon and points')
    plotter.add_polygon(poly_x_list, poly_y_list)
    for i in range(len(pt_x_list)):
        plotter.add_point(pt_x_list[i], pt_y_list[i], list_of_output[i][0])
    plotter.add_mbr([min(poly_x_list), max(poly_x_list), max(poly_x_list), min(poly_x_list), min(poly_x_list)],
                    [min(poly_y_list), min(poly_y_list), max(poly_y_list), max(poly_y_list), min(poly_y_list)])

    plotter.show()


if __name__ == '__main__':
    main()
