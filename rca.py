from create_objects import points_object, polygon_object
from mbr import MinBoundRect
from read_csv import get_id

pt_x_list = [i.get_x() for i in points_object('input.csv')]
pt_y_list = [i.get_y() for i in points_object('input.csv')]
poly_x_list = polygon_object('polygon.csv').get_xs()
poly_y_list = polygon_object('polygon.csv').get_ys()

instance = MinBoundRect(pt_x_list, pt_y_list, poly_x_list, poly_y_list)
instance.mbr_func()
outside_list = instance.points_in_mbr()
mbr_out = instance.points_outside_mbr()


class Rca:
    # It takes the input from MinBoundReact class and continues the further process to categorize points
    def __init__(self, pt_x_list, pt_y_list, poly_x_list, poly_y_list, mbr_out, outside_list):

        self.__pt_x_list = pt_x_list
        self.__pt_y_list = pt_y_list
        self.__poly_x_list = poly_x_list
        self.__poly_y_list = poly_y_list
        self.__mbr_out = mbr_out  # Stores points outside mbr
        self.__outside_list = outside_list

    def rca(self):
        # It further runs through points, categorised as 'inside' or 'boundary' by mbr_func() to reach final outcome.
        # Cross product and counting number method is used to carry out PIP test

        append = True
        cycle = False  # It is boolean type and it is used to control end of cycle counting number method

        for items in range(len(self.__pt_x_list)):
            # loop through all test points
            xs = self.__pt_x_list[items]
            ys = self.__pt_y_list[items]
            n = len(self.__poly_x_list) - 1
            # n: It is an integer type and stores length of polygon points - 1

            if self.__mbr_out[items] == 'outside':  # gets all points outside mbr
                pass
            else:
                crosses = 0
                # crosses: It is an integer type and is used to increase results of each crossing from counting method
                # It iterates over polygon coordinates and creates boundary by using vertex points
                for vertices in range(len(self.__poly_x_list)):
                    ver_x1 = self.__poly_x_list[vertices]
                    ver_y1 = self.__poly_y_list[vertices]
                    if vertices == n:
                        cycle = True

                    if vertices < len(self.__poly_x_list) - 1:
                        ver_x2 = self.__poly_x_list[vertices + 1]
                        ver_y2 = self.__poly_y_list[vertices + 1]

                    # To check: Point on Line Algorithm
                    # Source: https://blog.csdn.net/zhouzi2018/article/details/81735132?utm_medium=distribute.pc_relevant.none-task-blog-title-2&spm=1001.2101.3001.4242
                    # Author: Elbow Zhouzi, Date: 2018-08-16
                    # The source code is in C++.However, logic remains the same.

                    on_boundary = False
                    # on boundary: It is boolean type and is used to store boundary points
                    if ((xs - ver_x1) * (ver_y2 - ver_y1) == (ver_x2 - ver_x1) * (ys - ver_y1) and
                            min(ver_x1, ver_x2) <= xs <= max(ver_x1, ver_x2) and
                            min(ver_y1, ver_y2) <= ys <= max(ver_y1, ver_y2)):
                        on_boundary = True

                    if on_boundary:
                        category = 'boundary'
                        # category: It is string type and stores the category of point i.e. whether it is inside,
                        # outside or on boundary of polygon.
                        append = True
                        break

                    # Source: https://github.com/sasamil/PointInPolygon_Py/blob/master/pointInside.py#L50
                    # Author: Sasamil, Date: 2021-03-25

                    # To find whether upward crossing or downward crossing
                    if (ver_y1 <= ys < ver_y2) or (ver_y1 > ys >= ver_y2):
                        # compute actual edge-ray intersect x-coordinate
                        x_intersect = (ys - ver_y1) / (ver_y2 - ver_y1)
                        # if xs > (ver_x1 + x_intercept * (ver_x2 - ver_x1)):  # x > intersect - ray towards left
                        if xs < (ver_x1 + x_intersect * (ver_x2 - ver_x1)):  # x < intersect - ray towards right
                            crosses += 1  # valid crossing of y=ys right of x

                    # Finding result of counting number method, after testing all boundary lines:
                    # odd crosses: inside
                    # even crosses: outside

                    if cycle:
                        cycle = False
                        append = True
                        if crosses % 2 != 0:
                            category = 'inside'
                        else:
                            category = 'outside'

                # Updating the list that was created in mbr_func () to give the final outputs together
                if append:
                    self.__outside_list[items] = category
                    append = False
                    cycle = False

    def get_outside_list(self):  # Function that returns the final results.
        return self.__outside_list

    def output_id_category(self, filepath):  # Function to give output with id and category

        # Source: geeksforgeeks.org/python-convert-two-lists-into-a-dictionary
        # Date: 28 Nov,2018

        test_keys = get_id(filepath)
        test_values = self.get_outside_list()
        res = {}
        for key in test_keys:
            for value in test_values:
                res[key] = value
                test_values.remove(value)
                break

        return res


instance_rca = Rca(pt_x_list, pt_y_list, poly_x_list, poly_y_list, mbr_out, outside_list)
