# 1. Function to input choice
def user_choice():
    while True:
        choice = int(input('Enter your choice:\n'))
        if choice == 1:
            csv_input()
            break

        elif choice == 2:
            keyboard_input()
            break

        else:
            print('Invalid choice! Choice can be 1 or 2\n')
            print('Try again!!')
    return choice


# 2. Function: Get input from csv file
def csv_input():
    from plotter import Plotter
    from mbr import MinBoundRect
    from rca import Rca
    from create_objects import points_object, polygon_object
    from read_csv import output_csv, read_from_csv

    input_filepath = '{}'.format(str(input('(Filepath must have backward slashes)\n Enter the filepath: ')))

    pt_x_list = [i.get_x() for i in points_object(input_filepath)]
    pt_y_list = [i.get_y() for i in points_object(input_filepath)]
    poly_x_list = polygon_object('polygon.csv').get_xs()
    poly_y_list = polygon_object('polygon.csv').get_ys()

    instance = MinBoundRect(pt_x_list, pt_y_list, poly_x_list, poly_y_list)
    instance.mbr_func()
    outside_list = instance.points_in_mbr()
    mbr_out = instance.points_outside_mbr()

    print('\nRead input.csv')

    read_from_csv(input_filepath)
    print('Point objects created:--')
    print(points_object(input_filepath))

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

    dict1 = instance_rca.output_id_category(input_filepath)
    print(dict1)

    print('\nWrite output.csv')

    def output_filename():
        filename = '{}.csv'.format(str(input('Enter output filename: ')))
        return filename

    print(output_csv(filepath=output_filename(), dictionary=dict1))

    print('\nPlot polygon and points')
    plotter = Plotter()
    plotter.add_polygon(poly_x_list, poly_y_list)
    for i in range(len(pt_x_list)):
        plotter.add_point(pt_x_list[i], pt_y_list[i], list_of_output[i][0])

    plotter.show()


# 3. Function: takes input from keyboard.
def keyboard_input():
    from create_objects import points_object, polygon_object
    from mbr import MinBoundRect
    from rca import Rca
    from plotter import Plotter

    pt_x_list = [i.get_x() for i in points_object('input.csv')]
    pt_y_list = [i.get_y() for i in points_object('input.csv')]

    print('Insert point information')

    try:  # To catch the error and explain ur error to user
        x = float(input('x coordinate: '))
        y = float(input('y coordinate: '))
        name = input('Enter point name: ')

    except ValueError as v:
        raise Exception('invalid datatype') from None

    # Source: http://stackflow.com/questions/52725278/during-handling-of-the-above-exception-another-exception-occured

    user_info = [(name, x, y)]  # for only one point info from user
    input_data = points_object(user_info)  # this returns a list of Point object from data user inputted
    print(input_data)

    print('categorize point')
    pt_x_list = [i.get_x() for i in input_data]
    pt_y_list = [i.get_y() for i in input_data]
    poly_x_list = polygon_object('polygon.csv').get_xs()
    poly_y_list = polygon_object('polygon.csv').get_ys()

    instance = MinBoundRect(pt_x_list, pt_y_list, poly_x_list, poly_y_list)
    instance.mbr_func()
    outside_list = instance.points_in_mbr()
    mbr_out = instance.points_outside_mbr()

    instance_rca = Rca(pt_x_list, pt_y_list, poly_x_list, poly_y_list, mbr_out, outside_list)
    instance_rca.rca()
    print(instance_rca.get_outside_list())

    def func():
        res = []
        for element in instance_rca.get_outside_list():
            sub = element.split(', ')
            res.append(sub)
        return res

    list_of_output = func()

    print('\nPlot polygon and points')
    plotter = Plotter()
    plotter.add_polygon(poly_x_list, poly_y_list)
    for i in range(len(pt_x_list)):
        plotter.add_point(pt_x_list[i], pt_y_list[i], list_of_output[i][0])

    return plotter.show()
