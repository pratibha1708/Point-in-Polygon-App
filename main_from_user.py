from plotter import Plotter
from read_csv import read_from_csv
from creativity import input_choice_display
from user_input import user_choice


def main():
    plotter = Plotter()
    print('read polygon.csv')
    read_from_csv('polygon.csv')  # Called Function to read polygon_csv file

    input_choice_display()  # Function to implement GUI which displays choices available to user for input
    user_choice()

    """Function to take user input type and call further function accordingly
    Function to enter choices in terminal
    user_choice() calls the csv_input() or keyboard_input() according to the choice and categorise the points."""

    plotter.show()  # To plot the points


if __name__ == '__main__':
    main()
