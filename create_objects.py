from read_csv import get_point_cor
from classes import Point, Polygon


def points_object(filepath):
    if isinstance(filepath, str) and filepath.endswith('.csv'):  # reads csv files and creates point objects from them
        point_obj_list = []
        for i in get_point_cor(filepath):
            point_obj_list.append(Point('Id', i[0], i[1]))

    elif isinstance(filepath, list):  # creates point object from list

        for i in filepath:
            point_obj_list = [Point(i[0], i[1], i[2]) for i in filepath]
    return point_obj_list


def polygon_object(filepath):
    return Polygon('polygon', points_object(filepath))


