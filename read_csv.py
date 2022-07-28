# 1. Function to read the csv file and returns id,x,y list as string
def read_csv(filepath):
    data = []
    with open(filepath, 'r') as f:
        for values in f.readlines():
            values = values.replace('\n', '')
            values = values.split(',')
            data.append(values)
    return data  # reads the entire dataset with headers(id,x,y) as lists (string) of list


# 2. Function to fetch the x_coordinates
def get_xs(filepath):
    data = read_csv(filepath)  # fetching data as lists of list from read_csv function
    data_new = data[1:]
    xy_floats = [[float(j) for j in i] for i in data_new]  # converting strings into floating numbers
    xs = []
    for i in xy_floats:
        xs.append(i[1])  # creating list of x values

    return xs


# 3. Function to fetch the y_coordinates
def get_ys(filepath):
    data = read_csv(filepath)
    data_new = data[1:]
    xy_floats = [[float(j) for j in i] for i in data_new]
    ys = []
    for i in xy_floats:
        ys.append(i[2])  # creating list of y values
    return ys


# 4. Function to fetch the id's of point
def get_id(filepath):
    data = read_csv(filepath)
    data_new = data[1:]
    xy = [[(j) for j in i] for i in data_new]
    id_list = []
    for i in xy:
        id_list.append(i[0])  # creating list of id
    return id_list


# 5. Function to fetch x_coordinates and y_coordinates (in format (x,y) to plot point

def get_point_cor(filepath):
    data = read_csv(filepath)
    data_new = data[1:]
    xy_floats = [[float(j) for j in i] for i in data_new]
    # print(xy_floats)
    xy = []
    for i in xy_floats:
        xy.append([i[1], i[2]])  # creating list of x,y values
    return xy


# 6. Function to give output to csv file

def output_csv(filepath, dictionary):
    with open(filepath, 'w') as f:
        f.write(str('Id, Category\n'))  # Adding headers to csv file

        for key, value in dictionary.items():
            f.write(f'{key},{value}\n')  # To write the output in csv file
    return 'Output can be found in CSV file created'


# 7. Function to read list of x,y coordinates from csv

def read_from_csv(filepath):
    data = []
    with open(filepath, 'r') as f:
        for values in f.readlines():
            values = values.replace('\n', '')
            values = values.split(',')
            data.append(values)

        data_new = data[1:]
        xy_floats = [[float(j) for j in i] for i in data_new]
        # print(xy_floats)
        xy = []
        for i in xy_floats:
            xy.append([i[1], i[2]])  # creating list of x,y values
        return xy
