"""Creating a class to calculate the Minimum Boundary Rectangle: Gives surety about points that are definitely
outside the polygon"""

from create_objects import points_object, polygon_object

pt_x_list = [i.get_x() for i in points_object('input.csv')]
pt_y_list = [i.get_y() for i in points_object('input.csv')]
poly_x_list = polygon_object('polygon.csv').get_xs()
poly_y_list = polygon_object('polygon.csv').get_ys()


class MinBoundRect:
    def __init__(self, pt_x_list, pt_y_list, poly_x_list, poly_y_list):
        """" class MinBoundReact takes 4 arguments as input: coordinates(x and y) of test points and coordinates(x,
        y) of polygon"""

        self.__pt_x_list = pt_x_list
        self.__pt_y_list = pt_y_list
        self.__poly_x_list = poly_x_list
        self.__poly_y_list = poly_y_list
        self.__mbr_category = []  # To store the category of all points w.r.t MBR
        self.__outside_mbr = []
    # To store position of points outside MBR i.e. points that are definitely outside MBR and index of other categories

    def mbr_func(self):

        """"Here, list x and y coordinates of each point defining polygon and take maximum of x and y coordinates(top-
        right corner) and take minimum of x and y coordinate(bottom-left corner) """

        # Outside MBR points, therefore outside polygon
        for i in range(len(self.__pt_x_list)):
            if (self.__pt_x_list[i] > max(self.__poly_x_list) or self.__pt_y_list[i] > max(self.__poly_y_list) or
                    self.__pt_x_list[i] < min(self.__poly_x_list) or self.__pt_y_list[i] < min(self.__poly_y_list)):
                self.__mbr_category.append('outside')
                self.__outside_mbr.append('outside')

        # Inside MBR points not sure of polygon
            elif min(self.__poly_x_list) < self.__pt_x_list[i] < max(self.__poly_x_list) and min(self.__poly_y_list) \
                    < self.__pt_y_list[i] < max(self.__poly_y_list):
                self.__mbr_category.append('inside')
                self.__outside_mbr.append(([i + 1]))

        # Boundary points of MBR
            else:
                self.__mbr_category.append('boundary')
                self.__outside_mbr.append(i + 1)

    def points_in_mbr(self):             # Returns category of points (inside,outside,boundary) w.r.t MBR
        return self.__mbr_category

    def points_outside_mbr(self):       # Returns outside category + positions of other categories
        return self.__outside_mbr



