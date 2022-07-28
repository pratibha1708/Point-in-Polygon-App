class Point:
    def __init__(self, name, x, y):

        self.__name = name
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __repr__(self):                                 # To see what is actually inputted
        return f'Point({self.__x},{self.__y})'


class Polygon:
    """"Points here should be point objects"""

    def __init__(self, name, points):
        self.__name = name
        self.__points = points

    def get_points(self):
        return self.__points

    def get_xs(self):
        return [point.get_x() for point in self.__points]  # all x coordinates in the polygon object

    def get_ys(self):
        return [point.get_y() for point in self.__points]  # all y coordinates in the polygon object
